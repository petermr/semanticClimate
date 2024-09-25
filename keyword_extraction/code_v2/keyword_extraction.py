import pandas as pd
from tqdm import tqdm
from argparse import ArgumentParser
from transformers import (
    TokenClassificationPipeline,
    AutoModelForTokenClassification,
    AutoTokenizer,
)
from transformers.pipelines import AggregationStrategy
import numpy as np


# Constructor class for the Hugging Face model
class KeyphraseExtractionPipeline(TokenClassificationPipeline):
    def __init__(self, model, *args, **kwargs):
        super().__init__(
            model=AutoModelForTokenClassification.from_pretrained(model),
            tokenizer=AutoTokenizer.from_pretrained(model),
            *args,
            **kwargs
        )

    def postprocess(self, model_outputs):
        results = super().postprocess(
            model_outputs=model_outputs,
            aggregation_strategy=AggregationStrategy.SIMPLE,
        )
        return np.unique([result.get("word").strip() for result in results])


#
class KeywordExtraction():
    def __init__(self, textfile, html_path, saving_path):
        self.text = []
        self.keyphrases = []
        self.textfile = textfile
        self.html_path = html_path
        self.saving_path = saving_path

        """
        :@params text: List of string variables
        """

    def read_from_text_file(self):
        with open(self.textfile, encoding="utf-8") as file:
            text = file.readlines()
            # print(text[0])
            self.text = text

    def extract_keywords(self):
        self.read_from_text_file()

        model_name = "ml6team/keyphrase-extraction-kbir-inspec"
        for line in tqdm(self.text):
            # print(line)

            extractor = KeyphraseExtractionPipeline(model=model_name)
            keyphrases = extractor(line)
            for i in keyphrases:
                self.keyphrases.append(i)
            # print(self.keyphrases)
        self.keyphrases = [*set(self.keyphrases)]
        print(self.keyphrases)
        # df = pd.DataFrame(self.keyphrases)
        # df.to_csv(self.saving_path + 'keyphrases.csv' ,index=False)
        return self.keyphrases

    def main(self):
        self.extract_keywords()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-i', '--html_path',
                        required=False,
                        help=' path of the HTML file: /...')

    parser.add_argument('-t', '--text_file',
                        required=False,
                        help='path to textfile: /...')

    parser.add_argument('-s', '--saving_path',
                        required=False,
                        help='path of the folder where you want to save the files : /...'
                        )
    args = parser.parse_args()

    html_path = args.html_path  # '/content/semanticClimate/ipcc/ar6/wg3/Chapter06/fulltext.flow.html'
    saving_path = args.saving_path  # '/content/'
    text_file = args.text_file

    keyword_extractions = KeywordExtraction(text_file, html_path, saving_path)
    keyword_extractions.main()
