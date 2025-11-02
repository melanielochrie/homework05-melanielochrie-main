# Homework 05 Report

1. What does the `in` operator do? Provide examples of the `in` using strings and lists (or tuples). 
    
    The in operator checks whether a value exists inside another object, like a string, list, or tuple. It returns a Boolean value( True or False). 
   
2. Taking a moment to research, why would one want to use .casefold() instead of .lower() in python when comparing strings? Please include the reference on where you find the information.
   
   According to w3schools, it is better to use .casefold() instead of .lower() because .casefold() is more aggressive and handles more types of characters when comparing strings in Python. The .lower() method only works well for basic English letters, but .casefold() works with special or accented letters too. 
   
   Reference: https://www.w3schools.com/python/ref_string_casefold.asp

3. For each of the three sequential types you have learned (list, string, tuple) - label as mutable or immutable (refer to the team activity).
   * string - immutable 
   * list - mutable
   * tuple - immutable

4. Explain mutability and immutability in your own words.
    
    Mutability means that something can be changed after it has been created. Immutability means that once it has been created, it cannot be changed. 

5. Given the following code:

    ```python
    def mystery_function(x):
        x = 100

    x = 1
    print(x)
    mystery_function(x)
    print(x)
    ```

* What is the output of the code above?
  
    ```
    1
    1
    ```
* Explain why the output is what it is.

    The first print(x) shows 1 because x=1 before the function was called. Inside the mystery_function(x) the line x = 100 only changes the local version of x that exists inside the function. It doesn't affect the x outside of it. 

1. Given the following code:

    ```python
    def mystery_function(x):
        x[0] = 100

    x = [1, 2, 3]
    print(x)
    mystery_function(x)
    print(x)
    ```
* What is the output of the code above? 
    ```
    [1, 2, 3]
    [100, 2, 3]
    ```
* Explain why the output is what it is.

    During the first run, x is a list [1, 2, 3]. The first print(x) shows that list. Then, when mystery_function(x) is called. Inside the function, the code x[0] = 100 changes the first value in the list to 100. This is because lists are mutable. 

1. Would happen if `x` was a tuple? What is generated when you try to run the code above with a tuple?

    ```
    TypeError: 'tuple' object does not support item assignment

    ```


8. Given the following code:

    ```python
    def mystery_function(x):
        x[1][0] = 100

    x = (3, [1, 2, 3], [4, 5, 6])
    print(x)
    mystery_function(x)
    print(x)
    ```

* What is the output of the code above?
    ```
    (3, [1, 2, 3], [4, 5, 6])
    (3, [100, 2, 3], [4, 5, 6])
    ```
    
## Deeper Thinking

We talked a lot about immutable and mutable. Why would this matter? Take a moment to describe in your own words why computers would care. Pay particular attention to how computers store data in memory, and how making something immutable may help with that storage.
---
Mutability matters because it affects how data is stored and handled in memory. When something is mutable, like a list, Python has to keep track of where it is stored so it can be changed later. That means the same list can be updated without created a new copy each time. 
When something is immutable, Python stores it in a fixed way. Meaning, if you try to change it, Python makes a brand-new object in memory instead of editing the old. one. This is matters becase it makes immutable objects safer to use because you know they can't be accidentally changed in a program. It also helps manage memory efficiently within Python because it can reuse the same value in multiple places without making copies. 

---

### Software Engineering Exploration and Reflection (Deeper Thinking Part 2)

As someone learning about software engineering and application development, you need to understand the real-world complexities and challenges that professional developers face when building large-scale applications. This assignment will help you explore the field and reflect on what it means to work in software development.


Find three different sources that discuss major complications, failures, or challenges in building real-world applications. Look for diverse perspectives - perhaps a case study of a software failure, a technical blog post from an engineering team discussing lessons learned, or an industry report on development challenges. Very are a fair number of blogs on switching from one language to another, and why that was selected. Your sources should come from credible places like engineering blogs, tech publications, academic sources, or documented case studies.

After reading your sources, write a reflective response (3 paragraphs, approximately 150-200 words each) that explores:

- What surprised you most about the challenges these applications faced? What complications did you not expect, and how do these real-world problems differ from what you might encounter in coursework or small personal projects?

- Based on your research, how do you now view the role of a software engineer? What skills beyond coding seem most important, and what aspects of the job appear most challenging or rewarding?

- How does this research influence your understanding of software development as a career field? What areas would you want to learn more about, and what questions do you still have about working in application development?

This is a personal reflection meant to help you think more deeply about the software engineering field. Focus on your genuine reactions and insights rather than trying to provide "correct" answers. Include mentions of your sources, but the emphasis should be on your own thinking and learning process. Make sure to link your sources, and write your reflection below. 

---
After reading about real-world software engineering challenges, I was most surprised by how small oversights can lead to huge financial or system failures. The CIO article on the Knight Capital fiasco described how one untested software deployment caused the company to lose $440 million in less than an hour. I did not expect such a simple error of missing a test procedure to have that level of impact. This helped me realize how different real-world development is from classroom assignments. In my assignments, a bug might just crash a small program rather than an entire company. The stakes are much higher and testing and documentation become essential for preventing disasters. 

Based on my research, I now view software engineers as responsible for far more than just writing code. The Investopedia article on Mt. Gox explained how weak security practices and poor data management led to the loss of hundreds of thousands of bitcoins. That failure showed how crucial it is for developers to think about security and reliability at every step. The Medium article about building engineering teams in startups also emphasized the human side of software engineering. The success of a project is affected by how leadership, communication, and teamwork comes together. Technical skills alone are not enough. 

This research deepened my understanding of software engineering as both a technical and organizational challenge. I can see now why large-scale systems require collaboration, strong testing, and careful planning. It also made me think about the kind of engineer I want to become. I want to become someone who not only writes functional code but also designs responsibly and anticipates risks. I am interested in learning more about cybersecurity and how secure coding practices can prevent data loss and protect users. Overall, this reflection helped me appreciate that software engineering isn't just about problem-solving with code, it is about ensuring reliability, safety, and teamwork in systems that affect real people. 

Sources: 
https://www.cio.com/article/286790/software-testing-lessons-learned-from-knight-capital-fiasco.html
https://www.investopedia.com/terms/m/mt-gox.asp
https://medium.com/better-programming/12-lessons-learned-while-building-a-successful-engineering-team-in-a-small-startup-7cdb4eb869b3