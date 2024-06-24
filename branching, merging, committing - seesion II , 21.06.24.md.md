## BRANCHING
Right, what I'm going to do now is I'm going to the, documents that we've already got.

[PMR] 	
So if we go to a list and we say get Status then I'm on PMR one. Origin is,I'm never quite sure what origin is, so I'm not going to say anything here.

[Peter Murray-Rust]
Somewhere, these are all the files that I have. Which. But otherwise. All the PMR one branches files are in the system and have been pushed.

[PMR]
Right. A number of these I'm just checking to see if any of these are important.

[PMR]
But I don't think so, right. So this is in the branch. Now I'm going to,Check out Which really means switch branches, but the word is check out. A main it used to be called master that was felt to be rather colonial.

[PMR] 
Yes, has been changed to main, but you will still find, tutorials and so on.
That talk about Awesome. Okay. This is up to date as well. So we have 2 branches.

[PMR]    
And we want to synchronize those and we believe that main has got stuff that that, PMR one has it. Now I went to the web to find out how to do this. Let me check for somewhere on that..

## MERGING

[PMR]    
That we put main in.I want to merge the main into branch. That's always safe because it won't hurt main.

[PMR]    
It, Right, so, so you can see why it says main here. Master, but we'll change it to main.

[PMR]    
So, okay, git merged master into branch.

[PMR]    
I had one which I, we don't want to use rebase at all.

[PMR]   
I think it was this one was very simple. So we check out main. All to make sure that it is an up to date.

[PMR]   
We check out our branch. This branch is called valid data. Here this, ours is called PMR one.

[PMR]    
We merge the main and when we push, okay. So that's what we're going to do.

[PMR]    
So here I am. On main, I will, git pull.

[PMR]    
Just to make sure it's up to date. I will check out PMR one.

[PMR]    
Which means change branches.

[PMR]    
Okay. And then we are going to, get, get, Main. So merging main.

[PMR]    
In PMR one. If we are fortunate and there are I don't many changes any any main differences or if you know the files don't overlap.

[PMR]   
This will be straightforward. If however we've got more than one version of the file, we have to take decisions as to which one to do.

[PMR]  
So let's see how this works out. And there's a visual tool which will help us.

[PMR]   
So git merge main

[PMR]   
It's got quite a lot of thinking to do. It's a very sophisticated system is, git.

[PMR]   
Merge conflict in Read. Okay. So Can I do this in `pycharm`,  let me see if this, works in `pycharm`

[PMR]   
Is it a remote? I'll go in here. I have checked out. Main.

[PMR]   
Yeah.

[PMR]   
I saw that it here would actually bring up a visual editor. I'm disappointed it hasn't. Okay

[PMR]   
At least read me is not very very large

[PMR]   
Why? Let's see.

[PMR] 
She's not particularly helpful.

[PMR]   
We haven't even got to read me. On this one.

[PMR]   
Right, there's a lot of differences here.

[PMR] 
Oh, of course it may be to read me at the top.

[PMR]  
Hey, this is just a subdirectory.

[PMR]   29 59
I hope it's not going to do it on every file.

[PMR]   30 18
Right, so yes, so. It's not been able to merge. This here so.

[PMR]   
That's actually put both of those in and see if it. If it manages this.

[PMR]   
Okay, so we've edited that maybe.

[PMR]  
Okay, I wish it would actually tell us which the, merged files were.

[PMR]   
I can get some idea of this.

[PMR]  
So I'm going to have to.

[PMR]   
Go back to the web and look for this. These have obviously diverged more, than they should do.

[PMR]   
And this is a reason for not keeping your branches widely separated.

[PMR]   
I'm gonna look for how to do this.

[Sravya]  
Okay. I think, the, I mean, the both files are not merged .

[PMR]  
No, they, no, it's not merging. We want to, merge them.

[PMR]   
Right.

[Sravya]   
In that case, you can merge the, files in GitHub.

[PMR]   
Right, do you know how to do this?

[Sravya]   
So I just asked the Google how to do that and

[Sravya]  
I think it should be only done in GitHub.

[PMR]  
This is I mean, I've run into these sorts of problems before. I wish it said which the files were.

[PMR]   
I mean. I'm going to go back and see what. Clearly.

[PMR]   
I'll have to think. 

[PMR]   
Maybe it's just to read me, so git add file.

[PMR]   
Let me try again.

[PMR]   
Okay, so.

[PMR]  
Okay, let me try to merge. Which am I on? I'm on Branch PMR one, that's fine.

[PMR] 
So I'm gonna go back to the merge, and see what happens.

[PMR]   
No.

[PMR]  
Okay.

[PMR] 
Right, okay, now if I am lucky, it's push those files to git.

[PMR] 
Recent pushes, okay. Well, on Main, Main contains ALIS, right?

[PMR]   
We go to PMR one.

[PMR]   
Yeah. And it's now got a list, right? Is that right?

[Sravya]   
Yeah.

## FRICTIONS IN MERGING

[PMR]        
So 1st of all, Many thanks to both of you for your. It is a It is a patient area this.

[PMR]       
Secondly, It is incredibly complicated. Git. And, You work by having a small number of commands that you know work and when you run into problems you take things very, very slowly.

[Sravya]        
Yes.

[PMR]        
We didn't, we didn't go off. And find commands like rebase everything. Minus fix it or something of that sort.

[PMR]        
We came down to the situation where there was one file which was a problem. No, I don't actually care what that file looks like.

[PMR]  
Yes, certainly got stuff at the bottom there. It's actually got both of them in.

[PMR] 
The merge is very powerful. And occasionally, crypts up on very small problems but it's an incredibly powerful system and if it is used , then, you find that there are very few, problems, and that you have to, that what you have to do is just keep it up to date No, I've now got a PMR one which is my own and which is compatible with main. So I can now continue to make changes to PMR one.

[PMR]  
And push to PMR one but from time to time we are going to have to then integrate PMR one and and Sravya and Parijat and Nitika and so on with the main, right?

[PMR]   
So we don't want to We don't want to leave that too long. Right, wow.

[PMR]   
That's so. I really thought we were going to be in trouble then, right? So don't be afraid of, of the get commands but if you don't understand them Look them up, look for the simplest ones ask on the slack. Always ask on the slack. If you're unclear, ask for somebody to share a session with you.

## ADDING MARKEDDOWN FILES TO GITHUB

[PMR]
What are we going to do now?

[Parijat Bhadra]       
How do we add the summaries?

[PMR]    
Right. Okay, that's, that's a very good, thing. So let's go through, let's go through that.

[PMR]        
Right. Okay. What about you, Parijat? Have you anything in, Markdown ?

[Parijat Bhadra]      
yeah, I did it on Mark Down and like, saved it as an HTML file. I didn't summarize it. I cleaned it up a bit.

[PMR]     
Right.

[PMR]    
In the summary, What I'm going to suggest is we make one sentence for each of these, right?

[PMR]     
So, If you can open a file. Which, now this is a good question as to where the file is.

[PMR]        
What's the name of the file?

[Parijat Bhadra]  
This is open notebook and semantic climate.

[PMR]    
Right, okay.

[Parijat Bhadra]  
Then this was a little bit on `pygetpapers`

[PMR]   
Right. `pygetpapers`, so I get papers is all one word.

[PMR]    
Right. And also a software should always be lower case. So that's,

[PMR]    
It should be lower case. So the P should be. Lower case.

[PMR]     
That's right. And also, it should be, in it should be in, code form.

[PMR]        
That's it. Okay, if you save that. And now, view it.

[PMR]      
Yes. I think you will see that that is a different color. Is that right?

[Parijat Bhadra]    
Yes, yes.

[PMR]        
Yes, exactly. Okay, so. Everybody should make sure that The software is always bracketed with an opening and the closing back tick.

## GLOBAL EDITING TOOL

[PMR]        
As you know, it's a universal, convention. Right, so if you go through and make sure now you should be able to do that with a global edit right so do you have a tool which allows you to do a global edit what are we looking at this, what tool are we looking at this 

[Parijat Bhadra]      1 
That's something I wanted to ask you that I understood how we are using regular expression, but I don't know how to bring it into this like, picture like, Exactly.

[PMR]     
Yes.

[PMR]      
We're looking at the documents here what tool is being used to display the documents

[PMR]     
I mean, it says, Dillinger at the top 

[Parijat Bhadra]      
Yes, this is one of the like tools of markdown itself. It allows us to write it down on the left side and on the right side we already have the HTML part.

[PMR]      
Brilliant, brilliant. Okay. Well, What you have to do, I'll have a look for this at the moment.

[PMR]    
So, if I Look for global editing.

[PMR]       
Right. So.

[PMR]     
I think you need a local text editor, okay?

[Parijat Bhadra]        
Okay.

[PMR]        
Let's put your file in a branch, okay?

[Parijat Bhadra]        
Okay.

## SAVING A MARKDOWN FILE

[PMR]  
Indeed. Okay. So, Come out of Dillinger.

[PMR] 
Now, so, okay, before you do that, You've got a version here of your of this. That's in a Google Doc at the moment. Is that right?.

[Parijat Bhadra] 
Yes

[PMR]        
So, and this is for everybody. Everybody should have their files in their system.

[PMR]        
Export as marked down.

[PMR]        
Excellent. This is exactly the file you want. This is what you should be working with.

[Sravya]        
Oh, Peter, just now I also converted my document into Market and saved it.

[PMR]        
Good. Brilliant. Okay. So.

[PMR]        
Okay, fine. Well, Stavia, can you use the command line?

[Sravya]        
Yes, Peter, I can.

[PMR]        
So Sravya, if you can take the screen.

[Sravya]        
Yes, Peter. And this is my Markdown.

[PMR]        
Okay, good. What we want to do is just make a Git branch. And, and then commit the file.

[PMR]        
That's all we're going to do at the moment. So. Can you open the command line part of this?

[Sravya]        
Yes.

[PMR]        
Okay, so. If you can now go to if you can go to the directory, the repository on your system so this is semantic climate and go to the ALIS        .

[PMR]        
Excellent, okay. So. Can you type git?

[Sravya]        
Okay.

[PMR]        
Alright. So that.

[Sravya]        
Just a minute bit. I am just navigating.

[PMR]        
It's all right. I, I, you know, I have the same problem.

[Sravya]        
Yeah.

[Sravya]       
I don't know what's happening, but I'm

[PMR]       
I see. If you go to If you

[Sravya]       
But I can, I can open it in.

[PMR]       
All you need is a file name. So it looks to me as if it should be under wind.

[PMR]       
If you click on the users, it may tell you what the path is. 

[Sravya]       
Oh, Peter, can I do it in VS code?

[PMR]       
Yes, do it in VS code

[Sravya]       
Okay. I have semantic climate here.

[PMR]       
Right. Okay. Right. What we're going to have to do is to find the gIt extension in VS code.

[PMR]       
So this is useful.

[Sravya]        
Yes. I got it.

[PMR]        
Right, so type dir there and see what happens.

[Sravya]        
Okay.

[PMR]        
Right. Do you recognize? Yes, alis2024. Right.

[PMR]        
Do you see that?

[Sravya]        
Yes.

[PMR]        
Okay, that's fine. So for some reason you're called HP, right? That's fine.

[PMR]        
So. If you should have a, so what you can do is use get. So if you go to the left hand side.

[PMR]        
There's a row of icons. And now go right over to your left margin.

[PMR]        
And. Go to the top left of your window. There, yeah, left, left. Yeah.

[Sravya]       
Yeah.

[PMR]        
The next one, that's kit. Click on it.

[PMR]        
Right. 

[PMR]        
I'm not sure what it's showing me that this. If you go, okay, try it on the command line, go down to a very bottom and type git.

[PMR]        
Okay.

[PMR]        
Good, you got Git in the system. Okay. Now do git status.

[PMR]        
Yep. You're on branch PMR one great you want to make a new branch right so you say git Branch.

[PMR]       
And now let's. Call it Sravya or whatever, right? I  think no minus.
.
[PMR]        
I think you should put your name in it so that we know so and don't put minus.

[Sravya]        
Oh, okay.

[PMR]        
Right, now. You're now on your branch. Just do git status.

[Sravya]        
Yes.

[PMR]        
Right, your branch is up to date.

[PMR]        
I know. With that, just try git make, make a file. Just make an edit.

[PMR]        
Edit a read me file or something like that.

[PMR]        
So we're work, wait, We are, which one are we working on?

[PMR]        
We're working on alis2024 yes, and but. Oh.

[PMR]        
This is open notebook, right, okay. So let's. Open a new file in

[Sravya]        
Yes, Peter.

[PMR]        
Open a new file in VS code. Just a new file. And we will call it summary.

[Sravya]        
Okay.

[PMR]        
No, put some summary, open notebook, right? We may need to make extra branches at the moment, but you're writing a summary about Open Notebook.

[PMR]        
So summary_open notebook.

[PMR]        
That's right.

[PMR]        
oh, let's make it a mark down file.

[Sravya]        
Okay.

[PMR]        
Right. Okay. And now let's just put in this, put in hash.

[PMR]        
Yes, space. Summary of. Open notebook, underscore.

[PMR]        
Whatever the file was called open notebook.

[Sravya]        
Okay. underscore?

[PMR]        
Yeah. No, just put space.

[Sravya]        
Okay.

[PMR]        
Section. It doesn't really matter what we've got in because we're going to edit it right.

[PMR]        
And then type. After this, put us a new line. And put Summary of Topics

[Sravya]        
With hash.

[PMR]        
Hey, it's a good no, no hash. Good idea to put a blank line here.

[Sravya]        
Okay.
.
[PMR]        
Summary of topics in.

[PMR]        
And what was the file called?

[PMR]       
Let me see if I've got it on mine. So just, I's half a minute.

[PMR]        
It was called Open note_semantic.

[PMR]        
Okay, that's fine. That's all you need to do at the moment. And then, let's save that file.

[Sravya]        
Okay. Yes.

## ADDING A FILE TO GIT

[PMR]        
Right and now let's go to git

[PMR]        
And say git status.

[PMR]       
And it should tell us we got a new file. Right, do you see that?

[Sravya]        
Yes, Peter.

[PMR]        
Right, on track. So you've got to add that now. You can either add it in VS Code or you can add it directly here. So let's add it directly here. Git_Space , Add. And then this file, summary note. Yeah.

[Sravya]        
Is that okay?

[PMR]        
Good. Yeah, that's absolutely fine. Now do git status again.

[PMR]        
And what you'll see now is You've got a change to be committed. Do you see that?

[Sravya]        
Yes, Peter.

[PMR]        
So the red one was not in the system. The green one is in the system. So what we now do is, we have to commit it.

[PMR]        
So we say git commit - "am".

[PMR]        
And say, added summary for Open Notebook session.

[PMR]        
Right, okay. Return.

[PMR]        
So. It tells you it's done it. Now do git status again.

[Sravya]        
Yes.

[PMR]        
And now it says your branch is ahead of origin PMR one by one commit. So you've got to push it so git push.

[Sravya]        
Yes, Peter.

[PMR]        
That's it.

## ADDING SRAVYA AS A CONTRIBUTOR ON GITHUB

[PMR]        
Oh, okay. You don't have Permission here, right? So you have got to leave your screen as it is.

[PMR]        
You won't see this on your screen. Let me just,

[PMR]        
So I'm going to speak what I do. Maybe I will take the screen and show you, how we do this.

[Sravya]        
Yes.

[PMR]        
Right, can you see the screen? So this is our repository. Let's just have a look and see what branches we've got on this.

[Sravya]        
Yes.

[PMR]        
We got quite a lot of branches but we don't have yet have yours so what we're going to do is add you as a contributor.

[PMR]        
So to do that. I have to remember how to do it.

[PMR]        
Sorry, go to settings. I go to collaborators.

[PMR]        
Right, I now add people. So I have to add you to this report and you have to do this for every repository, right?

[Sravya]        
Okay.

[PMR]        
Invite collaborator.You Well now get an email which you have to reply to.

[Sravya]        
Yes, Peter, I will check it.

[Sravya]        
Yeah, I got the mail

[PMR]        
Right, okay, so now I go back to Semantic climate

[Sravya]        
It is saying that I now have the push access.

[PMR]        
Excellent. Okay, so now I go to settings, Collaborators

[PMR]        
Are you seeing my screen still?

[Sravya]        
Yes, yes, Peter.

[PMR]        
Okay.

[PMR]        
Right here. Oh, you already have access to this. 

[Sravya]        
Yes.

[PMR]        
No, you need to take the screen back, right?

[Sravya]        
Yes, we do.

[PMR]        
And already and did you okay you take the screen back so I need to stop sharing the screen.

[Sravya]        
Yeah.

[Sravya]        
Can you see my screen?

[PMR]        
It's brilliant. Yeah. Okay.

## NEW BRANCH

[Sravya]        
I'm doing this.

[PMR]        
Yeah, yeah, it's a game.

[Sravya]        
Yeah, that.

[PMR]        
Brilliant. Okay.

[PMR]        
Do git status. I'm not sure you pushed it to the right branch. Just do git status.

[Sravya]        
Oh.

[PMR]        
Right, okay. Do git checkout. Sravya or whatever you called it.

[PMR]        
No, let's make a change to that. And what was the file called?

[PMR]        
It's called summary_open notebook, isn't it? So.

[Sravya]        
Yes.

[PMR]        
You've now got to Cd alis2024 . So.

[PMR]        
At the bottom, cd alis2024 .

[PMR]        
Now do you have a text editor? Just Right, okay. This is going to be a bit messy.

[PMR]        
Let's make a new file here. So I'm going to have a new file. Say and simply

[Sravya]        
Okay.

[PMR]       
Yeah, make a new file. Oh, wait a minute. Can, you can edit it here.

[Sravya]        
Yes.

[PMR]        
Can you edit this file? Yes, I did edit that file.

[Sravya]        
This file. I mean.

[Sravya]        
I mean you want to, rename it? 

[PMR]        
No, just do any. Yes, okay. And now put in.

[PMR]        
Put in a new line. and put in let's put in a let's use alis so put in * opennotebook philosophy

[PMR]        
That's all right Okay. Now save that file.

[Sravya]        
Yeah, saved.

[PMR]        
Right, go back to your. Command line.

[PMR]        
And do git status.

[PMR]        
Right. So you've got a new file there, right? So you can now, do

[PMR]        
Git add..summary. Just copy the red thing.

[Sravya]        
Okay. This thing.

[PMR]        
Yeah, you should be able to cut and paste it. 

[PMR]        
Now do git Commit-am "summary_opennotebook"

[Sravya]        
Okay.

[PMR]        
Yep. And now, do, Git push.

[Sravya]        
Yeah.

[PMR]        
Right. This is the  st time you've done it, so you have to copy that thing in the middle.

[PMR]       
Between the blank lines git push Copy the whole of that into your paste buffer.

[Sravya]        
Okay.

[PMR]        
And then. That's it.

[PMR]        
Right, and you have now pushed this to the repository. And. What we're now going to do, is have a look at the, so you pushed it right.

[PMR]        
Now we are going to show how I pull it into my into my session. Right. So you stop stop sharing.

[Sravya]        
Yes.

[PMR]        
Okay. So I'm now in semantic climate.

[PMR]        
And now we should have Branch Sravya, okay?

[PMR]        
So let's have a look at that. You've got all sorts of things here, but in alis        .

[Sravya]        
Yeah.

[PMR]        
You should have.

[PMR]        
What was the file called?

[Sravya]        
Summary opennotebook.

[PMR]        
Yes, we've got that. Right, okay. And we got that there. Now.

[PMR]        
Let's have a look and see what I've got. So I, so. Mentally remember that.

[PMR]        
Actually what we can do is we can Open another window.

[PMR]        
And now I'm going to select my branch PMR One And. I'm going to, at your branch, put it up there.

[PMR]        
And I'm going to look at my branch here.

[PMR]        
Right, so you can see that my version is different from yours.

## MERGING TWO VERSIONS 

[PMR]        
Right, and that's perfectly okay. So you've got that in there. So. What I'm going to do now is I'm going to merge.

[Sravya]        
Yes.

[PMR]        
Your version into mine. At least I hope I am. And then I'm probably going to crash.

[PMR]        
So I'll do this on the command line, I hope.

[PMR]        
cd alis    

[PMR]        
I'm going to get pull. You should always do that. And that actually pulls the whole repository.

[PMR]        
So you can see here that it tells me there's a new branch.

[Sravya]        
Yeah.

[PMR]        
Right, so what I'm going to do now is I'm going to Merge that branch in so This is on my machine. So this is on PMR one and this is on Sravya, so if I go to my thing here. I'm on PMR 

[PMR]        
So I'm not a going to say more.

[PMR]        
What's the file called?

[PMR]        
Summary.

[PMR]        
Okay, I'm going to Git merge and I'm going to go back and look up. How we doing?

[PMR]        
I'm going to check out yours and I'm going to merge it into PMR one. 

[PMR]        
That's git merged.

[PMR]        
Merge conflict so it didn't, it wasn't able to do it, right?

[PMR]       
So we will open the open notebook.

[PMR]        
Not quite sure. Why can't do that?

[PMR]        
And ought to do.

[PMR]       
I'll create my own one here.

[PMR]        
Let's see if it allows me to merge now.

[PMR]        
You can, you know, I don't want to frighten you about git, but, merging is at the limit as to what we can do.

[PMR]        
Right, you have an unfinished merge. These context must be resolved. This is the file.

[PMR]        
You and if I say merge. It now gives me a   way Version. So this is what we're going to end up with.

[PMR]        
This is what you've got and this is what I've got. So. Right, so I want to include yours.

[Sravya]       
Yes.

[PMR]        
So what I do is, there are   things you can either omit yours or you can omit this one.

[PMR]       
Or you can, sorry, you can either. Take your one or you can omit it.

[PMR]        
So we're going to take yours. And this is what we've got here.

[PMR]        
So we're going to say we're going to apply at the bottom. And now I hope that that is now going to allow me to git merge that

[PMR]        
Right, it's merged it. Okay, I'm now going to say git commit. I'm now going to git push.

[PMR]       
Right, so now let us go to git.

[PMR]        
Here is your file. On Sravya branch. If we go to PMR branch,

[PMR]         
And look at this. It's the same. So do you see that we have in incorporated your version into my question..

[Sravya]       
Yes, . Yeah.

[PMR]        
Right. Now. If I were giving a formal lecture I would have prepared that better. Do you see what I mean?

[PMR]         
But it's worked. So I don't want you to feel merging is a major problem. The main thing to do is to make sure that you frequently commit things because that will save things and you can always backtrack on them.

[PMR]         
And what we need to do now, and decide between the two of you is, that this is a really useful session on how to, use git to, maintain parallel branches and merge things.

[PMR]    
Okay.