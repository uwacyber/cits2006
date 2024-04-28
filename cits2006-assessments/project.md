# Project
In this project, you will be working as a group to perform defensive cybersecurity techniques. 
Please note, you are expected to conduct further research to learn more about various defensive cybersecurity techniques and use them in this project.

More details are as follows.

{% hint style="warning" %}
The standard UWA late penalty applies to ALL members if you defer your group deliverable/demo (i.e., -5% per day from raw marks for 7 days, then 0).
{% endhint %}

## Pretask: Group forming (week 8)

This project is to be carried out as a group.

You are to form your own group, but your group must meet the following requirements:

* The group's average grade from LQ1 must not exceed 73 (i.e., add all LQ marks then divide by the number of members). If you don't want to reveal your marks, you can employ multiparty encryption, or as a last resort you can form the group first and contact me to check whether your group meets this eligibility or not.

The number of members should be 5 (4 or 6 may be considered - requires approval).

{% hint style="info" %}
If the group's average grade is higher than 73, and you cannot find an appropriate group, you should contact me. I will either allocate you to a different group or allow an exemption. You are encouraged to find group members at the labs and using MS Teams. The only time I will allocate you to a group is if your currently formed group's average grade is higher than 73.
{% endhint %}

Once the group has been formed, go to MS Teams -> Project Discussion, and there is the "CITS2006 Project Groups" tab. There is a "Group details" tab, where you enter your group details (group name, group leader (main contact) and members' student IDs). The group leader will also contact me to confirm the group formation. Once confirmed, you may start with Task 1 below.

Please note that you are required to submit an individual report, so you should also be keeping records of individual contributions so that individual assessment components can be evaluated later. Please note that this doesn't mean you are competing with your group members, but instead, a chance to demonstrate your own skills and contributions to the project.

Complete Task 0 Group forming by end of week 8 (i.e., by Friday 26 April).


## Main Task: Configure security solutions as per requirements (Week 9-11)

Your group is formed of renowned cybersecurity experts hired to provide security solutions to the RapidoBank (RBa) filesystem. You can setup the filesystem like a server of your choice of OS. There were several features requested by the RBa CEO Monte:

* Customised Yara engine to detect improper files in their filesystems.
* Customised cipher system and hashing algorithm to protect their files.
* Customised Moving Target Defence (MTD) to change protection settings.
* Customised security recommendations to improve their data security when attacks are detected.

How each of these security features operate is up to your group. However, consider usability, effectiveness and practicality when implementing these features and how they would operate in your implementation.

### Yara engine
Your Yara engine must be able to do the following:

1. Detect malware in the filesystem.
2. Detect hidden files containing sensitive information (i.e., files were not encrypted but hidden by user(s) by mistake).
3. Detect scripts.
4. Detect executables accessing network resources.
5. Detect malicious URLs an executable file is trying to access.
6. Detect custom signatures (e.g., a specific string or pattern) you might find in the filesystem.

How you define each of these requirement is up to your group, but to get high marks, they must be comprehensive, reasonable and practical. You can use the Yara rules provided in the labs as a starting point, but you are expected to create your own rules to detect these files, as well as do further research to make them comprehensive. Make sure to prepare examples to demonstrate the above features.

### Cipher system and hashing algorithm
The cipher system is used to encrypt sensitive files in the RBa filesystem. To confuse the attackers, multiple cipher systems are used randomly (see later MTD how it can change the cipher system). The length of the cipher key should be 50 characters long. You must NOT use any cryptography libraries for this task. You don't have to build a commercial-grade cipher system for this task, but ensure that the cipher system is functional. 

The hashing algorithm is used to hash the files in the filesystem to detect any changes made to the files. The length of the hash should be 50 characters long. You must NOT use any cryptography libraries for this task. You should consider the hash algorithm's properties, such as one-way, collision-free (see lab 1 for a refresher), and other properties that make it suitable for this task.

Make sure you have a discussion about the cipher system and hashing algorithm you are implementing, and provide justifications for your choices. You should also provide examples to demonstrate how the cipher system and hashing algorithm work.

### Moving Target Defence (MTD)
Implement a Moving Target Defence (MTD) system to change protection settings. This could be a system that changes the encryption key, the hashing algorithm, or the cipher system used to encrypt the files. The MTD system should be able to change the protection settings based on the following:

* an alert has been raised by the Yara engine.
* a file has been added/modified/deleted in the filesystem.
* a certain time interval has passed.

The actual MTD you implement is up to your group, but make sure to provide valid justifications and analysis on why you chose the MTD system you implemented. You should also provide examples to demonstrate how the MTD system works.

### Security recommendations
Regular security recommendations are generated based on the information collected from the security features above. How and what security recommendations are to be generated will be up to your group, but they must be relevant to the security information provided from the above security features (i.e., cannot be generic, repetitive, etc.).


### Main task todo:

1. Complete all security feature implementations.
2. By Friday 5pm of week 11, your group leader must submit the group report on LMS outlining the implementation of the security features. This report will be used during the live demo as a guideline for the marker, and any new security features/implementations not in the report will not be counted toward the grade. 
3. You must also submit your individual report on LMS (by Friday 5pm of week 11). This should outline your contribution to the group project clearly and concisely. Remember, quality over quantity.
4. The group leader must schedule your demo slot from the available slots provided on MS Teams -> Project Discussion -> CITS2006 Project Groups -> Demo booking (week 12).

{% hint style="warning" %}
DON'T do everything yourself. This is not a race among the group members. If you read the rubric on individual reports, the marks are based on your ability to demonstrate defensive cybersecurity skills, which means QUALITY over QUANTITY (i.e., you don't have to get full marks in other tasks to receive full marks for your individual report).

What does "Quality" mean? In the context of this project, it means that you are able to not only demonstrate skills you have learned in the unit, but have also researched and applied more advanced skills derived from further research into the topic. That is, you are expected to conduct further research to learn more about various defensive cybersecurity techniques and use them in this project.

Of course, you will need to meet all requirements to receive marks for other tasks, which means your contributions may vary (i.e., you might have to cover for other members if needed).
{% endhint %}


## Demonstration: Live Demo of the Configured Layered Defence (Week 12)

Your group will demonstrate your layered security implementation during the scheduled lab. All members are expected to attend the scheduled session, and be able to demonstrate the contributed portion of the implementations as required (however, how you perform demonstration is up to the group i.e., a single presenter could perform the demo if it seems more appropriate).

### **Demonstration preparation:**
1. The group leader must book the group demonstration slot on the MS Teams -> Project Discussion -> CITS2006 Project Groups -> Demo booking (week 12).
2. Ensure all group members can attend the session.
3. Ensure the group report is submitted by the due date (Friday 5 pm of week 11).
4. Ensure the individual report is submitted by the due date (Friday 5 pm of week 11).
5. The demo should demonstrate the functionality of defence features implemented.


{% hint style="info" %}
The live demo will be no longer than 30 mins, you should aim it to be around 20 mins demonstration and 10 mins for Q&A.
{% endhint %}



## Marking Rubrics

<table>
    <thead>
        <tr>
            <th width="200">Component</th>
            <th width="100">Weight</th>
            <th width="200">N</th>
            <th width="200">P</th>
            <th width="200">CR</th>
            <th width="200">D</th>
            <th width="200">HD</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Configuring a layered defence (report)</td>
            <td>50%</td>
            <td>(1) Attempts were made, but none of the security features are functional.<br><br>(2) Report is not aligned with the demo and difficult to comprehend.</td>
            <td>(1) Implemented almost all security features outlined and functional with reasonable justifications and discussions provided.<br><br>(2) Report aligns with the demo but is lacking details and legibility.</td>
            <td>(1) Implemented almost all security features outlined, fully functional with detailed justification and discussions.<br><br>(2) Report aligns with the demo with full details in well formatted document.</td>
            <td>(1) Implemented all security features outlined, reflecting research with comprehensive details in implementations.<br><br>(2) Report aligns with the demo and is professionally formatted.</td>
            <td>(1) Implemented all security features outlined, with state-of-the-art or high specifications of the security details applied.<br><br>(2) Report aligns with the demo and is formatted professionally. Explanations are concise and easily understood, using various visual techniques to support the explanations and discussions.</td>
        </tr>
        <tr>
            <td>Demonstration</td>
            <td>20%</td>
            <td>(1) Demo failed to demonstrate the implemented security features.<br><br>(2) Group did not answer the questions sufficiently.</td>
            <td>(1) Demo demonstrated the functionality of security features.<br><br>(2) Group answered the questions but failed to provide sufficient details or reasonings.</td>
            <td>(1) Demo demonstrated the functionality of security features clearly.<br><br>(2) Group answered the questions with sufficient details and reasonings.</td>
            <td>(1) Demo demonstrated the functionality of security features clearly and comprehensively.<br><br>(2) Group answered the questions with sufficient details and reasonings.</td>
            <td>(1) Demo demonstrated the functionality of security features clearly and professionally.<br><br>(2) Group answered the questions precisely with technical reasoning and justifications.</td>
        </tr>
        <tr>
            <td>Individual report</td>
            <td>30%</td>
            <td>No or nearly none evidence of contributions made to the project.</td>
            <td>(1) Made some contribution to the project, demonstrating some defensive cybersecurity skills.<br><br>(2) Shows some indication of research done, exploring new defensive cybersecurity skills not covered in the class.</td>
            <td>(1) Made some key contributions to the project, demonstrating a variety of defensive cybersecurity skills.<br><br>(2) Shows a reasonable amount of research done, exploring new defensive cybersecurity skills not covered in the class.</td>
            <td>(1) Made major contributions in the project, demonstrating a variety of defensive cybersecurity skills.<br><br>(2) Shows a high level of research done, exploring new and advanced defensive cybersecurity skills not covered in the class.</td>
            <td>(1) Made major contributions in the project, demonstrating advanced defensive cybersecurity skills.<br><br>(2) Shows a comprehensive level of research done, exploring new and advanced defensive cybersecurity skills not covered in the class.</td>
        </tr>
    </tbody>
</table>





