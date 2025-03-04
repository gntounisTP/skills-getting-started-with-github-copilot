## Step 1: Preparing

Welcome to **"Accelerate with GitHub Copilot"** exercise! :robot:

In this exercise, you will be using different GitHub Copilot features to work on a website that allows students of Mergington High School to sign up for extracurricular activities :student:

### What is GitHub Copilot?

GitHub Copilot is an AI coding assistant that helps you write code faster and with less effort, allowing you to focus more energy on problem solving and collaboration.

GitHub Copilot has been proven to increase developer productivity and accelerate the pace of software development. For more information, see [Research: quantifying GitHub Copilot’s impact on developer productivity and happiness in the GitHub blog.](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)

### How can I use GitHub Copilot?

### :keyboard: Activity: Getting to know basic Copilot features :robot:

1. Right-click the below button to open the **Create Codespace** page in a new tab. Use the default configuration.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. Confirm the **Repository** field is your copy of the exercise, not the original, then click the green **Create Codespace** button.

   - ✅ Your copy: `/{{{full_repo_name}}}`
   - ❌ Original: `/skills/accelerate-with-copilot`

1. Wait a moment for Visual Studio Code to load in your browser.

1. Click the extensions sidebar tab and verify that `GitHub Copilot` extension is installed.

   ![image](https://github.com/user-attachments/assets/c1ddca93-723d-4c62-a309-5944e5dfc6f4)


1. Search for the Copilot Icon on the top right section of your editor.
   Open up Copilot Chat and ask Copilot to introduce you to the project.

   ```txt
   @workspace Briefly explain the structure of the codebase in this repository.
   ```

1. Run the project by using  `Run and Debug` section in the left sidebar of VS Code.

   <img width="300" alt="image" src="https://github.com/user-attachments/assets/50b27f2a-5eab-4827-9343-ab5bce62357e" />


1. Then head to the ports tab and open the application available on port `8000`

  ![image](https://github.com/user-attachments/assets/92d5642e-ce99-4a66-850c-2d311a673596)


1. Great! Now that you know what we will be working with, let's have your first interaction with Copilot.

   Open up a terminal a new terminal window in VS Code so you won't interrupt the debug session you just started in the current one.

   Next, `Right click` within the newly created terminal window, then click `Copilot` => `Terminal Inline Chat`.

   This feature can help you with any shell commands, in our case let's ask Copilot

   ```txt
   Hey copilot, how can I create and publish a new git branch? The branch should be named accelerate-with-copilot
   ```

   Copilot will provide you with a list of commands that it thinks you should run. If something feels off, you can Ask Copilot to fix or customize the commands further and when you are ready, press `Run` and Copilot will run the commands for you in your terminal!

1. Wait a moment for the bot to check your work. You will see a comment with progress info and the next lesson.

   <details>
   <summary>Having trouble? 🤷</summary><br/>

   If you don't get feedback, here are some things to check:

   - Make sure your created the branch with the exact name `accelerate-with-copilot`. No prefixes or suffixes.

   </details>
