# Week 12 - Operations & Infrastructure

[DORA's DevOps capabilities](https://cloud.google.com/architecture/devops)

## Containerization

contain everything you need to run an application, e.g.

- [Docker](https://docs.docker.com/)
- [podman](https://podman.io/)

## Infrastructure as Code

machine-readable configuration files, e.g.

- [Terraform](https://www.terraform.io)
- [OpenTofu](https://opentofu.org)
- [Ansible](https://www.redhat.com/en/ansible-collaborative)

## Service Level Agreement

set clear expectations

- availability

    - downtime frequency
    - downtime duration
    - maintenance windows
    - data availability (recovery point of backups)

- performance

    - thresholds for response times (e.g. less than 1 second in 99% of the cases)

- response time
- monitoring & reporting

## Post Mortem

example: [Last Epoch's Launch Retrospective](https://forum.lastepoch.com/t/1-0-launch-retrospective/69374)

## Tasks

- the [12 factors](https://12factor.net/) are distributed equally among all teams

    - (15 min) read and understand the factor(s)
    - (1 min) short presentation per factor

- in the team:

    - (30 min) Identify a process in your development workflow that is cumbersome or error-prone. Automate it! Examples:

        - linting
        - [dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuring-dependabot-version-updates)
        - [GitHub Action: Automatic Releases](https://github.com/marketplace/actions/automatic-releases)
        - hacky bash script
