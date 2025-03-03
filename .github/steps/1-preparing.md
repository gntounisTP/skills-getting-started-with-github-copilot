## Step 1: Preparing

Welcome to **"Accelerate with GitHub Copilot"** exercise! :robot:

In this exercise, you will be using different GitHub Copilot features to work on a website that allows students of Mergington High School to sign up for extracurricular activities :student:

### What is GitHub Copilot?

GitHub Copilot is an AI coding assistant that helps you write code faster and with less effort, allowing you to focus more energy on problem solving and collaboration.

GitHub Copilot has been proven to increase developer productivity and accelerate the pace of software development. For more information, see [Research: quantifying GitHub Copilot’s impact on developer productivity and happiness in the GitHub blog.](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)

### How can I use GitHub Copilot?

### :keyboard: Activity: Getting to know basic Copilot features :robot:

1. Right-click the below button to open the **Create Codespace** page in a new tab.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

   - The free tier of Codespaces that comes with all GitHub accounts is fine, assuming you still have minutes available.
   - The default Codespace settings are fine.
   - This repository will provide the additional settings and files for making your extension.

1. Confirm the **Repository** field is your copy of the exercise, not the original, then click the green **Create Codespace** button.

   - ✅ Your copy: `/{{{full_repo_name}}}`
   - ❌ Original: `/skills/accelerate-with-copilot`

1. Wait a moment for Visual Studio Code to load in your browser.

1. Click the extensions sidebar tab and verify that `GitHub Copilot` extension is installed.

   <!-- TODO: Add screenshot -->

1. Search for the Copilot Icon on the top right section of your editor.
   Open up Copilot Chat and ask Copilot to introduce you to the project, to do that type `/explain` in the Chat Window.
   <!-- TODO: Add screenshot -->
1. Run the project by using  `Run and Debug` section in the left sidebar of VS Code. Then head to the ports tab and open the application available on port 8000

   <!-- TODO: Add screenshot -->

1. Great! Now that you know what we will be working with, let's have your first interaction with Copilot.

   Open up a terminal in VS Code so you won't interrupt the debug session you just started.

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
