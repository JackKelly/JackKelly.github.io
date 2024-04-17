---
title: "Using computing to fix climate change, part 2"
categories: [open climate fix, machine learning, climate change mitigation, software engineering]
---

Four years ago, I wrote a blog post on [Using computing to fix climate change](2019-10-03-using-computing-to-fix-climate-change). Since then, I've learnt a lot! So I thought I'd write a follow-on to that blog post. Compared to my old blog post, this new blog post is more philosophical, and less practical. So, if you want practical advice, then please check my previous blog post!

## Who is this blog post for?

This blog post is primarily aimed at software engineers who are not currently working on climate change mitigation, but would like to move their career towards actively working on climate mitigation. 

## Caveats

Even though I've been working on climate change mitigation for about fifteen years, I'm as confused as ever about how best to maximise impact on the climate! The more I work on climate change mitigation, the more difficult it seems! So I definitely don't claim to be able to give perfect advice about how best to maximise your climate impact!

## In an ideal world, work on stuff that you enjoy, and is useful to the world (independent of the anticipated climate impact)

In general, it's frustratingly hard to predict whether a specific project will reduce emissions at scale:

- Maybe your product simply won't work.
- Or, maybe your product will work perfectly, but no one uses it (perhaps because it doesn't solve users' most pressing problem, or because it's too expensive). 
- Or maybe your product works well, _and_ people love using it, but there's some other bottleneck (completely out of your control) that means that your excellent work doesn't impact the climate.
- Or, worst, maybe your product works well, and people use it, but it has some unexpected secondary effect which actually _increases_ emissions! (For example, see the [rebound effect](https://en.wikipedia.org/wiki/Rebound_effect_(conservation))).

Let me tell a sad story: Imagine you dedicate your life to a project that you _thought_ would reduce emissions. The _only_ reason you work on this project is because you desperately want to help reduce emissions, and you expected this project to reduce emissions. But you hate the work. And you don't have any time to see your friends and family. After ten years, you reluctantly come to the conclusion that your work isn't helping the climate, either. That's not the end of the world: you've learnt a lot. But you feel pretty burnt out. And you can't shake the feeling that you've wasted the last decade of your (finite) life.

If you're at the beginning of your "climate journey" then you probably want to avoid this scenario! So, in an ideal world, I’d recommend working on stuff which has the following properties, _independent of whether you expect that work to impact the climate_:

Try to work on stuff that:

1. You _enjoy_: Specifically, stuff that you find intellectually stimulating, satisfying, and which has a friendly community, and pays you enough! (Of course, you can't expect to enjoy every minute of the job: all jobs have difficult and/or frustrating periods.)
2. Is useful to the world, even if it fails to help fix climate change.

## Building things is relatively easy. It's much harder to figure out which problem to work on!

In many ways, it's never been easier to lash together a technical demo that appears to prove some principle. And, as technologists, it's all too easy to get over-excited about the _tech_, and to loose sight of what users need! (I've certainly done this!)

One of the hardest problems is figuring out which problem to work on!

This sounds like I'm about to sing the praises of "agile" software development. But I'm actually pretty sceptical of agile software development (but this blog post isn't the right place for that particular rant!)

The perfect scenario, in my opinion, is to get extensive, _first-hand experience_ of a problem before you try to solve that problem. Then _you're_ the first user _and_ the developer.

(To get very pretentious and controversial for a second: In some ways I think about software engineering in the same way that I think about art. My hypothesis is that the best art is produced by people who create stuff that they're passionate about, and which scratches _their own_ creative itch. They pour their soul into the work. But they don't over-obsess about whether _other_ people will love the work (because we can never know other peoples' minds as well as we know our own). Good artists have a strong vision, and they're brutally honest with themselves, and they have the time and energy to repeatedly re-do work that they're not happy with. If you're self-aware, then you'll get a much stronger "signal" from your own critical assessment of your work than you'll ever get from other people. "Successful" artists are ones whose tastes happen - almost by chance - to align with other peoples' tastes. In contrast, a great way to make mediocre art is to do something that doesn't inspire you, but instead you're just doing because you _think_ other people will like. I think one of the great tragedies of modern software engineering is that we've forgotten that it's a deeply creative endeavour, and we've tried - mistakenly - to turn it into a mechanical process.)

So, to return(!) to concrete advice:

1. I _highly_ recommend spending as much time as you can "at the coal face". For example, if you want to help make the electricity grid more efficient, then spend a year or more working at (or consulting for) an electricity company. You'll gain invaluable experience of the _real_ problems that the grid faces, and you'll make a tonne of contacts. And, hopefully, you'll find yourself thinking "gosh, this process is insanely inefficient... Life would be so much easier if I had _x_". And _then_ you can go and build _x_!
2. Talk to as many people in your target industry as possible. Email folks. Go to as many in-person conferences and workshops as possible.

## Wait. Isn't generative AI going to make programmers obsolete in six months?

No, programmers won't be obsolete in six months :)

Beyond that, I can't predict what will happen with any confidence!

My hunch is that generative AI will increasingly be used for "junior" coding tasks (e.g. adding a simple feature to an existing codebase). My hunch (or naive hope?!) is that there will continue to be, for at least the next few years, the need for people who excel at programming, and/or people who can _design_ large systems (taking into consideration feedback from users, and considerations about how best to maintain the software for years to come, etc.). (I really like TJ DeVries' recent YouTube video "[Is it still worth it to learn to code? (I think so)](https://www.youtube.com/watch?v=JMK_30jeGww)").

If you're excited about diving deep into coding, and you love understanding "how things work", and you want to build stuff that's never been built before, then I'm fairly confident that it's still sensible to pursue a career in programming. In fact, in some ways it's never been a _better_ time to be a programmer, because generative AI helps reduce some of the tedium of coding (writing boiler-plate!)!

If, on the other hand, you're not especially curious about programming, and/or you imagine that most of your programming career will be spent copying-and-pasting code from StackOverflow because you're building something that's a tiny variation on something that's been built a thousand times before, then it might be best to consider an alternative career! Generative AI will probably excel at pumping out customised versions of things that have been built many times before.

If you want to be an engineer (but not necessarily a _software_ engineer) then it might be worth considering a more "physical" engineering career. I really am out of my depth here, but I'd guess that AI is particularly well-suited to _coding_ because there's a tonne of code on the web, and because it's fast and easy to check if code technically "works" (so AI can learn to code through "self-play"), and because AI researchers are also coders. Jobs in mechanical engineering, electrical engineering, etc., _might_ be less likely to be made redundant by AI.

## Avoiding the hype

In some ways, it might actually be _harder_ today to find jobs that will benefit the climate, compared to a few years ago. That's because a _lot_ of jobs and companies _claim_ to benefit the climate. But a lot of this is just noise. It turns out that the main trick to attracting funding is to tell a good _story_, and to hype up your company as much as possible. Unfortunately, the climate system doesn't work like most funders. The climate system doesn't care about how many YouTube reaction videos your product launch gets, or how bold your claims in your pitch-deck.

I'm honestly not sure how best to avoid this trap.

Some red flags mights be things like the boss of a "climate company" driving a fuel-guzzling sports car. Or the company regularly flying the team to events, even though it'd only take a few hours to do the same journey by train.

## The importance of this work

Most of this blog post has been rather down-beat!

I need to end on a more encouraging note!

I still totally believe what I wrote in 2019:

> Good luck! It’s gonna be tough. But we can’t fail. To paraphrase Greta: If we fail, future generations will never forgive us. (Sorry to be so gloomy!)
>
> But it’s also technically exciting work (and actually quite good fun!) and there’s a great community of people using computer science to mitigate climate change! So, dive in - we need your help!

