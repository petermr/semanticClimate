
# summarization (Harshul)
09:06:46 No bugs, okay. Right. Okay. Marshall, can you, I'm going to hand the screen over to you.
09:06:57 Can you talk us through what you've done with hugging face and, summarization.
09:07:06 Okay.
09:07:10 Is that okay?
09:07:12 Yes, Peter.
09:07:13 Good, okay. And don't you know, you're, you're among friends, so don't worry if anything, doesn't work out 1st time.
09:07:24 Sure.
09:07:28 So you're telling a story, give us at the beginning, it's a good idea with stories that you tell people what you're going to tell them, right?
09:07:39 So a brief summary, 2 3 sentences, this is what I'm going to show you so that we know where we are.
09:07:47 Okay.
09:07:47 And then you give the message and at the end you then summarize by saying this is what we looked at.
09:07:54 And it's summed up in the model motto.
09:07:59 Tell them what you're going to tell them. Tell him, tell him what you told them, right?
09:08:07 Okay.
09:08:05 Okay. And it's, so tell us what, what we're going to see.
09:08:12 In overview.
09:08:19 Huh.
09:08:24 Well, no, no.
09:08:15 So it would be from the beginnings. Yes, go after the transcript after the transcript. You can read it from the zoom and yeah.
09:08:34 Hmm.
09:08:27 So it's Hong Kong is going to say something like, Hi. Explored summarization of our transcripts using hugging face summarize or whatever it is right so that's what you're going to tell us right and and then you might put in a thing to say we're going to see the installation of the transformer then it's customization.
09:08:58 Then it's use on an example. Okay. So that's a sort of, introduction.
09:09:10 Good.
09:09:08 Okay. Does that make sense? Right. Yes.
09:09:11 Okay. Kind of tutorial. Yeah.
09:09:20 Right, so the task at hand was, can we come up with a good summarization for the long transcript text that we have and for that I explored.
09:09:29 PM?
09:09:32 2 different approaches that I'm gonna later explain that users having faced transformers which are again open source.
09:09:45 Yeah.
09:09:40 We And, right, I'll jump into the 1st one. Which was done using a transformer called Bart.
09:09:49 And before jumping into that, I can give an overview of what the 2. Broad types of summarization are that I have each tried.
09:09:58 The 1st one is called extractive summarization. Where the idea is that you compress the long text that you have.
09:10:08 Without changing the wording. So let's say. You have a thousand word document you want to summarize it.
09:10:16 No, the way you will do it is not by paraphrasing or by you know using your own deduction or reasoning to paraphrase to you know get to the crux of the document.
09:10:29 How it is done is that it takes the sentences present in the document largely and it you know compresses that So that is the 1st and that is called extractive summarization.
09:10:44 Conversely the second type of summarization is called abstractor summarization where it's just the opposite.
09:10:50 Where, rather than compressing the text itself. The idea is that the model generates text.
09:11:01 New text that is supposed to be a good summarization for the text. So, we look at both of them.
09:11:10 This one is for abstractive summarization. The 1st part is obviously installing all the necessary packages.
09:11:20 And my screen is visible, right?
09:11:25 Great.
09:11:22 Brilliant. That was an excellent introduction, really good.
09:11:30 Thank you. And so this is the bad model that I mentioned which performs abstractive summarization. So here the challenge or the Oh, the particular challenge of us is that our document is long, right?
09:11:45 And these transformers at 1 point they can only take 500 words as an input. So one part of the pre-processing is to divide the long document into 500.
09:11:59 Oh, word long, chunks or passages. And the workflow is that the model summarizes these 500 word long passages.
09:12:15 And coll that and the other the another process on top of that is that it takes those summaries on top of that is that it takes those summaries, concatenates them and generates a summary on top of that.
09:12:30 So like there are 2. Different types of outputs.
09:12:39 I'm absolutely.
09:12:36 So I can give an example, I can show how it looks like. So if the If it's visible here, so it says that, it is divided by text into 56 passages.
09:12:48 56, 500 word long passages. And
09:12:51 Quick question, when you say the text, is this a 500 word text or is it the whole lot?
09:12:59 The text refers to the transcript and the chunks of the passages refer to the 500 word longer.
09:13:05 It's subdivisions that we're doing.
09:13:08 Right and and so there are altogether then 2,800 words 56 by 2, by 500.
09:13:21 28,000.
09:13:21 56. Great, 56 into 500. Approximately.
09:13:26 Yeah, so that's that's 28,000.
09:13:32 Right.
09:13:33 Right, okay, and is that all of our transcripts?
09:13:39 No, this is just one of the transcript. The name is, I can look that up.
09:13:50 Okay, this is very, very good, right?
09:13:54 It's called meeting saved closed caption. So like I just took one of them for experimenting.
09:13:58 Yes, we need to now, the next thing we have to do immediately afterwards is give these decent labels, but that's fine.
09:14:08 Right. So as you can see like for each of the chunks it generates a summary.
09:14:15 So for example, We have separate channels and slack for different types of discussion. This is the summary for this particular.
09:14:24 Chunk the 500 word long chunk and, I, another step, what it also does is that it takes all of the summaries generated, concatenates them and generates a summary.
09:14:42 Yes.
09:14:40 Of that. So a summary of summaries. And that is.
09:14:48 That is shown here. But that was not very good. So like that was that didn't come out to be very good.
09:15:02 Yep.
09:14:56 So final somebody which other somebody or somebody uses. Summarizes uses tools from zoom and slack. We record videos which have an audio stream in them.
09:15:06 So it's not very useful. Like from experiments
09:15:10 How long is, these summaries, how many words are they, they take 500 words are they, they take 500 words and condense them into what lengths.
09:15:20 The maximum length is 500 by 6, which like which is a hyper parameter I said.
09:15:26 So, 500 by 6 would be approximately 125 1 30 words. That is the maximum length that I have said.
09:15:35 So you're condensing. 500 words into 1 30 words.
09:15:40 Yes, a maximum of 1 30.
09:15:42 Right. Yes. Excellent.
09:15:50 And then you
09:15:50 Do you vote flow for the? Sorry.
09:16:08 I'm writing it to the text file. Yeah.
09:15:53 No, and then you're taking all of those. 56, chunks of 1 30 words and, turning them into a single And that but it's making a single final summary.
09:16:14 So how long is the single final summary?
09:16:16 The single final summary was in 2 grade. It was just one line.
09:16:21 Yeah, that's no use to it. Yes. Yes.
09:16:27 That's right.
09:16:22 Summarizes using tool from zoom in slack per record videos which have an audio stream we publish all this material record then the transcript onto slide this last for a period over 2 months.
09:16:34 So I don't know what went wrong there maybe. Something went wrong but yeah like this is the current how it looks.
09:16:39 Right. So. One of the things is that.
09:16:45 Whenever you do something like this 1st time, It usually goes wrong and you repeat exactly what you did or you think you did.
09:16:57 And then it starts getting better. So 1st time through, always with things like this you can expect.
09:17:05 Okay.
09:17:05 You know to get something that isn't right.
09:17:11 And the workflow for a second one is exactly the same. It is just that we use it different transformer to shift from abstractive to extractive.
09:17:22 So, if Peter, you remember, yes, and you were saying that the summary. Sounds like a 3rd person overview.
09:17:30 Yes.
09:17:30 So that is that is a function of that the that is a component of it being summarized using abstractive summarization because like you are generating new lines, paraphrasing, the original content.
09:17:48 So it looks like a 3rd person has read it and you know given a summary in their own words.
09:17:52 Right. I wondered whether, so when you gave it to chat GPT, presumably you gave it some sort of prompt.
09:18:01 Yes.
09:18:02 And I wondered whether the prompt had, influenced that. In other words, I you said please summarize this and Chatchi PT took summarized to mean write a review of it rather than you know, abstract the meaning in the same style.
09:18:26 Yes.
09:18:30 Yeah.
09:18:23 Probably. I used a very simple problem that said like your Like, a very simple problem. Where they are like changing the prompt influences.
09:18:34 The output I could, you know, specify, perform extracted summarization and then it probably would stick to performing extractor summarization.
09:18:45 Okay, that's tremendous. Now, can we have, Svia, Reno and, and ask you questions.
09:18:57 Do you understand this? What's happened here?
09:19:07 Yes, Peter, I got this some some not completely but that.


09:19:14 Shafia, what about you?
09:19:17 Yeah, I got it, but. Same, I mean, little confused.
09:19:23 Right, and part yet?
09:19:27 Alright, I think I understand how like it's generating.
09:19:33 Right, you don't have to understand the. Deep mechanics of it, and what type of network it is, and so on.
09:19:44 But you have to understand. What the input is, what the expected output is. And then we've got to work out whether it's worth while.
09:19:58 So. You think it condenses from 500 to a hundred 30 okay Did you feel those?
09:20:10 130 word summaries. And, gel were useful.
09:20:20 So I tried, 2 different versions, one by specifying the maximum length as it is, 1 50 words and the other without any without a hard encoding rate.
09:20:32 But in that case, like it turned out to be very long the document. So like I didn't share it because I felt the other one which uses 150 as the maximum words.
09:20:44 Give better result according to like my skimming of the output.
09:20:51 Right, okay. That's very, very useful. And indeed, we'll need to think about it.
09:21:01 You're showing us code here. Is that taken from, tutorials, so that, or have you had to write that?
09:21:14 So for obstructive summarization, I got the code from a blog that he had put out of video also explaining what he's doing and like there are links above.
09:21:25 And for the extractive component, I just had to change the what the model is doing. So I did that myself.
09:21:33 Right. Okay. We, we will have to find out, how useful this is.
09:21:45 And I think Probably. You're all.
09:21:50 All of you should have a look and see whether these. 130 word summaries are useful.
09:21:59 And, when that's going to help. My feeling is that given this, the way that you've had to divide it into 500
09:22:13 What chunks is actually better for us to chunk it because it has been the talk has been given on the basis that it's fairly well structured and I think our task is going to go through and turn it into chunks and then we might.
09:22:32 Repeat on that because your chunks are may overlap 2 concepts or it may not be enough for one concept or something of that sort.
09:22:44 Does that make sense?
09:22:46 Yep.
09:22:45 Okay. And another thing I tried which like did not, like I could not get the results until now is that.
09:22:53 Initially I tried it using Ch GPT, right? And. So then the better step was to try an open source, language model.
09:23:03 So I'm I'm working on that code to generate a summary using. An open source language model.
09:23:13 That could give a better result Lexi because it has a Hi, it has a bigger amount of words that it can process at a single time.
09:23:25 That's
09:23:24 So like for transformers it is 500 so for that it is 1,000 or in some cases even more.
09:23:33 Excellent. And, what are the resource requirements for this?
09:23:40 That one requires GPU resources. So like yesterday I was trying it out on Kaggle like Kaggle offers certain minimum, GPU.
09:23:52 Clouds. So I was trying it on that.
09:23:56 And, do they offer that free or do you have to pay?
09:24:01 That one is free.
09:24:03 Good. I should say, to everybody that we don't want any of you to, start paying any money for anything.
09:24:16 I accept for your connection charges. We can't do anything about that. NIPGR has, you know, installed a powerful, GPU machine.
09:24:29 I don't know what the load Renew, do you have any feeling for how that machine is used?
09:24:37 No, no, Peter. We have no information. It is there. Good day.
09:24:41 Yes. So that's a possibility. And that's is almost certainly, up to, to manage.
09:24:55 He's done very, very well in, you know, getting this. purchased and installed.
09:25:04 You know, and what you're doing, what we're doing, so this is a team effort.
09:25:09 Is maybe very very useful for some of the core business of the institute you can imagine For example, getting a, report from another government institute on, let's say, the, Management of crops or something like that and asking these tools to summarize it.
09:25:39 You know, and Possibly summarize it with, relevance to an IPGRs, core.
09:25:47 Disciplines. Does that make sense?
09:25:53 Yes, it does. Yeah.
09:25:54 Because I think, you know, the traditional reports and the scientific literature are vastly underused and and it may well be possible, say, if you've got an institute which produces, I don't know, let's say.
09:26:14 A thousand page a thousand pages of report a year something like that you can see saying what does this institute and you know these will be publicly available you know these will be public available you know can you summarize this institute and you know these will be public available.
09:26:30 You know, these will be public available. You know, can you summarize this and can you find out, you know, can you summarize this and can you find out, whether and it is particularly involved with genomics or with invasive species or whatever it might be.
09:26:42 So. This is pioneering work, Castle and I think that's.
09:26:49 Very exciting indeed, so.
09:26:53 Right, so the message from this, now, that we need to section our our transcripts, along the lines of what we have, already done.
09:27:12 But we need to actually put that sectioning in the transcript. And that would make it easier to summarize.
09:27:21 How long does it, Take to run a hospital and Do you have a limited amount of resources?
09:27:30 On
09:27:35 Table has a limited resources for the free tier of GPUs that it provides. And then at the later iterations of the model it was crashing.
09:27:46 But this one, the transfer based one, there I'm perfectly fine. I ran it on Google.
09:27:52 Right, okay. So it's offered in Google Calab, is it?
09:28:01 Google. I've also, it also offers 3 GPUs up to up to a limit but in my experience Cagle offers a much more It offers more compute at for the free tier list.
09:28:18 Right. Okay. One small thing. Can you explain the difference between Bart and Bert's because they're, when we speak about them, it's easy to confuse them.
09:28:34 Great.
09:28:42 At a broad overview level. BART is a encoded with I love I might I don't want to get this wrong
09:28:59 So there is a difference in the architecture of the models that enables it to perform certain tasks, right?
09:29:06 So bird for example. Usually it is used for let's say classification. Or you know outputting something that is a label or like a short output.
09:29:16 Right Yep.
09:29:18 Compare that to but which is you know pre trained to generate text so like for that for that purpose it is used for abstracted summarization where you know it can generate text.
09:29:29 And a much more robust way compared to Bert where like internally it is just compressing the texts and then not particularly generating it.
09:29:40 That's very useful. Okay. I believe, that, is used as a basis of a number of the, Texts tools that we've used already.
09:29:55 In Docker analysis and so on that I think there and and there are quite a lot of But specialities where it's something, right?
09:30:08 And the
09:30:06 Good. So for example, biotech is pre-trained on you know abstracts of biomedical literature.
09:30:15 And a different bird, let's say, is. Pre-trained on documents that are particularly financial let's say so like a lot of different Specializations exist.
09:30:29 Which is owing to the. Going to what type of corporate or what type of ex it has been 3 trained on
09:30:38 Right. Good, okay. So, Okay, we'll draw a section here in the discussion.
09:30:50 So what what I think we're going to need to do is to give some verbal comments which can be used to section up the discussion.
09:31:00 So this is end of partial machine learning AI section and now we'll move on to a completely different subject which is human sectioning of what we have already got.
09:31:20 Now. We're going to do this in mark down and mark down is going to be the primary tool that we use to create something.
09:31:32 So, Nitika, Parjat, Strabia, have you all, explored marked down?
09:31:46 I, I used to, learn basic support the markdown. So I knew few.
09:31:54 I mean, how to write the markdown. So I try it.
09:31:58 Good. A parent chat?
09:32:01 I have exploded it, not quite, easy with it, but I have seen it.
09:32:07 Nichiko?
09:32:18 Good.
09:32:10 Oh, I also have had some experience with Mark down so I'm comfortable. Being yeah you think you're talking
09:32:22 And Anne Mole, you've just joined us, so welcome.
09:32:29 We've just had a, a session on machine learning AI from Harcel who's done an absolutely brilliant job in Introducing us to this.
09:32:41 And you should certainly go back and look at that recording if you missed some of it. So, Have you?
09:32:49 Got experience with marked down.
09:32:54 Yeah, 1st of all, I've been here in the meeting since like last 30 30 min.
09:33:05 Yeah.
09:33:06 Excellent. That's fine. Well, well done. Okay.
09:33:13 So, we will create markdown in our transcripts here. So we'll come up with, Each session we've done.
09:33:26 We will give an ID to and we will then put in major sections and gradually make them minor.
09:33:40 And section subsections, there will be one or 2 places with tables. And, and We will do this as a communal activity.
09:33:49 So.
09:33:53 This is an experiment that we've, done. I don't know whether it's going to work out.
09:33:59 I think it probably will. But the more that you can help as a community, the better. So, I,
09:34:11 Let me. Share my screen.
09:34:29 Okay, you can see my screen, now. And this is one particular analysis, and I've given it the, title of 2 0 2 4 0 6 13 which is the date Ranganathon, right?
09:34:52 And that probably should be renamed. So giving identifiers is really valuable and in this case we will give them semantic identifiers.
09:35:04 So I have put them in a repository here. Called semantic climate this is our communal, repository, isn't it?
09:35:19 Renew. When there's
09:35:21 You know, this is, this is the different, I think. Maybe you can share because in the US system.
09:35:27 So it is yours.
09:35:27 Well, I, it's on my machine, but I think it is, the,
09:35:32 Yeah, if it is yours then it is it will be the for all like, but if it is the assignments like Simon I create another one.
09:35:42 Plus the winter climate.
09:35:42 Well, I think we will find that. Let's see what it is.
09:35:46 If you come in and if you can see that then
09:35:53 So.
09:35:58 If it is gonna work space.
09:35:59 Oh, I see. It's Not.
09:36:07 It's such a complicated project. And we didn't know the structure at the beginning.
09:36:14 That yes, I think I have Conf. So this is actually
09:36:25 Yes, yes.
09:36:21 I think this is actually mine here. Now the semantic climate
09:36:32 The whole semantic climate. Oh, ownership, let's have a look at this.
09:36:42 Yeah, this one.
09:36:48 No, if you.
09:36:46 That's not me. We will. That's me, yes, but, I was trying to put them in,
09:36:57 The one that I think
09:37:00 This is not the the one we are talking about.
09:37:05 But this is.
09:37:07 Yeah, the one you're here. This is yours.
09:37:13 But this is on github.com.
09:37:15 Yes, the name is different. It has it contains all the repository of glossary IPCC.
09:37:21 And.
09:37:22 Yes. So I would. So I would suggest, so you've got, yeah, this is a, we've got discussions here on this repository we have been
09:37:44 That's misnamed. I tried to rename it. This is where I have been creating, the discussion here, of our Yes.
09:37:58 Table of content.
09:38:02 So this is not on my GitHub. This is on communal gitub, is that right?
09:38:11 This is owned by the semantic climate project. Okay, so.
09:38:13 Yes, yes.
09:38:29 This is I don't know whether we're going to be able to do this. Easily, communally.
09:38:38 So you may see me struggling a little bit with this because I know what's going on here roughly.
09:38:48 But we've had a number of.
09:38:51 Maybe 3 of us can do like, and you and me. While others.
09:38:57 Well, what I want is everybody to see, what's happening unless there are clear tasks that we can give people at the moment.
09:39:08 Hmm, yes, yes.
09:39:09 Do you think that there are clear tasks?
09:39:12 Clear task has not got it right now because
09:39:16 No. So I think it may be a bit boring for people, but it will be a very good introduction on how you deal with.
09:39:27 A very good introduction on how you deal with. A very good introduction on how you deal with, complex projects.
09:39:30 And, if you've got ideas. Be very, me happy to suggest them, but also, expect that, you might find that they're not acceptable to the structure.
09:39:44 We've already got at the moment. This is such a complex project that, you know, my brain is, struggling to manage all of this.
09:39:58 So what I'm going to do on this one. Is, have you had any more, feedback from GitHub.
09:40:08 Renew.
09:40:10 No Peter, nothing, no emails have reverted that.
09:40:13 Right, has anybody else, contributed to GitHub?
09:40:19 Life.
09:40:21 Well, what I mean is we've lost Harshaw, but we need to be putting this stuff up on GitHub and I wondered if GitHub had, blocked anybody else's account.
09:40:38 I mean, nobody is trying to take a risk. So that is the reason that nobody has tried it.
09:40:41 I see, well,
09:40:42 Yeah, because I did it with the 2 account and the same test, same transcript.
09:40:52 Right, well.
09:40:49 The it has did this another account it was also banned. Okay, they already checked.
09:41:01 Hmm.
09:40:58 Right, so it's happened to you twice. Right.
09:41:04 I'm just waiting and otherwise I'll have to ask someone else to, generate with their email.
09:41:11 I didn't need to have account and give it to me so that I can use it for the website and for doing the semantics, It's called, the.
09:41:22 Right, okay. What I'm going to do now is I'm going to assume that I can continue to contribute to discussions.
09:41:30 So,
09:41:29 Yeah.
09:41:33 I'm going to add a comment at the bottom here. Where I put a list of all of the.
09:41:43 Transcripts that we've got.
09:42:01 And
09:42:11 We'll go over these transcripts and we will. Decide whether they're useful and we will label them.
09:42:22 It may be mainly me talking. But it will be us doing the work together. Okay. So, it may be a bit boring, but, trust me, we will come up with something useful at the end.
09:42:38 So. We'll go back in the slack. To find, all the transcripts, by the way, are, safe on my machine and their backed up and so on.
09:42:54 And.
09:42:57 If we can find somewhere to back them up, which is not GitHub. Then, we should do that, because that will make, them safe.
09:43:08 But, at the moment we'll work on What we've got.
09:43:18 And try and give it. Crown represent the overall. Thing here So there will be periods of silence when I think, okay.
09:43:44 So we're going to go back to our slack. Slack doesn't.
09:43:52 Last for a very long period.
09:44:26 So.
09:44:29 It may be that you can help by also looking at your copy. Of the slack here and decide.
09:44:38 Where we want to go back to.
09:44:44 That. It looks like it's not a good idea to host raw text into slack.
09:45:00 Right, so we're getting to the.
09:45:36 I don't know why it suddenly flipped back to March, but you can see by the way here that we can't get back beyond.
09:45:44 That it's You have to pay huge amounts of money. You've probably got to pay.
09:45:54 I don't know something like, $10,000 a month to slack. It is huge.
09:46:28 I will go back and try and label all of these but the impression is that
09:46:42 I don't know why. Why it's taken us back so far.
09:46:52 It'll be late May somewhere.
09:47:08 Right, I've tried to give, an idea here, so that's,
09:47:56 We're still doing software at that stage.
09:48:07 I would like better and more open systems. Can you see how useful this is? As a record of what we've done.
09:48:15 It's not perfect. But, It's allows us to go back. 2 or 3 months.
09:48:31 Yeah.
09:49:30 Still doing Gatsby and stuff.
09:50:07 Right. And. It's still.
09:50:30 What we are now, this is. 2 weeks ago. So yes, so this is where we start looking for it.
09:50:46 Hiashan. Can you see How exciting it is to have all our collaborators creating things.
09:51:03 So we may very well come back and.
09:51:12 Excession to very boring. Okay.
09:51:19 I'm going to start. Noing these.
09:51:31 No, we can go back. They're not going to disappear yet.
09:51:37 Components of a dictionary might be valuable, so Let's go back Monday, June the 3.rd
09:52:03 I've lost my
09:52:08 Believe that on here and we go back to. The repository
09:52:25 Actually, have bookmarks for this, but I don't.
09:52:44 Right side, right side, yes, L is in structure.
09:52:47 Yes. That's right. Well done.
09:53:17 What was it? It was said again. Okay.
09:53:43 Then we got a.
09:53:53 Right, so this one. Session one we have. Mainly.
09:54:19 Right, so I have presented this. So I'm going to.
09:54:51 That's June the 4.th Yeah.
09:55:13 That's not what I wanted at all. Oh, my to me, yes it is, okay.
09:55:34 Alright.
09:55:47 This is making me feel much happier, right? You may all think that it's
09:56:03 Boring.
09:56:09 Right, so this.
09:56:19 Between the 5th
09:56:39 And you can see that what we need is a button where slack post it directly to this but it.
09:56:51 You probably have to pay a lot of money for that.
09:57:15 And we need to get the transcript somewhere. And When you when you got blocked Reno were you posting this to discussion or were you posting it to a Reported.
09:57:30 This discussion 12 discussion number 12 I have created the discussion number 12.
09:57:36 Right. And, it did it when you posted something in, is that right?
09:57:43 I paste all the transmit, the big chunk, the long.
09:57:54 Hmm.
09:57:46 Right, I think, I think probably. I think that that was what the problem was. Okay. So I don't think people should pass transcripts.
09:57:59 In discussion. Hmm.
09:58:07 Yes.
09:58:00 Large things to discussions because what they probably think is that you are trying to spam it. So yes, I, so we will create or use a repository where We put our transcripts in the GitHub repository and not What?
09:58:18 As a test file. Yes, as it as it. Thanks. While we upload that file.
09:58:21 Yes, as a exactly. And I think that Yeah. Good. Well, I'm sorry it's happened to you.
09:58:31 And, yeah, that makes sense. that. Posting these transcripts is not a good idea.
09:58:40 On discussion things okay so that's June here. The 5.th
09:59:14 Right, so we had session one on one day and session 2 on. Another day. And
09:59:28 And we will take that.
09:59:53 I'm going to go on until I've got this summarized and then we will have a a break for tea.
10:00:02 Okay.
10:00:06 So that captures everything.
10:00:12 Yeah, I think that's captured that.
10:00:34 So we're now on Friday, is that right?
10:00:40 No, it still says Thursday.
10:02:05 Now the 11.th
10:02:12 This is a session on Monday.
10:02:18 That was. The. Mainly, debug, mainly software.
10:02:28 And Peter, we have a holiday on Monday.
10:02:33 We do some festival.
10:02:35 Okay, that's thanks very much for letting us know.
10:02:43 Yes. Yeah.
10:02:48 No.
10:02:40 If anyone is interested, you can continue with them. Meeting. I have the holder so I cannot come to the lab but others can join if they are happy to join on line.
10:02:53 That means that choose i've got to try and get most of this together for Tuesday right
10:03:00 Hmm, yes.
10:03:01 And Tuesday we should. Let's work out what the days are.
10:03:12 18.th We have the deadline till 20.th
10:03:19 You know.
10:03:10 She says the 18, th right? Till 20, th right, okay. But I think I can't, I, Do you have any idea whether this is a hard deadline?
10:03:27 In other words, they're not going to cut off software.
10:03:32 They've extended it, but I think
10:03:29 You already expect I think the I don't know about that but It is already expanded after 31st May to June 20.th
10:03:39 After that I didn't.
10:03:38 I know. I will tell them that we're in the process of submitting it. And So.
10:03:46 Sending the reminder to others. Cool. I'm sending the reminder to others who are supposed to submit.
10:03:55 Hmm.
10:03:59 Okay. Okay, you can continue.
10:03:55 Oh, you are. Oh, well done. Okay. Right, well, we'll, we'll get something in.
10:04:05 Hmm.
10:04:09 So this is top level narrative, June the 11.th
10:06:22 And then there was that's on the. What date is that?
10:06:42 That's on the 11.th
10:07:17 This is probably also true of Slack that we shouldn't paste huge things into Slack.
10:07:30 But it was not, in the slide, it was a text file only. It was the text file is uploaded in the slack.
10:07:40 This is the view viewing, yes.
10:07:38 Yes, this is probably okay, actually. They They seem to allow it.
10:07:44 Hmm.
10:08:05 So wait a minute.
10:08:10 Wednesday.
10:08:15 Maybe.
10:08:23 Good I did I post? There's nothing in there, right? I think I I had to rush off in Wednesday.
10:08:31 Do you remember that?
10:08:34 I had a guest. Right. I know. Yes, and I think I record.
10:08:40 Okay, so that's a very
10:08:35 Yes, you're going to the, I think. Okay. 15 min session was there 15 and a half an hour.
10:08:45 Hmm.
10:08:44 Yeah, yes, okay. So we need to post. Something into
10:08:55 I'm not sure whether it's possible to
10:09:00 Edit this.
10:09:06 I need to leave for lunch.
10:09:14 She on Tuesday.
10:09:08 Off you go, off you do. You're all doing brilliantly. When I finish this, I think we'll finish for the day.
10:09:19 I think I just need to go down and. So are you happy for us to work for another?
10:09:26 10 min from now get this. Sorted, okay. So I'm Yes.
10:09:25 Okay. Yes, yes, I am here. Yeah, you can go off and not also.
10:09:38 I'm going to edit this.
10:10:13 That's 12. Okay, that's fine.
10:10:33 Right, so that's Wednesday.
10:10:36 And this, manuscript production will be important.
10:12:16 I'm not going to edit it. That's wrong.
10:12:22 Sorry, I'm putting it into slack.
10:12:29 It's still pushing it into Slack. So that's.
10:13:02 And. I will go through and.
10:13:08 And give all of these things. Name so that we can then put it put them in the right order.
10:13:33 And I'm going to write a top level article from this. Covering everything we want. Which will be converted into the PDF.
10:13:44 I don't think we can use automatic tools at this stage. This will just be me going through everything here.
10:13:51 I'm writing some narrative in this. The
10:13:54 Yes, so we will be sending them in the gold document. So maybe they are going to convert it into the.
10:13:59 Oh yeah, a word. We'll put it in word, but this will be me sticking it together with all of us looking to make sure that.
10:14:03 Hmm. Okay.
10:14:11 It's,
10:14:14 It's correct. Has it been?
10:14:18 Okay.
10:14:22 So that I think
10:14:37 I'm gonna save that. I don't know what's happened to the recordings, but
10:14:44 I don't think they got uploaded.
10:14:50 And do it again. Huh. Oh, wait a minute.
10:14:57 Okay.
10:14:56 Wait a minute. I've got to save it. It's at the bottom of it.
10:15:00 Click on the green button.
10:15:03 And.
10:15:09 Where maybe they.
10:15:14 Put it in the end.
10:15:13 Maybe that. It appears to be in the end. Right, okay, so this has got to be edited.
10:15:22 So this is
10:15:18 Yeah. Hmm.
10:15:26 Okay. Goodness, Jay.
10:15:44 Recording. And now I haven't done a summary of this. So.
10:15:53 Cause if we go back to Wednesday.
10:16:09 I'm not sure where this is from.
10:16:14 Just click on this small button, it will disappear. The transcript. Yes.
10:16:22 Oh, okay, that's absolutely fine.
10:16:32 Yeah, he
10:16:38 Hmm.
10:16:33 It looks like A this manuscript production was what we were going to do. So that's the best that we can do for.
10:16:49 Right, have we got a Thursday recording?
10:16:52 Hmm. This recording that was converted.
10:16:58 Yes, what what did we do yesterday?
10:17:01 Yes, today we did.
10:17:17 I think yesterday we talked about Ranganison, didn't we?
10:17:24 Yes, we have open access and open source.
10:17:29 So if I go back to.
10:17:30 Open source and open access. Hmm.
10:17:34 Okay.
10:17:39 In the 1st session, yes.
10:17:34 Yes, that's right. And we're gonna the whole thing about Ranganathan and then at the end Yes, and the second one.
10:17:44 We have a GitHub ban.
10:17:44 We were all running out of energy was how we, how we create the paper, right? Okay, so that's good.
10:17:50 And at all about the beta ban also.
10:17:53 Absolutely.
10:18:12 So now. We'll edit.
10:18:22 Salescheck.
10:18:30 Yes, these are these. So those are well done. So I'm going to put.
10:18:38 That's in our.
10:19:03 And what do we have in session 2 and
10:19:08 Oh, we create our obstacle, yes.
10:19:40 Right, and now today
10:19:47 We'll put this one in. So.
10:21:26 That's today, 14. We will go back here. And what I'm going to do now is I'm going to Paste this in today.
10:21:39 And then say, goodbye. Now it's possible. I might want some help over no weekend, Friday and Saturday. I'm not planning it.
10:21:53 I'm trying to do all this myself, but if I hit a real crisis, I might come back to you.
10:21:57 Does that make sense, everyone?
10:21:59 Yes.
10:22:02 Yes. Hmm.
10:22:00 Yeah. And similarly on Monday. So, so. You have all been very helpful even if you haven't said a word.
10:22:13 Because I can, I cannot do this alone. Do you know what I mean? I mean, I've gone through this.
10:22:18 Yes, we are.
10:22:27 Hmm.
10:22:20 And you know, hearing renewed. Keep up the conversation. I can see your face and your interest and you smile.
10:22:34 Yeah.
10:22:38 Yeah.
10:22:36 There you go. Right. And so on. That's really valuable.
10:22:43 Okay.
10:22:46 So my plan now is the following. To. Take all those transcripts. And structure them, right?
10:22:59 I will listen to them. I will find out I will have 2 screens I hope. Where I'm listening to the transcript.
10:23:07 And I will click on it when it comes to the right place and I will put in, the structuring so that we know where it is.
10:23:15 So that is then a structured recording. Using marked down as a structure and that I think, could be extremely valuable.
10:23:26 And then I will try and write the overall, top level, word document that we will send to.
10:23:36 Whatever. Now we've got to do some diagrams.
10:23:43 I would like you all actually to sync, start thinking now and perhaps to spend the rest of today if there is any rest of today.
10:23:54 There isn't much. On what diagrams actually go into this. My brain isn't up to doing it today, so I will probably start looking at that tomorrow.
10:24:08 Okay.
10:24:12 There you go. So, Before we finish any final comments.
10:24:34 Absolutely, so
10:24:22 Yeah, for the diagram we can, Think about the process, the, the tools are working or the whole, like, we are using the PDF and then converting into in the, the whole process of the working of the report climate report.
10:24:39 Yes. Yes, and I will, we will make them schematic diagrams.
10:24:47 Hmm.
10:24:49 And if they're schematic, they can be done in,
10:24:53 Graph fish. Yep. Right. So that will be useful.
10:24:54 Yes Hmm. Okay. Awesome.
10:25:00 I may be that I draw them out and. Photograph them and Stick them in and then we're doing them in.
10:25:09 I think that would be valuable.
10:25:14 Yes.
10:25:10 Because it's the model of the story the whole thing is there maybe we can also do the one on the semantic publishing and open access.
10:25:24 Indeed. Indeed, absolutely.
10:25:20 D. Okay. Hmm. Okay.
10:25:29 Right. The main thing is to get the top level Word document in and then we can continue working on this and we will make a big point of that in the final document.
10:25:40 Okay.
10:25:43 Yes, yes.
10:25:46 Right. Wave to everybody. I think I will put the transcripts. I think I'll put the transcripts, up onto the, a semantic climate.
10:26:03 Repository because I think they're more useful than and I will probably give them formal numbers so that we can arrange them.
10:26:12 Makes sense to everybody.
10:26:16 Okay.
10:26:17 Okay, so we now go through the close down ritual, which is.
10:26:21 Okay. Safe transfer.
10:26:24 We start. Yes, If I can find out where it is.
10:26:35 Click on the Zoom Meeting and this you the full new transcript option on the caption button. It will appear.
10:26:46 Yes.
10:26:45 It will appear, okay. That's not what we want.
10:26:57 You are correct. Captions Beautiful transcript. Save transcript, right.
10:27:06 Yeah.
10:27:08 Transcript site and we're going to save the recording.
10:27:13 Stop the recording.
10:27:15 Stop that we're going to stop the recording. Also on Zoom.
10:27:27 Okay.
10:27:28 Trouble is it puts up Windows in different places on my machine. And I
10:27:39 Confuses me. Yes, here.
