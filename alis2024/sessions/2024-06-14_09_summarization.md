[Peter Murray-Rust] 09:02:58
Captions and full transcript. Now we're still working out how this, transcribing works and I think it's not too bad with some parts of it.

[Peter Murray-Rust] 09:03:11
But it's. Little bit. Counterproductive with others. So we will, we'll see what we've got.

[Peter Murray-Rust] 09:03:24
Right. We wait just 3 more minutes.

[Peter Murray-Rust] 09:03:32
Did we have a blue tea for you yesterday, Harsaw?

[Harshul Surana] 09:03:40
Yes, we did.

[Peter Murray-Rust] 09:03:41
We did that's fine. Okay.

[Peter Murray-Rust] 09:03:49
Right. Hello, Ranu, how are you? We're not normally takes a minute or 2 to connect because she has 2 devices.

[Peter Murray-Rust] 09:04:03
Smitchie isn't able to come today. So we'll see what happens, right?

[Peter Murray-Rust] 09:04:12
Okay. Do you know, Reno, whether we're expecting other people or not?

[Peter Murray-Rust] 09:04:26
Hello.

[Renu Kumari] 09:04:30
Yes, Nitika Nikita will join and the party that may may or may not join because she is volunteer type of thing.

[Peter Murray-Rust] 09:04:36
Right Yes, and, and what about.

[Renu Kumari] 09:04:39
Currently.

[Renu Kumari] 09:04:43
And I don't have any information, maybe he will come. You need a less.

[Peter Murray-Rust] 09:04:48
Okay, do you, do you have a lab meeting today that you have to

[Renu Kumari] 09:04:54
Yes, it was in the morning. It was in the mornings and now it is over. Until half an hour before it was finished.

[Peter Murray-Rust] 09:04:58
Oh good. Right.

[Renu Kumari] 09:05:03
So.

[Peter Murray-Rust] 09:05:04
Okay, so let's see how we go. So we're being recorded. We're doing captioning.

[Peter Murray-Rust] 09:05:10
And, The hello Excellent.

[Peter Murray-Rust] 09:05:21
So we're at the stage where we, we've recorded most of what we want to put into all of what we want to put into it.

[Peter Murray-Rust] 09:05:32
Simon has written his, very good article. So we've got to get something that, it's up to that sort of standard.

[Peter Murray-Rust] 09:05:42
It's full of pictures, right? So that's, very good. We're not going to have people pictures in it because the idea was it was in that article but we will want some diagrams.

[Peter Murray-Rust] 09:05:55
And in this, but I'll come to the diagrams. And I will have to be responsible for most of the diagrams.

[Peter Murray-Rust] 09:06:05
Okay.

[Peter Murray-Rust] 09:06:10
Let's try and work out the major components of what we're doing. we'll go over what we've recorded and we'll label them.

[Peter Murray-Rust] 09:06:24
And so on. But, before we do that, Has anybody got any problems, any bugs, any comments, any new exciting discoveries.

[Peter Murray-Rust] 09:06:39
We'll come to Harshal after that. Yeah.

[Peter Murray-Rust] 09:06:46
No bugs, okay. Right. Okay. Marshall, can you, I'm going to hand the screen over to you.

[Peter Murray-Rust] 09:06:57
Can you talk us through what you've done with hugging face and, summarization.

[Peter Murray-Rust] 09:07:06
Okay.

[Peter Murray-Rust] 09:07:10
Is that okay?

[Harshul Surana] 09:07:12
Yes, Peter.

[Peter Murray-Rust] 09:07:13
Good, okay. And don't you know, you're, you're among friends, so don't worry if anything, doesn't work out 1st time.

[Harshul Surana] 09:07:24
Sure.

[Peter Murray-Rust] 09:07:28
So you're telling a story, give us at the beginning, it's a good idea with stories that you tell people what you're going to tell them, right?

[Peter Murray-Rust] 09:07:39
So a brief summary, 2 3 sentences, this is what I'm going to show you so that we know where we are.

[Harshul Surana] 09:07:47
Okay.

[Peter Murray-Rust] 09:07:47
And then you give the message and at the end you then summarize by saying this is what we looked at.

[Peter Murray-Rust] 09:07:54
And it's summed up in the model motto.

[Peter Murray-Rust] 09:07:59
Tell them what you're going to tell them. Tell him, tell him what you told them, right?

[Peter Murray-Rust] 09:08:05
Okay. And it's, so tell us what, what we're going to see.

[Harshul Surana] 09:08:07
Okay.

[Peter Murray-Rust] 09:08:12
In overview.

[Renu Kumari] 09:08:15
So it would be from the beginnings. Yes, go after the transcript after the transcript. You can read it from the zoom and yeah.

[Peter Murray-Rust] 09:08:19
Huh.

[Peter Murray-Rust] 09:08:24
Well, no, no.

[Peter Murray-Rust] 09:08:27
So it's Hong Kong is going to say something like, Hi. Explored summarization of our transcripts using hugging face summarize or whatever it is right so that's what you're going to tell us right and and then you might put in a thing to say we're going to see the installation of the transformer then it's customization.

[Renu Kumari] 09:08:34
Hmm.

[Peter Murray-Rust] 09:08:58
Then it's use on an example. Okay. So that's a sort of, introduction.

[Peter Murray-Rust] 09:09:08
Okay. Does that make sense? Right. Yes.

[Harshul Surana] 09:09:10
Good.

[Renu Kumari] 09:09:11
Okay. Kind of tutorial. Yeah.

[Harshul Surana] 09:09:20
Right, so the task at hand was, can we come up with a good summarization for the long transcript text that we have and for that I explored.

[Peter Murray-Rust] 09:09:29
PM?

[Harshul Surana] 09:09:32
2 different approaches that I'm gonna later explain that users having faced transformers which are again open source.

[Harshul Surana] 09:09:40
We And, right, I'll jump into the 1st one. Which was done using a transformer called Bart.

[Peter Murray-Rust] 09:09:45
Yeah.

[Harshul Surana] 09:09:49
And before jumping into that, I can give an overview of what the 2. Broad types of summarization are that I have each tried.

[Harshul Surana] 09:09:58
The 1st one is called extractive summarization. Where the idea is that you compress the long text that you have.

[Harshul Surana] 09:10:08
Without changing the wording. So let's say. You have a thousand word document you want to summarize it.

[Harshul Surana] 09:10:16
No, the way you will do it is not by paraphrasing or by you know using your own deduction or reasoning to paraphrase to you know get to the crux of the document.

[Harshul Surana] 09:10:29
How it is done is that it takes the sentences present in the document largely and it you know compresses that So that is the 1st and that is called extractive summarization.

[Harshul Surana] 09:10:44
Conversely the second type of summarization is called abstractor summarization where it's just the opposite.

[Harshul Surana] 09:10:50
Where, rather than compressing the text itself. The idea is that the model generates text.

[Harshul Surana] 09:11:01
New text that is supposed to be a good summarization for the text. So, we look at both of them.

[Harshul Surana] 09:11:10
This one is for abstractive summarization. The 1st part is obviously installing all the necessary packages.

[Harshul Surana] 09:11:20
And my screen is visible, right?

[Peter Murray-Rust] 09:11:22
Brilliant. That was an excellent introduction, really good.

[Harshul Surana] 09:11:25
Great.

[Harshul Surana] 09:11:30
Thank you. And so this is the bad model that I mentioned which performs abstractive summarization. So here the challenge or the Oh, the particular challenge of us is that our document is long, right?

[Harshul Surana] 09:11:45
And these transformers at 1 point they can only take 500 words as an input. So one part of the pre-processing is to divide the long document into 500.

[Harshul Surana] 09:11:59
Oh, word long, chunks or passages. And the workflow is that the model summarizes these 500 word long passages.

[Harshul Surana] 09:12:15
And coll that and the other the another process on top of that is that it takes those summaries on top of that is that it takes those summaries, concatenates them and generates a summary on top of that.

[Harshul Surana] 09:12:30
So like there are 2. Different types of outputs.

[Harshul Surana] 09:12:36
So I can give an example, I can show how it looks like. So if the If it's visible here, so it says that, it is divided by text into 56 passages.

[Peter Murray-Rust] 09:12:39
I'm absolutely.

[Harshul Surana] 09:12:48
56, 500 word long passages. And

[Peter Murray-Rust] 09:12:51
Quick question, when you say the text, is this a 500 word text or is it the whole lot?

[Harshul Surana] 09:12:59
The text refers to the transcript and the chunks of the passages refer to the 500 word longer.

[Harshul Surana] 09:13:05
It's subdivisions that we're doing.

[Peter Murray-Rust] 09:13:08
Right and and so there are altogether then 2,800 words 56 by 2, by 500.

[Peter Murray-Rust] 09:13:21
28,000.

[Harshul Surana] 09:13:21
56. Great, 56 into 500. Approximately.

[Peter Murray-Rust] 09:13:26
Yeah, so that's that's 28,000.

[Harshul Surana] 09:13:32
Right.

[Peter Murray-Rust] 09:13:33
Right, okay, and is that all of our transcripts?

[Harshul Surana] 09:13:39
No, this is just one of the transcript. The name is, I can look that up.

[Peter Murray-Rust] 09:13:50
Okay, this is very, very good, right?

[Harshul Surana] 09:13:54
It's called meeting saved closed caption. So like I just took one of them for experimenting.

[Peter Murray-Rust] 09:13:58
Yes, we need to now, the next thing we have to do immediately afterwards is give these decent labels, but that's fine.

[Harshul Surana] 09:14:08
Right. So as you can see like for each of the chunks it generates a summary.

[Harshul Surana] 09:14:15
So for example, We have separate channels and slack for different types of discussion. This is the summary for this particular.

[Harshul Surana] 09:14:24
Chunk the 500 word long chunk and, I, another step, what it also does is that it takes all of the summaries generated, concatenates them and generates a summary.

[Harshul Surana] 09:14:40
Of that. So a summary of summaries. And that is.

[Peter Murray-Rust] 09:14:42
Yes.

[Harshul Surana] 09:14:48
That is shown here. But that was not very good. So like that was that didn't come out to be very good.

[Harshul Surana] 09:14:56
So final somebody which other somebody or somebody uses. Summarizes uses tools from zoom and slack. We record videos which have an audio stream in them.

[Peter Murray-Rust] 09:15:02
Yep.

[Harshul Surana] 09:15:06
So it's not very useful. Like from experiments

[Peter Murray-Rust] 09:15:10
How long is, these summaries, how many words are they, they take 500 words are they, they take 500 words and condense them into what lengths.

[Harshul Surana] 09:15:20
The maximum length is 500 by 6, which like which is a hyper parameter I said.

[Harshul Surana] 09:15:26
So, 500 by 6 would be approximately 125 1 30 words. That is the maximum length that I have said.

[Peter Murray-Rust] 09:15:35
So you're condensing. 500 words into 1 30 words.

[Harshul Surana] 09:15:40
Yes, a maximum of 1 30.

[Peter Murray-Rust] 09:15:42
Right. Yes. Excellent.

[Peter Murray-Rust] 09:15:50
And then you

[Harshul Surana] 09:15:50
Do you vote flow for the? Sorry.

[Peter Murray-Rust] 09:15:53
No, and then you're taking all of those. 56, chunks of 1 30 words and, turning them into a single And that but it's making a single final summary.

[Harshul Surana] 09:16:08
I'm writing it to the text file. Yeah.

[Peter Murray-Rust] 09:16:14
So how long is the single final summary?

[Harshul Surana] 09:16:16
The single final summary was in 2 grade. It was just one line.

[Peter Murray-Rust] 09:16:21
Yeah, that's no use to it. Yes. Yes.

[Harshul Surana] 09:16:22
Summarizes using tool from zoom in slack per record videos which have an audio stream we publish all this material record then the transcript onto slide this last for a period over 2 months.

[Peter Murray-Rust] 09:16:27
That's right.

[Harshul Surana] 09:16:34
So I don't know what went wrong there maybe. Something went wrong but yeah like this is the current how it looks.

[Peter Murray-Rust] 09:16:39
Right. So. One of the things is that.

[Peter Murray-Rust] 09:16:45
Whenever you do something like this 1st time, It usually goes wrong and you repeat exactly what you did or you think you did.

[Peter Murray-Rust] 09:16:57
And then it starts getting better. So 1st time through, always with things like this you can expect.

[Harshul Surana] 09:17:05
Okay.

[Peter Murray-Rust] 09:17:05
You know to get something that isn't right.

[Harshul Surana] 09:17:11
And the workflow for a second one is exactly the same. It is just that we use it different transformer to shift from abstractive to extractive.

[Harshul Surana] 09:17:22
So, if Peter, you remember, yes, and you were saying that the summary. Sounds like a 3rd person overview.

[Peter Murray-Rust] 09:17:30
Yes.

[Harshul Surana] 09:17:30
So that is that is a function of that the that is a component of it being summarized using abstractive summarization because like you are generating new lines, paraphrasing, the original content.

[Harshul Surana] 09:17:48
So it looks like a 3rd person has read it and you know given a summary in their own words.

[Peter Murray-Rust] 09:17:52
Right. I wondered whether, so when you gave it to chat GPT, presumably you gave it some sort of prompt.

[Harshul Surana] 09:18:01
Yes.

[Peter Murray-Rust] 09:18:02
And I wondered whether the prompt had, influenced that. In other words, I you said please summarize this and Chatchi PT took summarized to mean write a review of it rather than you know, abstract the meaning in the same style.

[Harshul Surana] 09:18:23
Probably. I used a very simple problem that said like your Like, a very simple problem. Where they are like changing the prompt influences.

[Peter Murray-Rust] 09:18:26
Yes.

[Peter Murray-Rust] 09:18:30
Yeah.

[Harshul Surana] 09:18:34
The output I could, you know, specify, perform extracted summarization and then it probably would stick to performing extractor summarization.

[Peter Murray-Rust] 09:18:45
Okay, that's tremendous. Now, can we have, Svia, Reno and, and ask you questions.

[Peter Murray-Rust] 09:18:57
Do you understand this? What's happened here?

[Renu Kumari] 09:19:07
Yes, Peter, I got this some some not completely but that.

[Peter Murray-Rust] 09:19:14
Shafia, what about you?

[Sravya] 09:19:17
Yeah, I got it, but. Same, I mean, little confused.

[Peter Murray-Rust] 09:19:23
Right, and part yet?

[Parijat Bhadra] 09:19:27
Alright, I think I understand how like it's generating.

[Peter Murray-Rust] 09:19:33
Right, you don't have to understand the. Deep mechanics of it, and what type of network it is, and so on.

[Peter Murray-Rust] 09:19:44
But you have to understand. What the input is, what the expected output is. And then we've got to work out whether it's worth while.

[Peter Murray-Rust] 09:19:58
So. You think it condenses from 500 to a hundred 30 okay Did you feel those?

[Peter Murray-Rust] 09:20:10
130 word summaries. And, gel were useful.

[Harshul Surana] 09:20:20
So I tried, 2 different versions, one by specifying the maximum length as it is, 1 50 words and the other without any without a hard encoding rate.

[Harshul Surana] 09:20:32
But in that case, like it turned out to be very long the document. So like I didn't share it because I felt the other one which uses 150 as the maximum words.

[Harshul Surana] 09:20:44
Give better result according to like my skimming of the output.

[Peter Murray-Rust] 09:20:51
Right, okay. That's very, very useful. And indeed, we'll need to think about it.

[Peter Murray-Rust] 09:21:01
You're showing us code here. Is that taken from, tutorials, so that, or have you had to write that?

[Harshul Surana] 09:21:14
So for obstructive summarization, I got the code from a blog that he had put out of video also explaining what he's doing and like there are links above.

[Harshul Surana] 09:21:25
And for the extractive component, I just had to change the what the model is doing. So I did that myself.

[Peter Murray-Rust] 09:21:33
Right. Okay. We, we will have to find out, how useful this is.

[Peter Murray-Rust] 09:21:45
And I think Probably. You're all.

[Peter Murray-Rust] 09:21:50
All of you should have a look and see whether these. 130 word summaries are useful.

[Peter Murray-Rust] 09:21:59
And, when that's going to help. My feeling is that given this, the way that you've had to divide it into 500

[Peter Murray-Rust] 09:22:13
What chunks is actually better for us to chunk it because it has been the talk has been given on the basis that it's fairly well structured and I think our task is going to go through and turn it into chunks and then we might.

[Peter Murray-Rust] 09:22:32
Repeat on that because your chunks are may overlap 2 concepts or it may not be enough for one concept or something of that sort.

[Peter Murray-Rust] 09:22:44
Does that make sense?

[Harshul Surana] 09:22:45
Okay. And another thing I tried which like did not, like I could not get the results until now is that.

[Peter Murray-Rust] 09:22:46
Yep.

[Harshul Surana] 09:22:53
Initially I tried it using Ch GPT, right? And. So then the better step was to try an open source, language model.

[Harshul Surana] 09:23:03
So I'm I'm working on that code to generate a summary using. An open source language model.

[Harshul Surana] 09:23:13
That could give a better result Lexi because it has a Hi, it has a bigger amount of words that it can process at a single time.

[Harshul Surana] 09:23:24
So like for transformers it is 500 so for that it is 1,000 or in some cases even more.

[Peter Murray-Rust] 09:23:25
That's

[Peter Murray-Rust] 09:23:33
Excellent. And, what are the resource requirements for this?

[Harshul Surana] 09:23:40
That one requires GPU resources. So like yesterday I was trying it out on Kaggle like Kaggle offers certain minimum, GPU.

[Harshul Surana] 09:23:52
Clouds. So I was trying it on that.

[Peter Murray-Rust] 09:23:56
And, do they offer that free or do you have to pay?

[Harshul Surana] 09:24:01
That one is free.

[Peter Murray-Rust] 09:24:03
Good. I should say, to everybody that we don't want any of you to, start paying any money for anything.

[Peter Murray-Rust] 09:24:16
I accept for your connection charges. We can't do anything about that. NIPGR has, you know, installed a powerful, GPU machine.

[Peter Murray-Rust] 09:24:29
I don't know what the load Renew, do you have any feeling for how that machine is used?

[Renu Kumari] 09:24:37
No, no, Peter. We have no information. It is there. Good day.

[Peter Murray-Rust] 09:24:41
Yes. So that's a possibility. And that's is almost certainly, up to, to manage.

[Peter Murray-Rust] 09:24:55
He's done very, very well in, you know, getting this. purchased and installed.

[Peter Murray-Rust] 09:25:04
You know, and what you're doing, what we're doing, so this is a team effort.

[Peter Murray-Rust] 09:25:09
Is maybe very very useful for some of the core business of the institute you can imagine For example, getting a, report from another government institute on, let's say, the, Management of crops or something like that and asking these tools to summarize it.

[Peter Murray-Rust] 09:25:39
You know, and Possibly summarize it with, relevance to an IPGRs, core.

[Peter Murray-Rust] 09:25:47
Disciplines. Does that make sense?

[Renu Kumari] 09:25:53
Yes, it does. Yeah.

[Peter Murray-Rust] 09:25:54
Because I think, you know, the traditional reports and the scientific literature are vastly underused and and it may well be possible, say, if you've got an institute which produces, I don't know, let's say.

[Peter Murray-Rust] 09:26:14
A thousand page a thousand pages of report a year something like that you can see saying what does this institute and you know these will be publicly available you know these will be public available you know can you summarize this institute and you know these will be public available.

[Peter Murray-Rust] 09:26:30
You know, these will be public available. You know, can you summarize this and can you find out, you know, can you summarize this and can you find out, whether and it is particularly involved with genomics or with invasive species or whatever it might be.

[Peter Murray-Rust] 09:26:42
So. This is pioneering work, Castle and I think that's.

[Peter Murray-Rust] 09:26:49
Very exciting indeed, so.

[Peter Murray-Rust] 09:26:53
Right, so the message from this, now, that we need to section our our transcripts, along the lines of what we have, already done.

[Peter Murray-Rust] 09:27:12
But we need to actually put that sectioning in the transcript. And that would make it easier to summarize.

[Peter Murray-Rust] 09:27:21
How long does it, Take to run a hospital and Do you have a limited amount of resources?

[Peter Murray-Rust] 09:27:30
On

[Harshul Surana] 09:27:35
Table has a limited resources for the free tier of GPUs that it provides. And then at the later iterations of the model it was crashing.

[Harshul Surana] 09:27:46
But this one, the transfer based one, there I'm perfectly fine. I ran it on Google.

[Peter Murray-Rust] 09:27:52
Right, okay. So it's offered in Google Calab, is it?

[Harshul Surana] 09:28:01
Google. I've also, it also offers 3 GPUs up to up to a limit but in my experience Cagle offers a much more It offers more compute at for the free tier list.

[Peter Murray-Rust] 09:28:18
Right. Okay. One small thing. Can you explain the difference between Bart and Bert's because they're, when we speak about them, it's easy to confuse them.

[Harshul Surana] 09:28:34
Great.

[Harshul Surana] 09:28:42
At a broad overview level. BART is a encoded with I love I might I don't want to get this wrong

[Harshul Surana] 09:28:59
So there is a difference in the architecture of the models that enables it to perform certain tasks, right?

[Harshul Surana] 09:29:06
So bird for example. Usually it is used for let's say classification. Or you know outputting something that is a label or like a short output.

[Peter Murray-Rust] 09:29:16
Right Yep.

[Harshul Surana] 09:29:18
Compare that to but which is you know pre trained to generate text so like for that for that purpose it is used for abstracted summarization where you know it can generate text.

[Harshul Surana] 09:29:29
And a much more robust way compared to Bert where like internally it is just compressing the texts and then not particularly generating it.

[Peter Murray-Rust] 09:29:40
That's very useful. Okay. I believe, that, is used as a basis of a number of the, Texts tools that we've used already.

[Peter Murray-Rust] 09:29:55
In Docker analysis and so on that I think there and and there are quite a lot of But specialities where it's something, right?

[Harshul Surana] 09:30:06
Good. So for example, biotech is pre-trained on you know abstracts of biomedical literature.

[Peter Murray-Rust] 09:30:08
And the

[Harshul Surana] 09:30:15
And a different bird, let's say, is. Pre-trained on documents that are particularly financial let's say so like a lot of different Specializations exist.

[Harshul Surana] 09:30:29
Which is owing to the. Going to what type of corporate or what type of ex it has been 3 trained on

[Peter Murray-Rust] 09:30:38
Right. Good, okay. So, Okay, we'll draw a section here in the discussion.

[Peter Murray-Rust] 09:30:50
So what what I think we're going to need to do is to give some verbal comments which can be used to section up the discussion.

[Peter Murray-Rust] 09:31:00
So this is end of partial machine learning AI section and now we'll move on to a completely different subject which is human sectioning of what we have already got.

[Peter Murray-Rust] 09:31:20
Now. We're going to do this in mark down and mark down is going to be the primary tool that we use to create something.

[Peter Murray-Rust] 09:31:32
So, Nitika, Parjat, Strabia, have you all, explored marked down?

[Sravya] 09:31:46
I, I used to, learn basic support the markdown. So I knew few.

[Sravya] 09:31:54
I mean, how to write the markdown. So I try it.

[Peter Murray-Rust] 09:31:58
Good. A parent chat?

[Parijat Bhadra] 09:32:01
I have exploded it, not quite, easy with it, but I have seen it.

[Peter Murray-Rust] 09:32:07
Nichiko?

[Nitika Baghel] 09:32:10
Oh, I also have had some experience with Mark down so I'm comfortable. Being yeah you think you're talking

[Peter Murray-Rust] 09:32:18
Good.

[Peter Murray-Rust] 09:32:22
And Anne Mole, you've just joined us, so welcome.

[Peter Murray-Rust] 09:32:29
We've just had a, a session on machine learning AI from Harcel who's done an absolutely brilliant job in Introducing us to this.

[Peter Murray-Rust] 09:32:41
And you should certainly go back and look at that recording if you missed some of it. So, Have you?

[Peter Murray-Rust] 09:32:49
Got experience with marked down.

[Anmol Negi] 09:32:54
Yeah, 1st of all, I've been here in the meeting since like last 30 30 min.

[Anmol Negi] 09:33:05
Yeah.

[Peter Murray-Rust] 09:33:06
Excellent. That's fine. Well, well done. Okay.

[Peter Murray-Rust] 09:33:13
So, we will create markdown in our transcripts here. So we'll come up with, Each session we've done.

[Peter Murray-Rust] 09:33:26
We will give an ID to and we will then put in major sections and gradually make them minor.

[Peter Murray-Rust] 09:33:40
And section subsections, there will be one or 2 places with tables. And, and We will do this as a communal activity.

[Peter Murray-Rust] 09:33:49
So.

[Peter Murray-Rust] 09:33:53
This is an experiment that we've, done. I don't know whether it's going to work out.

[Peter Murray-Rust] 09:33:59
I think it probably will. But the more that you can help as a community, the better. So, I,

[Peter Murray-Rust] 09:34:11
Let me. Share my screen.

[Peter Murray-Rust] 09:34:29
Okay, you can see my screen, now. And this is one particular analysis, and I've given it the, title of 2 0 2 4 0 6 13 which is the date Ranganathon, right?

[Peter Murray-Rust] 09:34:52
And that probably should be renamed. So giving identifiers is really valuable and in this case we will give them semantic identifiers.

[Peter Murray-Rust] 09:35:04
So I have put them in a repository here. Called semantic climate this is our communal, repository, isn't it?

[Peter Murray-Rust] 09:35:19
Renew. When there's

[Renu Kumari] 09:35:21
You know, this is, this is the different, I think. Maybe you can share because in the US system.

[Renu Kumari] 09:35:27
So it is yours.

[Peter Murray-Rust] 09:35:27
Well, I, it's on my machine, but I think it is, the,

[Renu Kumari] 09:35:32
Yeah, if it is yours then it is it will be the for all like, but if it is the assignments like Simon I create another one.

[Renu Kumari] 09:35:42
Plus the winter climate.

[Peter Murray-Rust] 09:35:42
Well, I think we will find that. Let's see what it is.

[Renu Kumari] 09:35:46
If you come in and if you can see that then

[Peter Murray-Rust] 09:35:53
So.

[Renu Kumari] 09:35:58
If it is gonna work space.

[Peter Murray-Rust] 09:35:59
Oh, I see. It's Not.

[Peter Murray-Rust] 09:36:07
It's such a complicated project. And we didn't know the structure at the beginning.

[Peter Murray-Rust] 09:36:14
That yes, I think I have Conf. So this is actually

[Peter Murray-Rust] 09:36:21
I think this is actually mine here. Now the semantic climate

[Renu Kumari] 09:36:25
Yes, yes.

[Peter Murray-Rust] 09:36:32
The whole semantic climate. Oh, ownership, let's have a look at this.

[Renu Kumari] 09:36:42
Yeah, this one.

[Peter Murray-Rust] 09:36:46
That's not me. We will. That's me, yes, but, I was trying to put them in,

[Renu Kumari] 09:36:48
No, if you.

[Peter Murray-Rust] 09:36:57
The one that I think

[Renu Kumari] 09:37:00
This is not the the one we are talking about.

[Peter Murray-Rust] 09:37:05
But this is.

[Renu Kumari] 09:37:07
Yeah, the one you're here. This is yours.

[Peter Murray-Rust] 09:37:13
But this is on github.com.

[Renu Kumari] 09:37:15
Yes, the name is different. It has it contains all the repository of glossary IPCC.

[Renu Kumari] 09:37:21
And.

[Peter Murray-Rust] 09:37:22
Yes. So I would. So I would suggest, so you've got, yeah, this is a, we've got discussions here on this repository we have been

[Peter Murray-Rust] 09:37:44
That's misnamed. I tried to rename it. This is where I have been creating, the discussion here, of our Yes.

[Renu Kumari] 09:37:58
Table of content.

[Peter Murray-Rust] 09:38:02
So this is not on my GitHub. This is on communal gitub, is that right?

[Peter Murray-Rust] 09:38:11
This is owned by the semantic climate project. Okay, so.

[Renu Kumari] 09:38:13
Yes, yes.

[Peter Murray-Rust] 09:38:29
This is I don't know whether we're going to be able to do this. Easily, communally.

[Peter Murray-Rust] 09:38:38
So you may see me struggling a little bit with this because I know what's going on here roughly.

[Peter Murray-Rust] 09:38:48
But we've had a number of.

[Renu Kumari] 09:38:51
Maybe 3 of us can do like, and you and me. While others.

[Peter Murray-Rust] 09:38:57
Well, what I want is everybody to see, what's happening unless there are clear tasks that we can give people at the moment.

[Renu Kumari] 09:39:08
Hmm, yes, yes.

[Peter Murray-Rust] 09:39:09
Do you think that there are clear tasks?

[Renu Kumari] 09:39:12
Clear task has not got it right now because

[Peter Murray-Rust] 09:39:16
No. So I think it may be a bit boring for people, but it will be a very good introduction on how you deal with.

[Peter Murray-Rust] 09:39:27
A very good introduction on how you deal with. A very good introduction on how you deal with, complex projects.

[Peter Murray-Rust] 09:39:30
And, if you've got ideas. Be very, me happy to suggest them, but also, expect that, you might find that they're not acceptable to the structure.

[Peter Murray-Rust] 09:39:44
We've already got at the moment. This is such a complex project that, you know, my brain is, struggling to manage all of this.

[Peter Murray-Rust] 09:39:58
So what I'm going to do on this one. Is, have you had any more, feedback from GitHub.

[Peter Murray-Rust] 09:40:08
Renew.

[Renu Kumari] 09:40:10
No Peter, nothing, no emails have reverted that.

[Peter Murray-Rust] 09:40:13
Right, has anybody else, contributed to GitHub?

[Renu Kumari] 09:40:19
Life.

[Peter Murray-Rust] 09:40:21
Well, what I mean is we've lost Harshaw, but we need to be putting this stuff up on GitHub and I wondered if GitHub had, blocked anybody else's account.

[Renu Kumari] 09:40:38
I mean, nobody is trying to take a risk. So that is the reason that nobody has tried it.

[Peter Murray-Rust] 09:40:41
I see, well,

[Renu Kumari] 09:40:42
Yeah, because I did it with the 2 account and the same test, same transcript.

[Renu Kumari] 09:40:49
The it has did this another account it was also banned. Okay, they already checked.

[Peter Murray-Rust] 09:40:52
Right, well.

[Peter Murray-Rust] 09:40:58
Right, so it's happened to you twice. Right.

[Renu Kumari] 09:41:01
Hmm.

[Renu Kumari] 09:41:04
I'm just waiting and otherwise I'll have to ask someone else to, generate with their email.

[Renu Kumari] 09:41:11
I didn't need to have account and give it to me so that I can use it for the website and for doing the semantics, It's called, the.

[Peter Murray-Rust] 09:41:22
Right, okay. What I'm going to do now is I'm going to assume that I can continue to contribute to discussions.

[Renu Kumari] 09:41:29
Yeah.

[Peter Murray-Rust] 09:41:30
So,

[Peter Murray-Rust] 09:41:33
I'm going to add a comment at the bottom here. Where I put a list of all of the.

[Peter Murray-Rust] 09:41:43
Transcripts that we've got.

[Peter Murray-Rust] 09:42:01
And

[Peter Murray-Rust] 09:42:11
We'll go over these transcripts and we will. Decide whether they're useful and we will label them.

[Peter Murray-Rust] 09:42:22
It may be mainly me talking. But it will be us doing the work together. Okay. So, it may be a bit boring, but, trust me, we will come up with something useful at the end.

[Peter Murray-Rust] 09:42:38
So. We'll go back in the slack. To find, all the transcripts, by the way, are, safe on my machine and their backed up and so on.

[Peter Murray-Rust] 09:42:54
And.

[Peter Murray-Rust] 09:42:57
If we can find somewhere to back them up, which is not GitHub. Then, we should do that, because that will make, them safe.

[Peter Murray-Rust] 09:43:08
But, at the moment we'll work on What we've got.

[Peter Murray-Rust] 09:43:18
And try and give it. Crown represent the overall. Thing here So there will be periods of silence when I think, okay.

[Peter Murray-Rust] 09:43:44
So we're going to go back to our slack. Slack doesn't.

[Peter Murray-Rust] 09:43:52
Last for a very long period.

[Peter Murray-Rust] 09:44:26
So.

[Peter Murray-Rust] 09:44:29
It may be that you can help by also looking at your copy. Of the slack here and decide.

[Peter Murray-Rust] 09:44:38
Where we want to go back to.

[Peter Murray-Rust] 09:44:44
That. It looks like it's not a good idea to host raw text into slack.

[Peter Murray-Rust] 09:45:00
Right, so we're getting to the.

[Peter Murray-Rust] 09:45:36
I don't know why it suddenly flipped back to March, but you can see by the way here that we can't get back beyond.

[Peter Murray-Rust] 09:45:44
That it's You have to pay huge amounts of money. You've probably got to pay.

[Peter Murray-Rust] 09:45:54
I don't know something like, $10,000 a month to slack. It is huge.

[Peter Murray-Rust] 09:46:28
I will go back and try and label all of these but the impression is that

[Peter Murray-Rust] 09:46:42
I don't know why. Why it's taken us back so far.

[Peter Murray-Rust] 09:46:52
It'll be late May somewhere.

[Peter Murray-Rust] 09:47:08
Right, I've tried to give, an idea here, so that's,

[Peter Murray-Rust] 09:47:56
We're still doing software at that stage.

[Peter Murray-Rust] 09:48:07
I would like better and more open systems. Can you see how useful this is? As a record of what we've done.

[Peter Murray-Rust] 09:48:15
It's not perfect. But, It's allows us to go back. 2 or 3 months.

[Peter Murray-Rust] 09:48:31
Yeah.

[Peter Murray-Rust] 09:49:30
Still doing Gatsby and stuff.

[Peter Murray-Rust] 09:50:07
Right. And. It's still.

[Peter Murray-Rust] 09:50:30
What we are now, this is. 2 weeks ago. So yes, so this is where we start looking for it.

[Peter Murray-Rust] 09:50:46
Hiashan. Can you see How exciting it is to have all our collaborators creating things.

[Peter Murray-Rust] 09:51:03
So we may very well come back and.

[Peter Murray-Rust] 09:51:12
Excession to very boring. Okay.

[Peter Murray-Rust] 09:51:19
I'm going to start. Noing these.

[Peter Murray-Rust] 09:51:31
No, we can go back. They're not going to disappear yet.

[Peter Murray-Rust] 09:51:37
Components of a dictionary might be valuable, so Let's go back Monday, June the 3.rd

[Peter Murray-Rust] 09:52:03
I've lost my

[Peter Murray-Rust] 09:52:08
Believe that on here and we go back to. The repository

[Peter Murray-Rust] 09:52:25
Actually, have bookmarks for this, but I don't.

[Renu Kumari] 09:52:44
Right side, right side, yes, L is in structure.

[Peter Murray-Rust] 09:52:47
Yes. That's right. Well done.

[Peter Murray-Rust] 09:53:17
What was it? It was said again. Okay.

[Peter Murray-Rust] 09:53:43
Then we got a.

[Peter Murray-Rust] 09:53:53
Right, so this one. Session one we have. Mainly.

[Peter Murray-Rust] 09:54:19
Right, so I have presented this. So I'm going to.

[Peter Murray-Rust] 09:54:51
That's June the 4.th Yeah.

[Peter Murray-Rust] 09:55:13
That's not what I wanted at all. Oh, my to me, yes it is, okay.

[Peter Murray-Rust] 09:55:34
Alright.

[Peter Murray-Rust] 09:55:47
This is making me feel much happier, right? You may all think that it's

[Peter Murray-Rust] 09:56:03
Boring.

[Peter Murray-Rust] 09:56:09
Right, so this.

[Peter Murray-Rust] 09:56:19
Between the 5th

[Peter Murray-Rust] 09:56:39
And you can see that what we need is a button where slack post it directly to this but it.

[Peter Murray-Rust] 09:56:51
You probably have to pay a lot of money for that.

[Peter Murray-Rust] 09:57:15
And we need to get the transcript somewhere. And When you when you got blocked Reno were you posting this to discussion or were you posting it to a Reported.

[Renu Kumari] 09:57:30
This discussion 12 discussion number 12 I have created the discussion number 12.

[Peter Murray-Rust] 09:57:36
Right. And, it did it when you posted something in, is that right?

[Renu Kumari] 09:57:43
I paste all the transmit, the big chunk, the long.

[Peter Murray-Rust] 09:57:46
Right, I think, I think probably. I think that that was what the problem was. Okay. So I don't think people should pass transcripts.

[Renu Kumari] 09:57:54
Hmm.

[Renu Kumari] 09:57:59
In discussion. Hmm.

[Peter Murray-Rust] 09:58:00
Large things to discussions because what they probably think is that you are trying to spam it. So yes, I, so we will create or use a repository where We put our transcripts in the GitHub repository and not What?

[Renu Kumari] 09:58:07
Yes.

[Renu Kumari] 09:58:18
As a test file. Yes, as it as it. Thanks. While we upload that file.

[Peter Murray-Rust] 09:58:21
Yes, as a exactly. And I think that Yeah. Good. Well, I'm sorry it's happened to you.

[Peter Murray-Rust] 09:58:31
And, yeah, that makes sense. that. Posting these transcripts is not a good idea.

[Peter Murray-Rust] 09:58:40
On discussion things okay so that's June here. The 5.th

[Peter Murray-Rust] 09:59:14
Right, so we had session one on one day and session 2 on. Another day. And

[Peter Murray-Rust] 09:59:28
And we will take that.

[Peter Murray-Rust] 09:59:53
I'm going to go on until I've got this summarized and then we will have a a break for tea.

[Peter Murray-Rust] 10:00:02
Okay.

[Peter Murray-Rust] 10:00:06
So that captures everything.

[Peter Murray-Rust] 10:00:12
Yeah, I think that's captured that.

[Peter Murray-Rust] 10:00:34
So we're now on Friday, is that right?

[Peter Murray-Rust] 10:00:40
No, it still says Thursday.

[Peter Murray-Rust] 10:02:05
Now the 11.th

[Peter Murray-Rust] 10:02:12
This is a session on Monday.

[Peter Murray-Rust] 10:02:18
That was. The. Mainly, debug, mainly software.

[Renu Kumari] 10:02:28
And Peter, we have a holiday on Monday.

[Renu Kumari] 10:02:33
We do some festival.

[Peter Murray-Rust] 10:02:35
Okay, that's thanks very much for letting us know.

[Renu Kumari] 10:02:40
If anyone is interested, you can continue with them. Meeting. I have the holder so I cannot come to the lab but others can join if they are happy to join on line.

[Peter Murray-Rust] 10:02:43
Yes. Yeah.

[Peter Murray-Rust] 10:02:48
No.

[Peter Murray-Rust] 10:02:53
That means that choose i've got to try and get most of this together for Tuesday right

[Renu Kumari] 10:03:00
Hmm, yes.

[Peter Murray-Rust] 10:03:01
And Tuesday we should. Let's work out what the days are.

[Peter Murray-Rust] 10:03:10
She says the 18, th right? Till 20, th right, okay. But I think I can't, I, Do you have any idea whether this is a hard deadline?

[Renu Kumari] 10:03:12
18.th We have the deadline till 20.th

[Renu Kumari] 10:03:19
You know.

[Peter Murray-Rust] 10:03:27
In other words, they're not going to cut off software.

[Renu Kumari] 10:03:29
You already expect I think the I don't know about that but It is already expanded after 31st May to June 20.th

[Peter Murray-Rust] 10:03:32
They've extended it, but I think

[Peter Murray-Rust] 10:03:38
I know. I will tell them that we're in the process of submitting it. And So.

[Renu Kumari] 10:03:39
After that I didn't.

[Renu Kumari] 10:03:46
Sending the reminder to others. Cool. I'm sending the reminder to others who are supposed to submit.

[Renu Kumari] 10:03:55
Hmm.

[Peter Murray-Rust] 10:03:55
Oh, you are. Oh, well done. Okay. Right, well, we'll, we'll get something in.

[Renu Kumari] 10:03:59
Okay. Okay, you can continue.

[Renu Kumari] 10:04:05
Hmm.

[Peter Murray-Rust] 10:04:09
So this is top level narrative, June the 11.th

[Peter Murray-Rust] 10:06:22
And then there was that's on the. What date is that?

[Peter Murray-Rust] 10:06:42
That's on the 11.th

[Peter Murray-Rust] 10:07:17
This is probably also true of Slack that we shouldn't paste huge things into Slack.

[Renu Kumari] 10:07:30
But it was not, in the slide, it was a text file only. It was the text file is uploaded in the slack.

[Peter Murray-Rust] 10:07:38
Yes, this is probably okay, actually. They They seem to allow it.

[Renu Kumari] 10:07:40
This is the view viewing, yes.

[Renu Kumari] 10:07:44
Hmm.

[Peter Murray-Rust] 10:08:05
So wait a minute.

[Peter Murray-Rust] 10:08:10
Wednesday.

[Peter Murray-Rust] 10:08:15
Maybe.

[Peter Murray-Rust] 10:08:23
Good I did I post? There's nothing in there, right? I think I I had to rush off in Wednesday.

[Peter Murray-Rust] 10:08:31
Do you remember that?

[Peter Murray-Rust] 10:08:34
I had a guest. Right. I know. Yes, and I think I record.

[Renu Kumari] 10:08:35
Yes, you're going to the, I think. Okay. 15 min session was there 15 and a half an hour.

[Peter Murray-Rust] 10:08:40
Okay, so that's a very

[Peter Murray-Rust] 10:08:44
Yeah, yes, okay. So we need to post. Something into

[Renu Kumari] 10:08:45
Hmm.

[Peter Murray-Rust] 10:08:55
I'm not sure whether it's possible to

[Peter Murray-Rust] 10:09:00
Edit this.

[Harshul Surana] 10:09:06
I need to leave for lunch.

[Peter Murray-Rust] 10:09:08
Off you go, off you do. You're all doing brilliantly. When I finish this, I think we'll finish for the day.

[Harshul Surana] 10:09:14
She on Tuesday.

[Peter Murray-Rust] 10:09:19
I think I just need to go down and. So are you happy for us to work for another?

[Renu Kumari] 10:09:25
Okay. Yes, yes, I am here. Yeah, you can go off and not also.

[Peter Murray-Rust] 10:09:26
10 min from now get this. Sorted, okay. So I'm Yes.

[Peter Murray-Rust] 10:09:38
I'm going to edit this.

[Peter Murray-Rust] 10:10:13
That's 12. Okay, that's fine.

[Peter Murray-Rust] 10:10:33
Right, so that's Wednesday.

[Peter Murray-Rust] 10:10:36
And this, manuscript production will be important.

[Peter Murray-Rust] 10:12:16
I'm not going to edit it. That's wrong.

[Peter Murray-Rust] 10:12:22
Sorry, I'm putting it into slack.

[Peter Murray-Rust] 10:12:29
It's still pushing it into Slack. So that's.

[Peter Murray-Rust] 10:13:02
And. I will go through and.

[Peter Murray-Rust] 10:13:08
And give all of these things. Name so that we can then put it put them in the right order.

[Peter Murray-Rust] 10:13:33
And I'm going to write a top level article from this. Covering everything we want. Which will be converted into the PDF.

[Peter Murray-Rust] 10:13:44
I don't think we can use automatic tools at this stage. This will just be me going through everything here.

[Peter Murray-Rust] 10:13:51
I'm writing some narrative in this. The

[Renu Kumari] 10:13:54
Yes, so we will be sending them in the gold document. So maybe they are going to convert it into the.

[Peter Murray-Rust] 10:13:59
Oh yeah, a word. We'll put it in word, but this will be me sticking it together with all of us looking to make sure that.

[Renu Kumari] 10:14:03
Hmm. Okay.

[Peter Murray-Rust] 10:14:11
It's,

[Peter Murray-Rust] 10:14:14
It's correct. Has it been?

[Renu Kumari] 10:14:18
Okay.

[Peter Murray-Rust] 10:14:22
So that I think

[Peter Murray-Rust] 10:14:37
I'm gonna save that. I don't know what's happened to the recordings, but

[Peter Murray-Rust] 10:14:44
I don't think they got uploaded.

[Peter Murray-Rust] 10:14:50
And do it again. Huh. Oh, wait a minute.

[Peter Murray-Rust] 10:14:56
Wait a minute. I've got to save it. It's at the bottom of it.

[Renu Kumari] 10:14:57
Okay.

[Renu Kumari] 10:15:00
Click on the green button.

[Peter Murray-Rust] 10:15:03
And.

[Peter Murray-Rust] 10:15:09
Where maybe they.

[Peter Murray-Rust] 10:15:13
Maybe that. It appears to be in the end. Right, okay, so this has got to be edited.

[Renu Kumari] 10:15:14
Put it in the end.

[Renu Kumari] 10:15:18
Yeah. Hmm.

[Peter Murray-Rust] 10:15:22
So this is

[Renu Kumari] 10:15:26
Okay. Goodness, Jay.

[Peter Murray-Rust] 10:15:44
Recording. And now I haven't done a summary of this. So.

[Peter Murray-Rust] 10:15:53
Cause if we go back to Wednesday.

[Peter Murray-Rust] 10:16:09
I'm not sure where this is from.

[Renu Kumari] 10:16:14
Just click on this small button, it will disappear. The transcript. Yes.

[Peter Murray-Rust] 10:16:22
Oh, okay, that's absolutely fine.

[Renu Kumari] 10:16:32
Yeah, he

[Peter Murray-Rust] 10:16:33
It looks like A this manuscript production was what we were going to do. So that's the best that we can do for.

[Renu Kumari] 10:16:38
Hmm.

[Peter Murray-Rust] 10:16:49
Right, have we got a Thursday recording?

[Renu Kumari] 10:16:52
Hmm. This recording that was converted.

[Peter Murray-Rust] 10:16:58
Yes, what what did we do yesterday?

[Renu Kumari] 10:17:01
Yes, today we did.

[Renu Kumari] 10:17:07
Hmm

[Peter Murray-Rust] 10:17:17
I think yesterday we talked about Ranganison, didn't we?

[Renu Kumari] 10:17:24
Yes, we have open access and open source.

[Peter Murray-Rust] 10:17:29
So if I go back to.

[Renu Kumari] 10:17:30
Open source and open access. Hmm.

[Renu Kumari] 10:17:34
Okay.

[Peter Murray-Rust] 10:17:34
Yes, that's right. And we're gonna the whole thing about Ranganathan and then at the end Yes, and the second one.

[Renu Kumari] 10:17:39
In the 1st session, yes.

[Renu Kumari] 10:17:44
We have a GitHub ban.

[Peter Murray-Rust] 10:17:44
We were all running out of energy was how we, how we create the paper, right? Okay, so that's good.

[Renu Kumari] 10:17:50
And at all about the beta ban also.

[Peter Murray-Rust] 10:17:53
Absolutely.

[Peter Murray-Rust] 10:18:06
And

[Peter Murray-Rust] 10:18:12
So now. We'll edit.

[Peter Murray-Rust] 10:18:22
Salescheck.

[Peter Murray-Rust] 10:18:30
Yes, these are these. So those are well done. So I'm going to put.

[Peter Murray-Rust] 10:18:38
That's in our.

[Peter Murray-Rust] 10:19:03
And what do we have in session 2 and

[Peter Murray-Rust] 10:19:08
Oh, we create our obstacle, yes.

[Peter Murray-Rust] 10:19:40
Right, and now today

[Peter Murray-Rust] 10:19:47
We'll put this one in. So.

[Peter Murray-Rust] 10:21:26
That's today, 14. We will go back here. And what I'm going to do now is I'm going to Paste this in today.

[Peter Murray-Rust] 10:21:39
And then say, goodbye. Now it's possible. I might want some help over no weekend, Friday and Saturday. I'm not planning it.

[Peter Murray-Rust] 10:21:53
I'm trying to do all this myself, but if I hit a real crisis, I might come back to you.

[Peter Murray-Rust] 10:21:57
Does that make sense, everyone?

[Renu Kumari] 10:21:59
Yes.

[Peter Murray-Rust] 10:22:00
Yeah. And similarly on Monday. So, so. You have all been very helpful even if you haven't said a word.

[Renu Kumari] 10:22:02
Yes. Hmm.

[Peter Murray-Rust] 10:22:13
Because I can, I cannot do this alone. Do you know what I mean? I mean, I've gone through this.

[Renu Kumari] 10:22:18
Yes, we are.

[Peter Murray-Rust] 10:22:20
And you know, hearing renewed. Keep up the conversation. I can see your face and your interest and you smile.

[Renu Kumari] 10:22:27
Hmm.

[Renu Kumari] 10:22:34
Yeah.

[Peter Murray-Rust] 10:22:36
There you go. Right. And so on. That's really valuable.

[Renu Kumari] 10:22:38
Yeah.

[Peter Murray-Rust] 10:22:43
Okay.

[Peter Murray-Rust] 10:22:46
So my plan now is the following. To. Take all those transcripts. And structure them, right?

[Peter Murray-Rust] 10:22:59
I will listen to them. I will find out I will have 2 screens I hope. Where I'm listening to the transcript.

[Peter Murray-Rust] 10:23:07
And I will click on it when it comes to the right place and I will put in, the structuring so that we know where it is.

[Peter Murray-Rust] 10:23:15
So that is then a structured recording. Using marked down as a structure and that I think, could be extremely valuable.

[Peter Murray-Rust] 10:23:26
And then I will try and write the overall, top level, word document that we will send to.

[Peter Murray-Rust] 10:23:36
Whatever. Now we've got to do some diagrams.

[Peter Murray-Rust] 10:23:43
I would like you all actually to sync, start thinking now and perhaps to spend the rest of today if there is any rest of today.

[Peter Murray-Rust] 10:23:54
There isn't much. On what diagrams actually go into this. My brain isn't up to doing it today, so I will probably start looking at that tomorrow.

[Renu Kumari] 10:24:08
Okay.

[Peter Murray-Rust] 10:24:12
There you go. So, Before we finish any final comments.

[Renu Kumari] 10:24:22
Yeah, for the diagram we can, Think about the process, the, the tools are working or the whole, like, we are using the PDF and then converting into in the, the whole process of the working of the report climate report.

[Peter Murray-Rust] 10:24:34
Absolutely, so

[Peter Murray-Rust] 10:24:39
Yes. Yes, and I will, we will make them schematic diagrams.

[Renu Kumari] 10:24:47
Hmm.

[Peter Murray-Rust] 10:24:49
And if they're schematic, they can be done in,

[Peter Murray-Rust] 10:24:53
Graph fish. Yep. Right. So that will be useful.

[Renu Kumari] 10:24:54
Yes Hmm. Okay. Awesome.

[Peter Murray-Rust] 10:25:00
I may be that I draw them out and. Photograph them and Stick them in and then we're doing them in.

[Peter Murray-Rust] 10:25:09
I think that would be valuable.

[Renu Kumari] 10:25:10
Because it's the model of the story the whole thing is there maybe we can also do the one on the semantic publishing and open access.

[Peter Murray-Rust] 10:25:14
Yes.

[Renu Kumari] 10:25:20
D. Okay. Hmm. Okay.

[Peter Murray-Rust] 10:25:24
Indeed. Indeed, absolutely.

[Peter Murray-Rust] 10:25:29
Right. The main thing is to get the top level Word document in and then we can continue working on this and we will make a big point of that in the final document.

[Peter Murray-Rust] 10:25:40
Okay.

[Renu Kumari] 10:25:43
Yes, yes.

[Peter Murray-Rust] 10:25:46
Right. Wave to everybody. I think I will put the transcripts. I think I'll put the transcripts, up onto the, a semantic climate.

[Peter Murray-Rust] 10:26:03
Repository because I think they're more useful than and I will probably give them formal numbers so that we can arrange them.

[Peter Murray-Rust] 10:26:12
Makes sense to everybody.

[Renu Kumari] 10:26:16
Okay.

[Peter Murray-Rust] 10:26:17
Okay, so we now go through the close down ritual, which is.

[Renu Kumari] 10:26:21
Okay. Safe transfer.

[Peter Murray-Rust] 10:26:24
We start. Yes, If I can find out where it is.

[Renu Kumari] 10:26:35
Click on the Zoom Meeting and this you the full new transcript option on the caption button. It will appear.

[Peter Murray-Rust] 10:26:45
It will appear, okay. That's not what we want.

[Renu Kumari] 10:26:46
Yes.

[Peter Murray-Rust] 10:26:57
You are correct. Captions Beautiful transcript. Save transcript, right.

[Renu Kumari] 10:27:06
Yeah.

[Peter Murray-Rust] 10:27:08
Transcript site and we're going to save the recording.

[Renu Kumari] 10:27:13
Stop the recording.

[Peter Murray-Rust] 10:27:15
Stop that we're going to stop the recording. Also on Zoom.

[Renu Kumari] 10:27:27
Okay.

[Peter Murray-Rust] 10:27:28
Trouble is it puts up Windows in different places on my machine. And I

[Peter Murray-Rust] 10:27:39
Confuses me. Yes, here.

[Renu Kumari] 10:27:47
Okay.

[Peter Murray-Rust] 10:27:47
Stop the record. Recording stopped, then we stop the share.

[Peter Murray-Rust] 10:27:53
And then we wave goodbye. And then. We're gonna have some key, aren't we, Amy?

[Renu Kumari] 10:27:56
Yes. And Nice.

[Peter Murray-Rust] 10:28:01
Right. Okay, you're all wonderful. By the way, Rena, by the way, everybody who's involved in this will be authors of this document.

[Peter Murray-Rust] 10:28:12
If they're regular visitors here, then they are authors because we are authoring this document together.

[Renu Kumari] 10:28:20
Regular means what? Are these people will be going to author? Tegan, there's the whole whose word and in the middle of the

[Peter Murray-Rust] 10:28:25
My plan, my plan is that we have 20 or 30 authors on this right because it will it will, reference everybody who's made a significant contribution.

[Renu Kumari] 10:28:32
Yes.

[Peter Murray-Rust] 10:28:43
To what we're doing at the moment. So, I mean, somebody's just dropped in for one session is not a regular offer, but you know, You know, Yes, yes.

[Renu Kumari] 10:28:46
Okay.

[Renu Kumari] 10:28:52
No, no, so. I'll mention all the list to you. I share with them.

[Peter Murray-Rust] 10:29:00
So I would say that if somebody has been on. 3 or 4 authoring sections, in the last week or 2, then they are an author, right?

[Peter Murray-Rust] 10:29:12
But if somebody's just dropped in for half an hour, they're not an author.

[Renu Kumari] 10:29:13
Okay.

[Renu Kumari] 10:29:16
No, no. Okay

[Peter Murray-Rust] 10:29:17
But we We thank everybody

[Renu Kumari] 10:29:21
Yeah

