# Introduction to Labs

These labs are intended to provide a practical complement to the CITS2006 Penetration Testing unit. The materials are designed for you to complete individually, but you are welcome to work with your peers as well. However, please note that the lab quizzes are **individually assessed**, so it is essential that you fully understand the concepts and techniques covered in the labs to receive good marks.

As always, please contact the lab facilitator if you are stuck. We may use the UWA CSSE Help Server to submit your question ticket, so that questions can be answered in the order of requests. The details are outlined in the welcome lecture slide, but you can also ask the lab facilitator on site or via their emails or through MS Teams. If nothing works, please contact the UC explaining your issue.

## Laptop Requirement

This unit requires software that the University IT team can't install on the lab machines and so you will need to use your own laptop. This can be either Windows, Mac or Linux and instructions will be provided for those platforms as necessary. We will be running (often) two or more VMs at the same time, so it is advisable to get a laptop that has high core counts (minimum 4), additional RAM (minimum 16GB), and enough storage space (extra 50GB in addition to whatever you use already). Details for considerations are shown below.

If you do not have a laptop, it will make your life easier by getting one that meets the requirements specified in the above link.

You may also request a loan laptop from the student office. Please contact the Student Office to ask for more details: [studentwelfare-studserv@uwa.edu.au](mailto:studentwelfare-studserv@uwa.edu.au)

{% hint style="info" %}
It is essential that you reserve at least 10GB of additional disk space to store the lab files (e.g., docker images). You can free disk space by removing completed lab files later.
{% endhint %}


## Considerations when purchasing a laptop

### Operating system
This choice is critical. While most CSSE units can be successfully undertaken using a laptop running Windows, Linux, or macOS, Apple's macOS can only be (legally) run on Apple's hardware. Nearly all non-Apple laptops use an Intel or AMD processor, older Apple laptops use an Intel processor, and Apple laptops since 2020(ish) run an ARM-based Apple Silicon processors (M1, M2 etc.). It is possible to emulate Windows and Linux on Apple computers, but the performance differs due to significantly different architecture they run. Whether Windows is better than macOS, and whether Linux is better than them both, is almost a religious argument that won't be resolved here! Based on the CSSE course you're taking, investigate the recommended hardware and software for each unit. Geting through the degree, you should be fine with any of the OS.

### Screen size
Screen size obviously influences a laptop's overall size which, in turn, limits its portability and weight. While screen size matters little when sitting at a table, larger sizes affect your ability to work effectively on buses and trains. A 13-inch screen is considered a reasonable minimum, with a 15-inch screen being the sweet-spot. 17-inch and 19-inch behemoths are great for playing games, and anchoring large ships, but are far larger than required to complete CSSE assignments.

### Screen resolution
Screen resolution refers to the number of pixels (individual video elements) that provide the clarity of the text and images displayed on your screen. At higher resolutions, items appear sharper. The more pixels on your screen, the more information you can display, possibly enabling 3 or 4 non-overlapping windows. CSSE students love higher resolutions, enabling them to program in an IDE (integrated development environment), read documentation in a web-browser, execute their new graphical application under development, and plot data.

### Processor (CPU) speed
Historically, a CPU's clock frequency provided a good single-figure metric to describe a computer's performance. Today, as Moore's Law appears to be less relevant, the number of CPU cores (individual CPUs, often sharing some common memory) is a better measure of computer performance. A single CPU, no matter how fast, can only execute a single program at once, whereas a computer with N cores can execute N programs simultaneously. Today's laptops boast 4 or more cores, meaning you can watch a cat video, browse the web, read emails, listen to music, download the latest Linux distribution, send an instant message, and complete your CSSE assignments all at the same time! The recommended minimum is 4 cores, with 8 cores being a good size for most users.

### Memory (RAM) capacity
A computer's RAM holds the programs and data required by the CPU to execute applications. If RAM is limited, your whole system will run slower, or fewer applications will be able to run. Until 2020 it 'seemed obvious' that you could never have too much RAM, and laptop capacities approached 32GB. More recently, smarter design of the communication channels between CPU, RAM, and disk have enabled laptops to execute extremely fast with just 8GB of RAM (though 16GB is still better!). For the purpose of doing your CS degree, 16GB is a good minimum, with 32GB being a good size for most users.

Note: some manufacturers, notably Apple, do not support RAM upgrades - so choose the most RAM you can afford when purchasing.

### Storage (disk) capacity
By now, everyone should have SSD for their storage. If you have HDD, then it is time to consider upgrading your storage unit on your laptop. SSDs are faster, more reliable, and more power-efficient than HDDs. They are also more expensive, but the price has dropped significantly in recent years. A 256GB SSD is considered a minimum, with 512GB being a good size for most users. 1TB is a luxury, but if you can afford it, it is a good investment.

Note: some manufacturers, notably Apple, do not support SSD upgrades - so choose the largest SSD you can afford when purchasing.


| Consideration | Minimum | Good | Luxury |
| --- | --- | --- | --- |
| screen size | 13-inch | 15-inch | 16-inch |
| screen resolution | 1920x1080 | 2560x1600 | 3072x1920 (4K UHD) |
| CPU | 1.6GHz, 4 cores, i5 or M1 | 2.0GHz, 8 cores, i7 or M1 Pro | 2.5GHz, 12 cores, i9 or M1 Max |
| RAM | 8GB | 16GB | 32GB |
| Storage | 256GB SSD | 512GB SSD | 1TB SSD |
| GPU | Integrated | Integrated | Dedicated (RTX 4000/5000 series etc.) |

