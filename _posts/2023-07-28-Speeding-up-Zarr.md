---
title: "Helping to speed up Zarr"
categories: [open climate fix, machine learning, software engineering]
---

TL;DR: To enable many more people to train machine learning models on large, dense, multidimensional datasets (like weather and satellite datasets), I'm planning to dedicate 4 days a week (starting in September) to helping to speed up [Zarr](https://zarr.dev). This blog post describes my motivations for helping to speed up Zarr. And goes into a little detail on _how_ I hope to speed up Zarr.

My ultimate goal remains the same as it's been for the last few years: To help to mitigate climate change by substantially improving energy forecasting. Crucially, the goal is to help as many organisations as possible: To help _other_ people who forecast renewable energy generation (because that's the fastest way to climate impact).

This is a long-game. We need to lay some important foundations first. The idea is to take a "big swing": and for me to be laser-focused on this work for the next few years. As such, starting in September, my aim is to spend 4 days a week writing code to lay these foundations.

I'm more excited than ever about applying cutting-edge machine learning (especially [transformers](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))) to energy forecasting. The tools & data exist to do incredible things. I think the results could be really impressive. I want to move beyond ML models which "just" convert numerical weather predictions to power. I want to train ML models which learn atmospheric physics (like [MetNet-3](https://arxiv.org/abs/2306.06079) from Google) from the data and, crucially, learn to use the large amount of real-time data that's available from sensors on the ground (such as solar systems). What does it take to do that? Training on enormous numbers of training examples, as fast as possible! (As well as many other requirements!)

Let's take a step back and ask what has enabled the recent and very dramatic improvement in large language models (LLMs) (such as [OpenAI's GPT-4](https://en.wikipedia.org/wiki/GPT-4))?

One thing that enabled LLMs to make a huge leap forwards is the ability to train efficiently on enormous quantities of text. It'd be great to do the same for the weather. Weather observations are represented as multidimensional datasets, and to train models effectively we need to be able to sample freely and quickly from these multidimensional datasets (without spending a fortune!)

At their core, LLMs are transformers. Arguably, one of the main advantages that transformers have over previous sequence-to-sequence models is that transformers can be trained _very_ efficiently on a significant proportion of all the text on the Internet. (Recurrent neural networks (RNNs), in contrast, are slow to train on GPUs). OpenAI put an enormous amount of engineering effort into getting data quickly into GPT-4 during training, and on developing huge datasets (including some synthetic data).


### The challenge of sampling from multidimensional datasets

To train our solar-forecasting ML models, we need to sample arbitrary slices from large multidimensional datasets. For example, each ML training example might consist of a "slice" of satellite data that consists of 4 timesteps, 128 pixels high x 128 pixel wides, and 10 spectral channels. Each "slice" is sampled from a random location from the entire dataset, which might be on the order of 100 TBytes in size.

If there's no rush, then reading these "random slices" is perfectly do-able with existing tools. The challenge we face is that we need to read these random slices _really_ quickly in order to keep the GPU fed with data during ML training. In practice, we find that we need to load data at a few gigabytes per second (per machine) in order to keep the GPUs fed.

Unfortunately, sampling quickly from multidimensional arrays is harder than sampling quickly from text. The fundamental challenge with multidimensional arrays is that computer data storage systems (RAM, spinning disks, SSDs, etc.) all store data as a 1-dimensional sequence of bytes. Which is a great fit for text (which is also 1D). But not such a great fit for multidimensional arrays.

To store a multidimensional array in a computer, the array has to be "serialised" into a 1D sequence of bytes. But, once the elements are in 1D, elements which _were_ close together in _n_ dimensions may now be a long distance apart on disk. This is a problem because most computer storage systems perform best when data is read _sequentially_ (rather than sparsely). And, to make matters worse, if you compress the data on disk then it's no longer obvious where each element of the array lives on disk. The end result is that reading a single multidimensional slice (which is contiguous in _n_ dimensions) may require many sparse reads from disk. And sparse reads tend to be slow (to be more specific: sparse reads will always be slow from HDDs because it takes time for the HDD's read-head to move to a new location. SSDs, in contrast, can read from random locations very quickly, but only if the SSD is given a very long list of random reads at once, so it can fully saturate its internal parallel data paths).

The solution that many people use is to break their dataset into multidimensional chunks, compress each chunk individually, and store those chunks on disk. This is what Zarr does (and TileDB, and c-blosc2, and others). Then we read entire chunks from disk (which is fast because each chunk should be stored sequentially on disk). Now the issue is that, to minimise the amount of "wasted" data read when the requested slice doesn't precisely match the size of the chunks on disk, we want the chunks to be as small as possible. But that, again, requires very high performance for random reads.

Since OCF's beginning in 2019, we've been using Zarr-Python to store almost all of our data. Zarr-Python is a great tool! But it's not especially well-tuned for loading data into ML models during training because Zarr-Python is not particularly fast (yet!). In OCF, we've tried lots of complicated work-arounds to allow us to load data into our ML models fast enough, but all these workarounds have serious limitations (for example, pre-preparing training batches is an obvious solution, but it takes many days to pre-prepare the batches, which is a surprisingly large drag on the rate at which we can try new experiments. And, of course, it takes up a lot of storage space, which in turn limits us to train on a relatively small set of batches.)

While the rest of the OCF team will still be working on the same great ML research which has allowed us to keep pushing the boundaries of forecast performance over the last 18 months, I will be spending most of my time forging ahead with this longer arc problem. 

My plan is to spend 4 days a week for up to a few years laser-focused on implementing this plan, and one day a week working with the OCF team on the current models and plans.


### Speeding up reading arbitrary slices from multidimensional datasets

It's _possible_ that there are existing tools which will do what we need. So - after discussion with the lead author of [TensorStore](https://google.github.io/tensorstore/) and other folks in the Zarr community - my first task is to benchmark existing implementations of Zarr. The benchmarking code will be open-source, and I plan to write a detailed blog about the results. I'll selfishly focus on my main use-case: reading random crops of lightly compressed multidimensional data from a local SSD, using Linux (mimicking what our ML training code does).

If the benchmarking suggests that no existing tool fully saturates IO for our use-case, then we can probably conclude that we've identified a bit of a gap in the existing tooling: It's currently hard to cheaply read random slices from multidimensional datasets at the speed required to train ML models (multiple gigabytes per second). This is a problem for multiple domains. For example, neuroscientists are busy building petabyte-scale 3D imagery datasets (by slicing brains very thinly, and scanning those slices at very high resolution). Climate scientists have been using enormous multidimensional datasets for years.

My hope is that we can enable many more people to do this sort of work by building a super-performant Zarr library (or perhaps by re-implementing just Zarr-Python's performance bottlenecks). Being able to sample freely from training data would have multiple benefits for OCF and hopefully the climate: We'd be able to generate _trillions_ of examples on-the-fly, using much simpler data processing code, and without having to pre-prepare batches. To put this another way: We'd be able to train our models faster, on more examples, and we'd be able to test new ideas much faster. And these benefits would apply for any project that requires large multidimensional datasets (not _just_ solar forecasting).

To quote a comment on a draft version of this blog post from [Stephan Hoyer](http://stephanhoyer.com/) (research lead at Google, and the creator of [Xarray](https://github.com/pydata/xarray)):


> "The advantage of a fast Zarr reading is that you can do more preprocessing of data on the fly with minimal performance consequences (e.g., choice of variables and/or time slicing), and you don't necessarily need to store duplicated shuffled copies of your data…
>
>
> There are also two other big advantages of fast random access to Zarr in my opinion:
>
>
> 1. Preserving metadata. It's much easier to debug bad interactions between models and data when you have the full metadata to identify where each bit of data came from, rather than just knowing that it's a "random batch."
> 2. Reproducible & deterministic training. For debugging purposes, it's invaluable to have deterministic training scripts. This can get tricky when combined when using cloud infrastructure that may be pre-empted at any time. It's way easier to write pre-emption robust code if you can quickly index into arbitrary locations in the training data, with indices that only depend on the training step number."

There's a "democratisation" argument too: A fast Zarr library should make it easier for more people to experiment with training ML models on multidimensional datasets.

And, at OCF, we've always wanted to contribute open-source tools that help lots of people. (Personally, I feel we actually have a moral obligation to contribute back to the open-source community, given how much open-source code we use!)

So, my proposal is that I build a new Zarr reader, which is heavily optimised for read-speed (by implementing in the Rust programming language, and using tools like [tokio](https://tokio.rs/) and [io_uring](https://news.ycombinator.com/item?id=23133040) for asynchronous IO). The basic idea is to build something that is as efficient as possible at using the hardware, whilst also exposing two simple Python APIs: one which mimics the existing Zarr-Python API (to make it as easy as possible for folks to use the new code), and a new async Python API. Or, perhaps, it will be sufficient "just" to re-implement parts of Zarr-Python in Rust. I will also get much more involved in the Zarr community. (See the [Appendix](#appendix) for more details, and a brief discussion of other Zarr implementations)


### Timeline

It'll be a while before anything concrete happens. I need to finish off some stuff at OCF. And then I need to get better at Rust :). And I'm on a family holiday for 3 weeks in Aug. But hopefully, from about September onwards, I'll be able to spend about 4 days a week on Zarr-Rust. Then, after I get a functional MVP of Zarr-Rust running, I'll probably transition to spending about half my time on ML, and half on Zarr-Rust. I honestly have no idea how long this will take, but I'd estimate that it'll take something like a year to get an MVP Zarr-Rust up-and-running. (Please see the section on [When will we know if this approach is worth pursuing?](#mvp) in the Appendix for more discussion of what counts as the MVP).

But please shout if you think this is no longer necessary! Or if you have any feedback at all!

And, of course, I'd do everything in the open, and discuss as much as possible with the Zarr community.


## <a name="appendix"></a>Appendix


### Tell me more about this "super-performant library for reading Zarr"!

The idea is to write a new Zarr library in Rust. With Python bindings. The idea would be to expose two Python APIs: one which is as similar to zarr-python's API as possible (to enable folks to use zarr-rust without changing any of their code); and another API that is fully async.

Crucial to this project will be building Zarr-Rust out-in-the-open, and in collaboration with the wonderful existing Zarr community!

The use-case I have in mind would involve trying to read & decompress thousands of small chunks per second (and maybe orders of magnitude more). Those small chunks would live on disk in shards.

[Zarr's sharding proposal](https://zarr.dev/zeps/draft/ZEP0002.html) changes the "Zarr paradigm" from reading a small number of large chunks to a large number of small chunks. This fundamentally changes the data access pattern. It becomes much more important to have performant async IO. We might want to read on the order of a _million_ chunks per second.


### What makes you think that it's possible to go faster than existing Zarr implementations?

I must admit that I can't be _certain_ that it's possible to go any faster.

That said, there are a few theoretical reasons to believe that it _might_ be possible to go faster. (But - all too often - theoretical benefits don't necessarily materialise!):

* I don't think any existing Zarr implementation uses [io_uring](https://news.ycombinator.com/item?id=23133040) (a newish feature of the Linux kernel that allows for async IO - including file operations and network operations - without any memory copying, and with minimal system calls). [Some database folks](https://www.scylladb.com/2020/05/05/how-io_uring-and-ebpf-will-revolutionize-programming-in-linux/) seem pretty excited about io_uring. [Some benchmarks](https://www.phoronix.com/news/Linux-5.6-IO-uring-Tests) show that io_uring can deliver almost 20x more IOPs for random reads than the previous approach.
* Zarr-Python is entirely single-threaded. Some other Zarr implementations use thread pools. But I believe that, theoretically, an async runtime like [tokio](https://tokio.rs/) (with a work-stealing scheduler) should be able to process more tasks per second, with less CPU & memory overhead. OS threads are surprisingly expensive: both in terms of RAM, and the cost of context switching. If we are serious about reading and decompressing a million chunks per second, then it would be madness to try to spawn a million OS threads! Or course, tokio uses threads under the hood. But it's at least possible that tokio will use threads more effectively than a hand-crafted scheduler.
* I'm also interested in doing some processing (downsampling, normalisation, etc.) on each chunk, in parallel, whilst the chunk is still in the CPU's cache after decompression (like [c-blosc2](https://github.com/Blosc/c-blosc2)). But I think [TensorStore already does that](https://github.com/google/tensorstore/blob/0eee84336eb33ada9dc9e546072221a597678380/tensorstore/downsample.h#L48).


### Fast, async file IO for huge numbers of files per second is useful beyond Zarr

Zarr isn't the only thing around that could benefit from fast, async file IO for huge numbers of files per second. So I may actually write _two_ Rust crates: a general purpose, high-performance library for async file IO operating concurrently on huge numbers of files (or chunks of files). And a "Zarr front-end".

The IO library would use all the CPU cores to saturate the disk / network interface card, and may use different strategies depending on the performance characteristics of the storage medium. And perhaps the Rust IO package would optionally decompress each chunk, and glue the resulting chunks together into a single array, ready for passing back to Python land.

In a sense, this would be a bit like [fsspec](https://filesystem-spec.readthedocs.io/en/latest/) (and would owe a lot to fsspec!), in that the Rust IO library would provide a common interface to local disks and cloud object storage, and the IO library wouldn't be specific to Zarr. But, unlike fsspec, this library would be laser-focused on high performance async IO for huge numbers of files (or parts of files) at once. And might include multi-core compression / decompression, and glueing the chunks together into a single array.

And this "high speed IO library" would also be useful as the "backend" for a new high-performance tool for reading huge numbers of GRIB files or EUMETSAT .nat files. So we could convert from GRIB and .nat files to Zarr as efficiently as possible.


### <a name="mvp"></a>When will we know if this approach is worth pursuing?

In general, I'm interested in exploiting platform-specific performance features (like io_uring in Linux). I'd plan to start with a proof of concept that only works on Linux, and only knows how to read from local files.

If it's not possible to go faster than TensorStore by "cheating" (using platform-specific features) then I'll give up :) (and that's fine - I will have benefitted from learning Rust, and from gaining much more hands-on experience with how Zarr behaves. So it wouldn't have been a waste of time.). If it looks promising then I'd add the ability to read from cloud buckets (maybe also using io_uring for network IO). And then extend to other operating systems.
