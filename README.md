# Syllabus

1. [Description](#toc-description)
1. [Time & Location](#toc-time-location)
1. [Learning Objectives](#toc-learning-objectives)
1. [Outline](#toc-outline)
   1. [Introduction & Orga](#toc-week-0)
   1. [Git](#toc-week-1)
   1. [Ideation & Planning](#toc-week-2)
   1. [Design](#toc-week-3)
   1. [Architecture](#toc-week-4)
   1. [Documentation](#toc-week-5)
   1. [Agile](#toc-week-6)
   1. [Coding together](#toc-week-7)
   1. [Scientific Presentations](#toc-week-8)
   1. [Testing](#toc-week-10)
   1. [Retrospective](#toc-week-11)
   1. [Infrastructure](#toc-week-12)
   1. [Bug Bounty / Hackathon](#toc-week-13)
   1. [Security](#toc-week-14)
1. [Grades](#toc-grades)
1. [Books](#toc-books)
1. [Lectures](#toc-lectures)
1. [Office Hours](#toc-office-hours)
1. [Checks for Understanding](#toc-checks-for-understanding)
1. [Student Conference](#toc-student-conference)
1. [Final Project](#toc-final-project)
1. [Attendance](#toc-attendance)
1. [Academic Honesty](#toc-academic-honesty)
   1. [Reasonable](#toc-honesty-reasonable)
   1. [Not Reasonable](#toc-honesty-not-reasonable)
1. [This repository](#toc-this-repo)
   1. [Links in this repository](#toc-links)
   1. [Further resources](#toc-further-resources)

<a id="toc-description"></a>

## Description

This is AI1021, University of Fulda's introduction to project work in the realm of software development. This course teaches you how to work effectively with others to build awesome software. It's less about good individual coding skills and more about leveraging teamwork to achieve greater results than you would be able to on your own. This involves division of labor, coordination, discussing ideas, resolving conflicts and celebrating successes. We will examine how to get the software to users and which measures are recommended for a long-lasting project. There will also be a segment on the scientific method that shows you how to study and evaluate scientific sources to become an even more rational thinker.

<a id="toc-time-location"></a>

## Time & Location

This course ordinarily meets for a lecture and discussion session on campus on Tuesdays, 3:30pm–6:45pm. The room is specified in horstl. Students are expected to attend these meetings in person. A connection from remote locations is not supported.

<a id="toc-learning-objectives"></a>

## Learning Objectives

Among this course’s objectives are that you learn how to:

- manage and lead a project
- decompose a project into tasks
- plan your work
- monitor and document progress
- communicate outcomes succinctly and precisely
- use agile and classic project management tools
- think more methodically
- operate at multiple levels of abstraction
- separate design from implementation details
- assess the correctness, design, and style of code
- identify threats to privacy and security
- read documentation, drawing conclusions from specifications
- assure the quality of your software, find faults, and identify corner cases
- identify trade-offs among resources

<a id="toc-outline"></a>

## Outline

Outlined below is the course’s subject matter, organized by week, each subtitled per to the context in which its topics are introduced.

<a id="toc-week-0"></a>

### [Week 00 Introduction & Orga](/weeks/week-00.md)

Getting to know each other. Organizational matters. Idea pitches. Group composition.

<a id="toc-week-1"></a>

### [Week 01 Git](/weeks/week-01.md)

Version Control System. Trunk Based Development. Continuous Integration (CI). DORA metrics.

<a id="toc-week-2"></a>

### [Week 02 Ideation & Planning](/weeks/week-02.md)

Ideas. Features. Kanban. Prioritization. Wireframes. User Stories. Acceptance Criteria.

<a id="toc-week-3"></a>

### [Week 03 Design](/weeks/week-03.md)

UX. UI. Colors. Icons. Material Design.

<a id="toc-week-4"></a>

### [Week 04 Architecture](/weeks/week-04.md)

Components. Interfaces. Configuration. Decision Records. Model-View-Controller. Microservices. Events. Feature Toggles.

<a id="toc-week-5"></a>

### [Week 05 Documentation](/weeks/week-05.md)

README.md. CONTRIBUTING.md. OpenAPI. Swagger. Wikis. Diátaxis.

<a id="toc-week-6"></a>

### [Week 06 Agile](/weeks/week-06.md)

Agile Manifesto. Scrum Guide. Retrospective. Extreme Programming.

<a id="toc-week-7"></a>

### [Week 07 Coding together](/weeks/week-07.md)

Acceptance Criteria. Definition of Done. Definition of Ready. Code Review. Task Automation. Style guide.

<a id="toc-week-8"></a>

### [Week 08 Scientific Presentations (1/2)](/weeks/week-08-09.md)

Scientific Method. Peer Review.

<a id="toc-week-9"></a>

### [Week 09 Scientific Presentations (2/2)](/weeks/week-08-09.md)

Scientific Method. Peer Review.

<a id="toc-week-10"></a>

### [Week 10 Testing](/weeks/week-10.md)

Testing Pyramid. Unit Tests. Test Driven Development (TDD). Decoupling. Test Automation.

<a id="toc-week-11"></a>

### [Week 11 Retrospective](/weeks/week-11.md)

Team building. Team dynamics. Continuous Improvement.

<a id="toc-week-12"></a>

### [Week 12 Infrastructure](/weeks/week-12.md)

12 Factor App. Continuous Delivery (CD). Dependabot. GitHub actions. Docker. Logging. Monitoring. Service Level Agreement (SLA). Disaster Recovery Plan. Post Mortem. Cost Management. DevOps. Infrastructure as Code.

<a id="toc-week-13"></a>

### [Week 13 Hackathon](/weeks/week-13.md)

Bug Bounty.

<a id="toc-week-14"></a>

### [Week 14 Security](/weeks/week-14.md)

OWASP Top 10. Brute-Force Attacks. Two-Factor Authentication. Hashing. Rainbow Table. Salting. Cryptography. HTTPS. End-to-End Encryption. Deletion.

<a id="toc-week-15"></a>

### Week 15 Final Project Presentation

<a id="toc-grades"></a>

## Grades

This is a pass/fail course without grades.

You are expected to

- attend the weekly meetings
- present a (self-chosen) scientific paper on a computer science topic
- work regularly together as a team on a final project:
   - initial idea pitch
   - weekly updates
   - one retrospective
   - presentation of the project in the last session

You must meet all expectations in order to be eligible for a satisfactory grade unless granted a compensation for disadvantages in examination performance ("Nachteilsausgleich") by the examination board ("Prüfungsausschuss").

Determination of the final grade:

| objective                     | weight    |
| ----------------------------- | --------- |
| final project                 | 60%       |
| scientific paper presentation | 20%       |
| (active) attendance           | 20%       |

The basis for evaluation:

- all "visible" artifacts (e.g. commits, pull requests, code reviews, user stories, mockups, documentation and whatever can be put in a zip archive)
- participation during meetings (e.g. small presentations, discussions, questions and whatever can be considered an ephemeral moment of light)

<a id="toc-books"></a>

## Books

No books are required. You can ask for recommendations on specific topics though. Some books are referenced on the [week's page](/weeks/).

<a id="toc-lectures"></a>

## Lectures

| Week                            | Topic                                                   | Date       |
|---------------------------------| ------------------------------------------------------- | ---------- |
| [Week 00](/weeks/week-00.md)    | Introduction & Orga                                     | 2024-10-29 |
| [Week 01](/weeks/week-01.md)    | Git                                                     | 2024-11-05 |
| [Week 02](/weeks/week-02.md)    | Ideation & Planning                                     | 2024-11-12 |
| [Week 03](/weeks/week-03.md)    | Design                                                  | 2024-11-12 |
| [Week 04](/weeks/week-04.md)    | Architecture                                            | 2024-11-19 |
| [Week 05](/weeks/week-05.md)    | Documentation                                           | 2024-11-26 |
| [Week 06](/weeks/week-06.md)    | Agile                                                   | 2024-12-03 |
| [Week 07](/weeks/week-07.md)    | Coding together                                         | 2024-12-03 |
| [Week 08](/weeks/week-08-09.md) | **[Student Conference (1/2)](#toc-student-conference)** | 2024-12-10 |
| [Week 09](/weeks/week-08-09.md) | **[Student Conference (2/2)](#toc-student-conference)** | 2024-12-17 |
| [Week 10](/weeks/week-10.md)    | Testing                                                 | 2025-01-14 |
| [Week 11](/weeks/week-11.md)    | Retrospective                                           | 2025-01-21 |
| [Week 12](/weeks/week-12.md)    | Infrastructure                                          | 2025-01-28 |
| [Week 13](/weeks/week-13.md)    | Hackathon                                               | 2025-02-04 |
| [Week 14](/weeks/week-14.md)    | Security                                                | 2025-02-04 |
| [Week 15](#toc-final-project)   | **Final Project Presentations**                         | 2025-02-11 |

<a id="toc-office-hours"></a>

## Office Hours

There are no office hours. The weekly appointments offer sufficient time and are the best opportunity to seek help or ask questions.

For asynchronous communication use the forum in the Moodle course.

If neither is an option, send me an email. However, I do not answer them every day.

<a id="toc-checks-for-understanding"></a>

## Checks for Understanding

Checks for understanding are short assignments after each meeting to practice applying each week's concepts.

These checks are *optional*, but pay into your active participation if you present them in the following week. So they could also be called opportunities to shine.

<a id="toc-student-conference"></a>

## Student Conference

The **Student Conference** is an epic event during which we dive into your choices of scientific papers. Everyone presents insights from the world of science and everyone learns something new.

To prepare for this:

1. Search for a scientific publication on a computer science topic of interest to you (in English!). Some search engine suggestions:

   - [ResearchGate](https://www.researchgate.net/)
   - [Google Scholar](https://scholar.google.com/)
   - [arxiv.org](https://arxiv.org/)
   - [Science.gov](https://www.science.gov/)

1. write title & author(s) in the Etherpad on Moodle. If possible, add a link to the full paper
1. Read and summarize the paper for yourself. Focus on these aspects:
  
   - objective
   - hypothesis
   - research method
   - reasoning
   - result

1. Situate the work in its larger context
1. What is your opinion? Are you convinced? Is anything unclear? Are there points of criticism?
1. Create a presentation on your findings.
1. Book a slot in the planer on Moodle.

Make your presentation appealing, engaging and informative so that we all benefit from it.


| Milestone      | allotted time | Date                   |
| -------------- | ------------- | ---------------------- |
| Presentation   | 10 min (max!) | Week 08 and Week 09    |

Remark: ["How to Read a Paper"](http://ccr.sigcomm.org/online/files/p83-keshavA.pdf) by S. Keshav is itself a scientific publication, which describes a procedure that you may want to adapt. Please read it in advance, it is only 2 pages long.

<a id="toc-final-project"></a>

## Final Project

The climax of this course is its final project. The final project is your opportunity to showcase your graduation progress and develop your very own piece of software. So long as the project draws upon your degree’s learning objectives, the nature of your project is entirely up to you (albeit subject to my approval).

You may implement your project in almost any language(s). You are welcome to utilize any infrastructure, provided you grant me access to any hardware and software that your project requires. Deviations from this rule must be well justified (e.g. the hardware cannot be transported or removed).

You may build something of interest to you: solve an actual problem, impact campus, or change the world. Strive to create something that outlives this course.

You are required to collaborate in a group of **4-6** classmates. Needless to say, it is expected that all students contribute equally to the design and implementation of the group’s project. Moreover, it is expected that the project’s scope is appropriate to the group’s size.

You are welcome to solicit advice from others outside your group, so long as you respect the course’s policy on academic honesty.

The team composition should be finalized in week 3, in which you **present your team's idea** to everyone.

From then on, at least 2 members of the team give a **weekly update** on the progress of the project.

Shortly before the final phase, the team comes together for a [**retrospective**](/weeks/week-11.md). The team reflects on the collaboration so far and, if necessary, considers adjustments for the future.

During the **Final Project Presentation** you:

- release your software
   - what is the goal or solved problem

- demonstrate all features and functionalities
   - walkthrough of the user experience
   - design considerations

- explain technical aspects
   - system architecture, key components and their interactions
   - technical challenges you faced
   - key code snippets
   - performance metrics and optimization efforts
   - testing process
   - CI/CD pipeline

- summarize your organization
   - roles & responsibilities
   - project timeline, milestones
   - ways of working together (Agile, Scrum, Kanban,...)
   - project management tools
   - quality assurance (code review, bug tracking,...)
   - documentation artefacts

- reflect on your approach: if you would start a new project, what would you
   - do the same way again?
   - do differently?
   - no longer do at all?

- discuss potential future enhancements to your software

- have space to talk about anything else of interest:
   - special hardware
   - tricky algorithm
   - strange bugs
   - unexpected turn of events
   - user feedback
   - specific efforts (e.g. accessibility, localization)
   - security considerations
   - ...

Each member of the group is responsible for a part of the presentation.

| Milestone      | allotted time | Date                   |
| -------------- | ------------- | ---------------------- |
| Proposal       | 10 min        | Week 03 (2024-11-12)   |
| Status Report  | up to 10 min  | every week from now on |
| Retrospective  | 30-45 min     | Week 11 (2025-01-14)   |
| Release        | 30 min        | Week 15 (2025-02-11)   |

### Past project ideas as inspiration

- tower defense game
- restaurant table reservation system
- file hosting service (NextCloud clone)
- inventory tracking system
- planner for exams & learning objectives
- smart home dashboard (Home Assistant clone)

<a id="toc-attendance"></a>

## Attendance

Attendance at the fixed events (as outlined in the sections *Student Conference* & *Final Project*) is **mandatory**. Exceptions will only be considered on submission of a medical certificate ("Krankmeldung"). If this is missing, the respective event will be assessed as failed. Any missed event must be compensated for in an appropriate way as soon as possible.

The only exceptions are the weekly team updates. For this it is only necessary that **at least 2** team members are always present. If an update does not take place, this will have a negative effect on the entire team.

<a id="toc-academic-honesty"></a>

## Academic Honesty

The course’s philosophy on academic honesty is best stated as “be reasonable.” The course recognizes that interactions with classmates and others can facilitate mastery of the course’s material. However, there remains a line between enlisting the help of another and submitting the work of another. This policy characterizes both sides of that line.

The essence of all work that you submit to this course must be your own. Collaboration on tasks is permitted to the extent that you may ask others for help so long as that help does not reduce to another doing your work for you.

Below are rules of thumb that (inexhaustively) characterize acts that I consider reasonable and not reasonable. Acts considered not reasonable are handled harshly. That may include an unsatisfactory or failing grade for work submitted or for the course itself.

<a id="toc-honesty-reasonable"></a>

### Reasonable

- discussing the course’s material with others in order to understand it better
- helping a classmate identify a bug in their code
- viewing, compiling, or running a classmate’s code
- writing code together if all authors are comprehensibly documented (e.g. individual commits or co-authored commits)
- incorporating a few lines of code that you find online or elsewhere into your own code, provided that you cite the lines’ origins
- submitting the same or similar work to this course that you have submitted previously to another course, so long as you disclose the extent in your submission
- turning to the instructor for help
- turning to the web or elsewhere for instruction beyond the course’s own, for references, and for solutions to technical difficulties
- working with (and even paying) a tutor to help you with the course, provided the tutor does not do your work for you

<a id="toc-honesty-not-reasonable"></a>

### Not Reasonable

- accessing or attempting to access, without permission, an account not your own
- failing to cite (as with comments) the origins of code or techniques that you discover outside of the course’s own lessons and integrate into your own work
- paying or offering to pay an individual for work that you may submit as (part of) your own
- submitting (after possibly modifying) the work of another individual beyond the few lines allowed herein
- submitting the same or similar work to this course that you have submitted or will submit to another course
- using AI-based software (e.g. ChatGPT, GitHub Copilot, Gemini, et al.) that suggests or completes answers to tasks or lines of code

<a id="toc-this-repo"></a>

## This repository

<a id="toc-links"></a>

### Links

We have a lot of references to external resources. Unfortunately, servers are not immortal and sometimes _the Internet_ very well does forget. In that case, try to paste the link into the [wayback machine](https://web.archive.org/) or some other archive of your choice.

<a id="toc-further-resources"></a>

### Adapted resources

Many thanks to the valued work of other academic lecturers, especially:

- [CS50's syllabus](https://cs50.harvard.edu/college/2023/fall/syllabus/)
- [UChicago CS Student Resource Guide](https://uchicago-cs.github.io/student-resource-guide/teams.html)