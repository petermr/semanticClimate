# session 2

10:19:48 We then have to do captions. And we have to view all transcript. So. When I've got a minute I will try and find out and Oh, whether these transcripts are all the same or which the best one is.
10:20:06 But they're relatively small compared with the Oh yeah and other streams. Okay. Any so Put in the, if you have comments or questions or anything, put them in the slack.
10:20:23 I won't necessarily answer them at the same time. But, We definitely need your feedback.
10:20:35 So.
10:20:39 And put them in coordination. Now, that should be finished now.
10:20:52 Okay, so. The video's been sent. Off we go. So I don't expect this to be more than an hour and it may well be less than an hour.
10:21:04 Right. Okay. So.
## intro
10:21:11 We've now got the motivation for being semantic. The, framework that we're going to use.
10:21:22 Conceptually and technically. And now we're going to give examples. Because, it's 1 thing to come up with, designs for something and it's another to get the world to use this.
## examples
10:21:38 So these are real working examples as are useful to the world.
### static and dynamic

10:21:45 So I'm going to distinguish our sources as static. And dynamic. 

* Static means that they never change.
10:21:58 You can find them the same in 20 years. A 100 years, etc. And that's common for things like religious texts and, cultural works and so on they don't change they might have annotations but the basically it's a static.
10:22:22 Corpus whereas, i

* Dynamic today's knowledge, it's constantly changing.
10:22:32 And if you take something like a Twitter stream, then people delete things. They add replies in different places.
10:22:39 That's the most immediate level of discourse that we have.
10:22:47 We're not going to deal with dynamic things. We have expandable corporate, and that's true of actually of all our corporate on different timescales.
10:23:01 So when we look at the, scholarly literature, that expands daily, Europe, Pubmed Central has many thousands of new papers a day.
10:23:15 When we look at, UN FCC, this updates every year. And when we look at.
10:23:27 Ipcc reports they update every 7 years. So, We're going to deal with, essentially static corpora, which may occasionally be expanded.
10:23:42 But not generally changed. 

#### examples

So the 1st of these, I should also say before we start that some corpora are very homogeneous and some are heterogeneous.
10:24:00 So the UNFCCC reports are extremely homogeneous. They have the same form for each COP meeting.
10:24:10 And the same structure of the documents. The same terminology. So it's possible to create a template which manages those, which will do the same for the next COP and the COP after that and so on.
10:24:26 For IPCC. The report structure probably changes every few years. But for the.
10:24:36 Scholarly literature, we have something much more heterogeneous, where every, Publisher publishes something different.
10:24:47 And it is, a nightmare to bring it all together because they're not semantic, in any sense of the term.
#### UNFCCC

10:24:56 So start with UNFCCC. Now, this is a typical legacy corpus. It's in PDF.
10:25:05 The PDFs are relatively easy to, convert into semantic form because, Say, single column pages.
10:25:18 They have a well-defined structure to their information. And we deal with them by creating heuristics.
10:25:27 That convert them all into semantic form we also, create a, an implicit ontology for them because they use the same terms.
10:25:46 Meeting after meeting. So it's possible to collect those terms. And 2 make the term semantic.
10:25:56 And then to use those to annotate the corpus.
10:26:02 there are no diagrams in UNFCCC. So the only problem we have is that they have in text footnotes.
10:26:14 At the bottom of each page which need detecting they're sometimes a little bit difficult to detect. And we transform those into, end notes rather than footnotes.
10:26:29 Pages have no real relevance in semantic and documents other than as legacy means of addressing.
10:26:42 And the page is a product of printing, not a product of the conceptual design of documents.

#### IPCC
10:26:56 The next is, the IPCC material. And, We start with, the reports.
10:27:09 The report structure has been well set out by Waheb in a set of videos Here it's simply that we have a set of Assessment reports.
10:27:24 At 7 year intervals, within that, We have a number of reports.
10:27:32 Usually about. 7. And within the report, it's explicitly structured into chapters and sections and then subsections and subsubsections.
10:27:54 These are all numbered so it gives us an annotation system. And we have, We can identify the paragraphs.
10:28:07 In. The. There are 2 forms of publication from IPCC.

##### PDF
One is PDFs, so you can get the reports as PDFs. These are normally double column.
10:28:23 The initial release is single column, the final release is double column with graphic. Additions.
10:28:35 But, it's relatively easy to pass this to a stream.

##### HTML
 However, we can also get the HTML.
10:28:46 From the quotes explore unquote. And facility, which gives us HTML in the browser.
10:28:56 This is dynamic, dynamically loaded HTML. So it includes sections which are hideable and viewable by clicking.
10:29:08 And so we need a dynamic.
10:29:13 Loading tool, for this. which hopefully, can download and expand all this material automatically.
10:29:25 And Ayush, developed a tool for this. We, we refer to this as headless browser.
10:29:36 Headless browsing. 

##### Glossary
The, IPCC, also create a glossary.
10:29:48 This glossary is online, firmly online. There is a PDF, the easiest thing we found is to download the glossary, in a headless manner.
10:30:01 You said, and this browser to expand it. But also the glossary material, which is really important.
10:30:11 Is spread over the different reports so different reports all have their own glossary, which, intersects that is distinct from and the main online glossary.
10:30:26 The online grocery has about 700 terms using the chapters we probably take this up to about 2,000 and there are also probably about a thousand abbreviations in the chapters.
10:30:46 So there's probably about between 1,000. 502,000. Entries in this glossary.
10:30:55 And we'll use the term dictionary glossary. And interchangeably.

##### IPCC reports
10:31:01 So, Our job, in all of these then is to turn it into semantic form.
10:31:11 So that we have a complete hierarchical structure all the way down to the paragraph and often down to the individual sentence.
10:31:21 And occasionally splitting the sentences into more than one concept because the IPCC reports. Have an implicit structure of statements.
10:31:36 They're very powerful but they're not structured. In this way and we have to do some empirical expansion.
10:31:47 So scraping this is not easy. 

##### IPCC styles
The IPCC HTML has 2 publication methods.
10:31:57 One uses the WordPress tool, the other the Cats be tool, they require different passing but we have passes for both of these.
10:32:08 And we been able to download all of the Corpus, 70 chapters and expand it to semantic form.
10:32:18 A structural semantic form. 

##### Scholarly Publication
The last component is the scholarly literature and here we use `pygetpapers` and `docanalysis`.
10:32:33 Written by, Ayush Garg and Shweata Hegde.
10:32:38 And these are very powerful general tools for the scholarly nitrogen. So that, Just go in literature is divided into.
10:32:51 Closed and open access. Closed access means we cannot read it without paying and in some cases we can't redistribute or comment on it without permission.
10:33:07 So we restrict ourselves to the open access where we can see this on the open web. And where we can make derivative copies.
10:33:19 And make it semantic and market up. There's a grey legal area over this. Which we won't comment on here, may come up later.
10:33:32 So, I get papers, is a tool to query the, organized open access literature in repositories and at the moment we support the following repositories.
10:33:48 Europe, Pub, Central, which is bioscience but has a lot of open access material, from other disciplines.
10:33:58 Open Alex which is a large metadata inspired collection of the publication. Arising probably out of Microsoft academic graph but now, handed over to the community founded by Heather Pivoire and Jason Prim who've done a brilliant job of.
10:34:24 Making this universally available. In some cases, full text is available in open. Europe, Central in other cases, it isn't and in some cases it's only available as PDF, so we have to be able to deal with that.
10:34:44 P get papers is able to query the material using complex queries so we can build queries with our Amy tools and give them to P get papers.
10:35:05 So you can look for multiple terms and you can create Boolean queries. And it downloads all the hits automatically onto a local machine.
10:35:14 It's then possible to run through that and turn it into semantic form and then, analyze it with dock analysis which uses natural language processing and A I ML tools to interpret this.
10:35:38 The most important initial thing is to classify it. So that we are able to find out what type of a document it is.
10:35:49 And what the concepts in it are. And then, we can apply domain specific tools, such as size spacey, which can, by scientific.
10:36:05 Concepts such as species and chemicals to determine these. And with the advent of.
10:36:17 Of domain specific, AI, for example, in hugging space, we expect Pi get papers and doc analysis to expand and to cover a wide range of subjects.
10:36:30 So it's possible to annotate these documents using modern technology.
10:36:43 So at the end of this, you get semantic documents and you will get some limited automatic annotation from domain specific tools.
10:36:55 In that. So that's our corporate. Those are our corpora that we work with. The
10:37:07 This will all be, this is all available as a work in progress. Which can be hyperlinked from this.
10:37:16 Ideally from the main. HTML discourse. Which will link into the various components and you will see these changing week by week as our community works on them.
10:37:30 No, the technology we've developed, or, web scraping. And for cementification.
10:37:41 Is generic it's not limited to, the single domain of climate.
10:37:52 And so we see the following as possible. Cool for that can be addressed. So. Output from cities on their climate plans.
10:38:06 And I've just downloaded the Cambridge City climate plan. It's about I think 50 pages and can run cementifying tools and our glossary over this.
10:38:24 To add value to that. A really important area is TCs. So that, a thesis is much better prepared than the average scholarly, publication in PDF.
10:38:42 It's single column it separates diagrams from text and, They normally have a fairly, standard, form with, labeled, sections and so on.
10:39:01 So, a primary area that It's just begging to be, made semantic and it would change our method of, publishing scholarship if we could actually work with CCs.
10:39:16 And I'm absolutely sure that would have been. Arguing for. For capturing CCs in an open repository, making them semantic from the start because it's really fairly straightforward to do if you have semantic authoring tools and these could be created within a matter of you know
10:39:47 Certainly months. With a semantic annotator such as a variety of glossaries.
10:39:56 Dictionaries which would update it. So I would say that this is, this is also where, Scholarship is 1st reported in many cases in TCs and they're heavily underused area of scholarship.
10:40:13 Also, comment on legal documents such as judgments of courts. And all laws. And the outputs of organisations such as.
10:40:28 Governments. Non-governmental organization NGO. Sometimes companies And then, perhaps the most immediate and exciting, pre prints.
10:40:44 So the. Scholar community urges people to publish their work as pre prints. And, these again are often single column PDFs.
10:40:57 And in some cases you may even get HTML.
10:41:02 Right, so that's our. And how we deal with them. So I'm having a very quick look here to see.
10:41:15 No comments, okay.
10:41:19 Or cheat.
10:41:26 Okay, so. That was the extension. Now, A bit about how we work. I'll community, is described in a separate article by, Simon.
10:41:40 Wasington and colleagues and that talks about how the semantic climate community was formed, how it operates.
10:41:50 As a community. But I'm going to describe now how we work technically within this part of the community this is the community which focuses on climate documents and their conversion into semantic form.
10:42:09 So. We work by having a zoom session every day and at the beginning of internships and projects this is often 2 h usually split.
10:42:28 And we have an open notebook source. And open notebook for philosophy where we intend to get the results and findings of these zoom sessions onto the public web.
10:42:44 That, we would benefit from having better tools at the moment. Some of this copying has to be, manual.
10:42:55 We record the videos, which have an audio, stream in them. And with tools from Zoom and Slack, we can turn these into, quite usable transcripts in English.
10:43:11 The main downside is that they mangle Indian names because they have a neo-colonialist attitude.
10:43:20 Although I did see that, I did see that you can, actually have tools in zoom for different languages.
10:43:30 And that might. Do somewhat better here. So we have and we have the text transcript. we publish all this material, both the, video recording and the transcript onto slack.
10:43:49 That lasts for a period of about 2 months. and ideally we should copy those transcripts and the audio where appropriate to public sites such as, GitHub would come to in a minute.
10:44:10 The slack is semi casual in that, and because it's got a permanence of 2 months approximately, we can we don't lose information which is of immediate value and and a lot of our discussion takes place on this.
10:44:31 And we have separate channels on slack for different types of discussion. So we have a channel for.
10:44:38 And Piket papers. Called get papers. We have a channel on doc analysis.
10:44:47 We're channel on Amy Lib, the library, that we use. We've developed and, one on Amy climate for climate and there are other ones, as well.
10:45:02 For example cities when we're talking about city plans so there's a structure there which we can use on slack but it's not permanent unless we want to pay literally tens of thousands of dollars a year.
10:45:18 To make it available to us. Then we have GitHub. Now, distinguish between Git and GitHub, G is a technology developed eyeliner's tall f.
10:45:31 Or a multi repository. And preservation and development of documents particularly software it's very powerful it's quite complex and we use a subset of GET.
10:45:51 So the get, subset that we use is we make our own repositories in GitHub.
10:46:00 Maybe I'll start with GitHub. GitHub is a tool for holding repositories.
10:46:08 It's not open. Organizationally, but, everything is accessible on that and the, permission to reuse it is sufficient for our purposes.
10:46:22 So, We published to GitHub in Open Notebook spirit. The repository holds everything so it's completely versions you commit.
10:46:38 Your next version of the of the software or the documents But the old ones are completely preserved. And if you download a Git repository so there might be a repository for.
10:46:53 Pie get papers, then the whole history of that is preserved in your repository. It's got a powerful tool called branching.
10:47:03 So that when we want to develop something we don't want to contaminate. And follow up the main production part of the repository and so we make a branch.
10:47:16 And so for example, I have a branch called PMR underscored Dick. Nichika has a branch called, test nitica and so forth.
10:47:27 And that means we can do our own thing there without fouling things up. And then at regular times, we merge this together when we all agree that those branches are successful.
10:47:38 We discard the branches if they didn't work out.
10:47:45 So, GitHub supports all of that. It also supports, issues.
10:47:53 So when we have a, a problem, we report it formally as an issue. And that is per repository.
10:48:02 We can all so if amy lib doesn't work in one bit someone can post an issue and as a developer I will read that issue.
10:48:16 And it's a formal statement of what the problem is and I will address it when I've got time.
10:48:23 And that's a very, very common and very successful way of working in open source. I'll call it false.
10:48:32 Brand open source software. There are also discussions so that, we put this material up on discussions on GitHub, the whole world can see it.
10:48:46 They can add comments to it. And so forth.
10:48:53 And GitHub material will be preserved indefinitely. Even if the company gets bought by, some mega, well, it's already belongs to a make a capitalist, but if it gets closed, then the Communities will immediately make it open.
10:49:16 So, we come on to, Good, get is a tool for managing version documents.
10:49:28 It's got hundreds of commands. It can be very complex. But we try and stick with a very small number of.
10:49:41 Get clone to download the repository onto your own machine. Get status to tell you where you were at.
10:49:51 Get commit which says, Mark, what I have done as a version and be prepared to push it to other repositories.
10:50:01 You don't have to push it. And get push. We'll push it, to a repository.
10:50:09 So, When you've got it on your machine to get a new version from your.
10:50:18 Remote online repository you say get all and that's about the limit of the commands or newcomers.
10:50:28 If you can master those ones, You've got 90% of what we do. If you follow up, then there are ways of recovery, but it's a good idea not to follow up.
10:50:45 And if you have got people developing different branches, and so I might for example develop a branch which deals with
10:51:00 Annotation and somebody else might deal with a branch which does indexing. And then we try and merge each branch together into the main branch.
10:51:12 So you would merge the indexing branch into the main branch. There might be incompatibilities so you would resolve those with git merge.
10:51:25 And then you might do the same thing for the, Other thing I mentioned. and merge that and so and so a Okay, get supportive repository is a stream of branches like that which come back and emerged and branched out and so on and so forth.
10:51:49 But generally there is a main branch and that main branch. It's the one that people should use.
10:51:56 For the,
10:52:00 For their production work. We do all our development in Python. Over the last 10 years, there's been a big input.
10:52:17 To make all the document management software. And most of the scientific software, compatible, regardless of which, and programming language you use, and so although some of the libraries we use are not Python at the level like network X and, other things of that sort.
10:52:49 They have Python wrappers which are well tested and and so on. So assume that everything you want is available in Python or Python wrapper.
10:53:02 There are 2 ways of using. Our software one is on your own machine where you get clone a repository, you might make some modifications and you run it.
10:53:17 Locally as a Python program, using the Python, command. And let me say that.
10:53:27 At the moment, everything we do is based on running things on the command line. We are developing methods of making it easier to use, in, both Google Collab.
10:53:43 And other containers and also building our own. IDE, not ID, and, which will help us navigate things like dictionaries and so on.
10:53:56 But at the moment most of the work is done on the command line.
10:54:02 And then the other. Alternative and complementary match approaches where you install things and you do this by posting a version of your software to Pi.
10:54:19 Which is a collection of 500,000 open source programs and so get papers I get papers, doc analysis.
10:54:32 Amy, Lib, Amy, Climate, are all on Python. And the advantage of Python is you can just install it with the pip command so pip install P get papers and then you have P get papers on your machine that will install the latest version but Pi Pi also supports semantic questioning so sometimes we have to use specific versions of software
10:55:08 And there will be links into lots of that, We work by being task driven. So when a new person comes in, as an intern, or as a volunteer.
10:55:26 Then they have 2 or 3 tasks which are distinct from everybody else but use the same technology so They choose a chapter of the IPCC reports.
10:55:46 There are 50 chapters. There may be 70 chapters, I think. and they choose one which appeals to them.
10:55:56 And then they work on that chapter, but they will. Carry out the same tasks on that chapter so they will learn how to download it they'll learn how to cement learn how to extract terms from it, they'll know how to annotate it.
10:56:17 And so forth. And at the end, they will have a chapter which is Similar in structure and semantics to all the other chapters we process.
10:56:29 So, this works very well because, everyone, shares in their knowledge. We call it learning by doing so when you start this.
10:56:40 Things won't always work out. There's no, blame in this.
10:56:48 And other people who are more experienced will be able to help on that. So that's the chapters.
10:56:57 And then on the other side, we have the glossary. The glossary has perhaps 2,000 terms.
10:57:04 At the moment we ask people to select a particular letter of the alphabet in the glossary and and then to make the entries there as semantic as possible.
10:57:18 So they're available in HTML. From Simon Worthington's, work.
10:57:25 And there is a partial, structure to those in interglossary links.
10:57:34 But we want to make those more.
10:57:39 Semantic by adding in other annotations and other links. And Perhaps the.
10:57:52 Epitome of what we want to create is a knowledge graph and knowledge graphs, a network of at rich triples of an ontologically enhanced triples.
10:58:06 Which allow us to link together all of the things, in this so that it links together components in a chapter, it links cross chapter references, it links Glossaries together it links the annotation of glossaries of chapters, black glossaries.
10:58:28 It links everything we have in semantic form. So a knowledge graph is a huge and concept. Construct but the good news is that it's now something that many people are working on.
10:58:44 You know it's a mainstream information science. And so, We can expect.
10:58:51 A wide range of tools that help us now, it's not easy to navigate knowledge graphs.
10:58:57 Without software and even with software you tend to get a huge cluster so ways of navigating through that are really important.
10:59:09 And then we come on to our. Ontoological, semantics and we do that with Wikimedia.
10:59:19 We can media is the, generic container for, what we call Wikipedia.
10:59:28 Thank you also includes, Wiki Data, 100 million plus. Semantic terms wiki publications, wiki journals, and Wikimedia resources such as images.
10:59:46 So it's a vast collection of intellect, interlinked. Semantic knowledge.
10:59:52 By default, we would say that any term that we use should be linked into the Wikimedia structure.
11:00:04 Both the Wikimedia page and the Wikimedia and the Wiki data.
11:00:12 Entry where possible. And we're writing tools which will take a phrase and retrieve both of those automatically.
11:00:24 There will be a lot of ambiguity so it needs human filtering but Is that this is a very powerful tool indeed.
11:00:33 So that's what we're aiming for.
11:00:37 Now, just a little bit about the software. And then about the projectory and then we will have finished this session.
11:00:47 Unless our community has added things which we should talk about and haven't. So software software structure now.
11:01:00 It's all in Python. Where ever possible, we use libraries. So libraries are things like pandas or, Spacey, or, requests or whatever.
11:01:16 Libraries which other people have written and which we rely on. And. So we try never to reinvent the wheel.
11:01:27 We however are non specialists. So, some of the more, advanced Python constructs.
11:01:38 Such as functional programming, and sometimes,
11:01:44 Yields and properties and things like that can be a bit daunting for newcomers. So we deliberately keep our discourse.
11:01:56 Barely, simple, and in some cases we write our own convenience routines to make things easier for the newcomer or newcomer from other languages.
11:02:13 So, it's aimed at that. And so far that's been very successful.
11:02:25 Our software is dynamic, so it's continually versioned. And we produce our libraries which are on Pi Pi and can be reused.
11:02:38 Those by ourselves and by other people. Very briefly. Sweet.
11:02:45 Apart from the existing 3rd party libraries. We have PIE get papers which, aims at downloading, scholarly publications.
11:03:02 From, repositories, and it covers. You're Pubmed Central Open Alex and the preprint literature.
11:03:13 I haven't mentioned pre prints that should go earlier. Freeprints. A form of open access publishing, which is highly encouraged.
11:03:24 And which, means that before you publish the formal version of a paper, you should expose it as a pre print.
11:03:34 And there are many pre print servers. We will probably use. well, we'll see if there's a appropriate one in India.
11:03:45 But we might use something like, which is run by the library at CERN. And is a leading open access.
11:03:54 And advocate.
11:04:02 So, PIECE, And one of the things about these repositories, is they have a query language, which is usually bullying queries based on a restful API.
11:04:16 So, get papers as, created APIs for, uses the APIs for Europe Pubmed Central Open Alex.
11:04:28 And, preprints were available and preprints occur in things like bio archive and med archive.
11:04:39 And the classical archive of physics and mathematics. I get papers, downloads onto your local disk, and all the, all the papers and their components, it's Time, and it has a separate.
11:05:04 Component for the metadata. Where the full text is available, it downloads. XML.
11:05:13 From your Popman Central where it isn't, it tries to get the PDF. And open Alex is, grows out of,
11:05:27 What's it called? On pay wall, and, the open access button which allows you to press.
11:05:39 On, a close publication and see if there is an open access. Version on a university or private repository or possibly in Doc analysis takes the output of PYGET papers and applies some ontoological markup to it.
11:06:09 And filtering so that you can use doc analysis, to decide which of the papers you've downloaded are most relevant to you.
11:06:18 And often there will be a 3 h of often up to. 10 times or you know 10% might be retained or something of that sort depending on this and then you can revisit that and perhaps tune up.
11:06:38 The query and both Doc analysis and Python papers can use our dictionaries to help, create this sort of query we need.
11:06:49 So if we are working that say on
11:06:54 Let's say that we're working on something like, Hi, justice. Climate justice we would want a dictionary on climate terms and a dictionary on justice terms and justice might include things like human rights and court of human rights, and European Court of Justice.
11:07:17 And things of that sort. Climate might include terms such as IPCC and sea level rise who knows what it might be.
11:07:30 Then separately, but related are the Amy tools. Amy is, involved in creating the Struck, semantic documents so it will take a legacy documents and such as PDFs, and much HTML, strip out non, content.
11:07:58 So, embellishments and navigation and things of those sorts and turn it into a semantic HTML.
11:08:07 Well, I, semantic IDs and sectioning are implemented. Then to make it a Then to make it, ontologically, semantic, we will have tools, which, use semantic, dictionaries, such as the IPCC glossary and that marks up.
11:08:37 These structural semantics with ontological semantics. And, the aiming climate tool, is a developing example of that.
11:08:49 These are all dynamic. They're continually changing. I get papers has a very stable release.
11:08:59 Talk analysis has stable releases and both of these have very good tutorial support so they're easy to get to use.
11:09:11 I'm Amy Lib is becoming. frozen. Or developing a frozen version.
11:09:20 But there still needs to be a lot of work on documentation there. How to use it.
11:09:28 Amy climate. This primary concerned with, IPCC materials, and, You UNFCC materials.
11:09:40 And making those structurally semantic at the moment. But, hopefully adding ontological semantic soon.
11:09:51 So those are what we've got. And that's how we work. And I don't see any comments that I've.
11:10:03 Missed anything out so what is our projectory So this is the future. Now, we only write about the future where it is not paper where this is very much going to happen.
11:10:20 It's being actively worked on at the moment and because we do everything open, you can come and see our factory if you like and look at the components.
11:10:31 Far too many scholarly publications are vapor where people talk about what they are going to do and it never happens.
11:10:40 This is talking about what we are actually doing. At the moment. So on the dictionary we are working towards a universal climate semantic climate dictionary where all the terms in climates are
11:11:01 Extracted from major climate resources such as IPCC or the current literature. And where those are then, embedded in the Wiki data.
11:11:15 Global graph. So, that is ongoing. And we've done it for a number of letters in the dictionary.
11:11:25 And so in terms of IPCC, which is static. Our aim is to come up with a knowledge graph for IPCC.
11:11:36 We've done this, with or, Egon Villegan has, prototype this for.
11:11:43 Part of the SYR synthesis report. And, so, the IPCC material consists of micros structure at the nano publications level.
11:12:00 Semantic addressing so that you can address within a report. The reports make, frequent, reference to other reports.
11:12:13 So we can address out and into these other reports, and we can micro address because we will have that semantic at the sentence level.
11:12:26 And the IPCC also links out to scholarly publications and other reports so we can link to that.
11:12:38 We are working on diagrams, but they're a little bit, on the back burner.
11:12:45 We have been able to make semantic diagrams with the components of the diagram are rendered in SVG and we can navigate round them but it's relatively early days.
11:12:57 For that. And we are aiming to create a intelligent scholarly reader which contains all of PI get papers, doc analysis.
11:13:12 Amy Lib and then domain specific. And interpretations on top of that. And we hope that with climate we can demonstrate this in a short period of time.
11:13:29 Now, one of the things that's happened since we started this, is the huge development of official intelligence and machine learning.
11:13:41 And how does what we do relate into that. Now. Hey, I is not a new concept.
11:13:52 Machine learning is not a new concept. They are 50 years old, at least. but in the last Hi, Piers, they've suddenly exploded into public prominence.
11:14:06 And this is because of the development of large language models and generative AI. Large language models.
11:14:15 Use a, a background corpus if you like of interpreted documents.
11:14:26 To enhance our understanding of sentences, paragraphs and documents.
11:14:35 Generative AI takes the same general background of scraping and allows you to predict. Where as, sentence or piece of desk course might go and so to create documents in the certain style and with certain types of Noledge.
11:15:02 This is a very, rapidly growing field. It's also very contentious because what all of these tools most of these tools are created by closed mega corporations whose business model is knowledge created by closed mega corporations whose business model is knowledge created by closed mega corporations whose business model is knowledge surveillance capitalism Let me scrape whatever.
11:15:29 Documents they can get. Public documents such as Wikipedia which has been a huge input into these without any permission.
11:15:40 They also scrape a lot of private material so that today there's an answer, Apple, we're adding AI to their tools.
11:15:50 I mean, they do it already, but they will. Take your emails, your photographs. Your discourse and they will scrape that and you so all of what you create in an Apple environment will be in their models.
11:16:08 The same is true for Google. And for the others, like, Musk with, X, Twitter, and so forth.
11:16:20 So the vast majority of AI, ML at the moment is Created in closed form by Mega Corporation.
11:16:30 So those mega corporations do not have the. Well, of the world at heart. They have they,
11:16:41 Exponential growth of their corporations by knowledge capture and reuse This means that you cannot rely on them.
11:16:53 To, to do anything they do what they want. You cannot rely on them to be transparent.
11:17:00 They do what they want and publish it. When or if they feel like it. And, they do not honor.
11:17:11 Either the, formal legal requirements of copyright or the ethics of open publication.
11:17:21 So There are a few open alternatives to this. I won't describe them all here, but we work on the basis that everything we do is open and could and should be incorporated into open models.
11:17:39 So, This set of open models is offered to the fully open community as something that can be used, with acknowledgement, but without permission, as, a useful component in creating semantic climate.
11:18:02 Right. That's the end of what I have to say. I'm just going to put, some, Foot, footnotes onto this.
11:18:15 The authorship of this document will honor All of the people who've made significant contributions to.
11:18:29 What we're working with at the moment because apart from PI get papers and doc analysis, there's been no scholarly publication on, The whole of the semantic climate effort which has included not just climate but also plants and barrel epidemics.
11:18:54 We have published a lot in video form. And in public presentations. So those people who have published in this form, significantly should be honored.
11:19:11 I can't remember all the people in my head. We've got probably a hundred 50 people who've are on our slack who participated in some.
11:19:24 Way. Some people have only been briefly here, they haven't finished their internships.
11:19:32 And have made an important
11:19:37 Recorded contribution so we'll have an approximate contribution of people who finished their internships and have created a useful.
11:19:50 Written report at the end or a significant online presentation. As a talk or video.
11:20:05 We will start with when we, and created open virus, which if you like was the 1st community approach.
11:20:16 And so for example, we will, and, invite Ambri, to be one of the authors of this because she was the 1st person because she was the 1st person to do machine learning And, She very much, held together, our first, st set of internships.
11:20:42 And, and so and so. Hi.
11:20:50 Reno and one or 2 others will go through and try and remember the contributions that have been made by the semantic climate community over the
11:21:07 We will probably as and we will record all of our presentations or we will hyperlink to them because they're already, established in the work that has been done by Wahab and and Shoopam in pulling this together and Renew in documenting it on the semantic climate, web page.
11:21:36 So that's the authorship.
11:21:43 I see we will have to have a mechanism for. Updating our narratives. That's not too difficult if they're HTML.
11:21:55 Because we will probably make them available on github discussions and people can comment on that. And so long as they are member of GitHub.
11:22:08 Right.
11:22:12 I see that that is or. Here. Renee, any comments?
11:22:22 So we have included all the aspects like starting from the semantic climate, I think all the passports have been included.
11:22:36 Right.
11:22:36 But we.
11:22:39 Now we need to structure it accordingly.
11:22:42 Absolutely, so What? What we will do is we will ask. Our.
11:22:52 We'll ask, people like Polly who has already reviewed, One of our, outputs and poly will be a really good.
11:23:06 Reviewer for this because she comes knowing she needs this coming from an NGO and climate justice oriented background.
11:23:16 And also has no prior knowledge of Python, or a lot of the material we're doing.
11:23:26 So if you can understand it, I think that's a level we can aim for. I mean, we can't take.
11:23:30 So, but we have to clean that content.
11:23:34 Oh, we have to clean it a lot, yes.
11:23:36 Presented in a like a paragraph and section.
11:23:40 Absolutely. I've tried to make it sections. it should be fairly easy to.
11:23:48 Add the sections into this. But this is what we will have to work on. Over the next period.
11:23:56 I have
11:24:00 I have a lunch engagement and I shall not be available most of the Uk's afternoon but do listen to the transcripts which I will Now.
11:24:13 Hmm. So do we need to clean that content or?
11:24:21 Well, I would suggest we take the transcripts as they are at the moment. You know, there's not much, Material that's not relevant.
11:24:32 Hmm.
11:24:37 Yes.
11:24:31 There are places where I've sort of said and then we look at X and then we'll look at why and then we'll look at Z, you know, that's easy to deal with.
11:24:44 And we have to edit that in. I know one or 2 cases where we say we deal with that later and so forth.
11:24:51 But the key thing is that we say we deal with that later and so forth. But the key thing is that we haven't omitted anything.
11:24:55 Hmm.
11:24:58 I will. Very much value. Faces view on this.
11:25:05 And ask her.
11:25:05 Okay, then you'll post it.
11:25:07 Right. Well, I'm going to now close the transcript, assuming that everyone's happy with that.
11:25:11 The Save them.
11:25:14 So save transcript. And then. Close. Stop the screen.
