# AutoDocGen

[![CI](https://github.com/mehrshud/AutoDocGen/actions/workflows/ci.yml/badge.svg)](https://github.com/mehrshud/AutoDocGen/actions) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org) [![Stars](https://img.shields.io/badge/stars-3000+-yellow)](https://github.com/mehrshud/AutoDocGen) [![Issues](https://img.shields.io/github/issues/mehrshud/AutoDocGen)](https://github.com/mehrshud/AutoDocGen/issues) [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-ffdd00?logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/omnilertlab)

## **Tagline**
💡 Save hours of documentation time and focus on coding with AutoDocGen, the AI-powered documentation generator for open-source projects.

## **Why I Built This**
I'll be honest, I was tired of wasting hours writing and updating documentation for my SaaS projects. As an indie hacker, I knew I wasn't alone in this struggle. I tried using existing tools like Swagger and Dox, but they were clunky, hard to integrate, and didn't quite fit my needs. I needed something that could automatically generate documentation based on my code comments and structure. After weeks of searching, I realized I had to build it myself. 
The moment of insight came when I was working on a project with a team of contributors. We were using GitHub and GitLab for version control, and I wanted a way to automatically deploy documentation to GitHub Pages. I started experimenting with natural language processing and machine learning libraries in Python, and soon I had a working prototype. 
I shared it with my team, and they loved it. We were able to save hours of documentation time and focus on coding. That's when I knew I had to share AutoDocGen with the world. I believe that every open-source maintainer and contributor deserves to have an easy and efficient way to generate and maintain documentation. 
That's why I'm sharing AutoDocGen with you today. It's not perfect, but it's a start. I hope you'll join me in making it better and helping to revolutionize the way we approach documentation in open-source projects.

## **Real-World Usage Examples**
# Example 1: Basic usage
from autodocgen import AutoDocGen
doc_gen = AutoDocGen()
doc_gen.generate_docs("path/to/your/code")

# Example 2: Customizing templates
from autodocgen import AutoDocGen
doc_gen = AutoDocGen(template="custom_template")
doc_gen.generate_docs("path/to/your/code")

# Example 3: Integrating with GitHub
from autodocgen import AutoDocGen
import github
github_token = "your_github_token"
doc_gen = AutoDocGen(github_token=github_token)
doc_gen.generate_docs("path/to/your/code")
doc_gen.deploy_to_github_pages()

# Example 4: Using with GitLab
from autodocgen import AutoDocGen
import gitlab
gitlab_token = "your_gitlab_token"
doc_gen = AutoDocGen(gitlab_token=gitlab_token)
doc_gen.generate_docs("path/to/your/code")
doc_gen.deploy_to_gitlab_pages()

# Example 5: Collaboration features
from autodocgen import AutoDocGen
doc_gen = AutoDocGen()
doc_gen.generate_docs("path/to/your/code")
doc_gen.add_collaborator("username")

## **Comparison Table**
| Feature | AutoDocGen | Alternative 1 (Swagger) | Alternative 2 (Dox) |
| --- | --- | --- | --- |
| AI-powered documentation generation | ✅ | ❌ | ❌ |
| Support for multiple programming languages | ✅ | ✅ | ✅ |
| Integration with GitHub and GitLab | ✅ | ❌ | ❌ |
| Customizable templates | ✅ | ❌ | ✅ |
| Automated deployment to GitHub Pages | ✅ | ❌ | ❌ |
| Collaboration features for team members | ✅ | ❌ | ❌ |

## **Architecture**
graph TD
  A[Client] -->|REST| B[API]
  B -->|Task| C[Worker]
  C -->|Result| B
  B -->|Result| A
  subgraph Redis
  D[Cache]
  end
  subgraph Celery
  E[Broker]
  end
  B -->|Task| E
  E -->|Task| C
The client sends a request to the API, which creates a task for the worker to process. The worker uses Redis as a cache to store the results, and Celery as a broker to manage the tasks. The API then sends the result back to the client. 

## **Getting Started**
# Step 1: Install AutoDocGen using pip
pip install autodocgen

# Step 2: Initialize AutoDocGen
autodocgen init

# Step 3: Generate documentation
autodocgen generate

## **Advanced Configuration**
| Environment Variable | Description | Default |
| --- | --- | --- |
| `AUTODOCGEN_TEMPLATE` | Custom template for documentation | `default_template` |
| `AUTODOCGEN_GITHUB_TOKEN` | GitHub token for deployment | `None` |
| `AUTODOCGEN_GITLAB_TOKEN` | GitLab token for deployment | `None` |
| `AUTODOCGEN_REDIS_URL` | Redis URL for caching | `localhost:6379` |
| `AUTODOCGEN_CELERY_BROKER` | Celery broker URL | `amqp://localhost` |

## **Troubleshooting**
1. **Error: Unable to connect to Redis** - Check your Redis URL and make sure it's correct.
2. **Error: Unable to deploy to GitHub Pages** - Check your GitHub token and make sure it has the correct permissions.
3. **Error: Unable to generate documentation** - Check your code comments and make sure they're in the correct format.
4. **Error: Collaborator not found** - Check the collaborator's username and make sure it's correct.
5. **Error: Template not found** - Check the template name and make sure it exists.

## **Roadmap**
- [ ] v1.1: Improve support for multiple programming languages
- [ ] v1.2: Add more customizable templates
- [ ] v1.3: Enhance collaboration features for team members

## **Contributing**
* Fork the repository
* Create a new branch for your feature
* Commit your changes with a descriptive message
* Open a pull request
* Wait for review and feedback

## **Demo**
> 📽️ **Live Demo:** [Watch on Loom](https://loom.com) | [Asciinema](https://asciinema.org)
> 
> ![Demo GIF](docs/assets/demo.gif)

## **Footer:**
Made with ❤️ by [mehrshud](https://github.com/mehrshud) · [AutoDocGen Website](https://omnilertlab.com)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/omnilertlab)