## Step 3: GitHub Copilot Edits

 [Copilot Edits](https://code.visualstudio.com/docs/copilot/copilot-edits) works as an AI-powered code editing session to make changes across multiple files using natural language.

 Copilot Edits applies the edits directly in the editor, where you can review them in-place, with the full context of the surrounding code.

**Key features:**

- **Multi-file Editing**: Copilot Edits can make changes across multiple files in your workspace.
- **Iterative Workflow**: Designed for fast iteration, allowing you to review, accept, or discard AI-generated code.
- **In-place Edits**: Shows generated code directly in your editor, providing a code review-like flow.
- **Working Set**: Allows you to define which files the edits should be applied to.


**How it works:**

- **Set Context**: Define the working set by selecting files.
- **Provide Instructions**: Use natural language to tell Copilot what changes you need.
- **Review Changes**: See proposed changes in-place in your code
- **Accept or Discard**: Review each AI-generated edit and choose which changes to keep
- **Iterate**: Provide follow-up instructions and refine the changes as needed

### :keyboard: Activity: Let's add a feature!

1. In the top left part of Copilot Chat window, switch to Copilot Edits.

 ![image](https://github.com/user-attachments/assets/0b17c5bd-d03b-41b1-b97d-624fcbf8ccd1)

1. Add the following files to the working set. Use the attach button in the bottom left corner of Copilot Edits view.
    - `src/static/app.js`
    - `src/static/index.html`
    - `src/static/styles.css`
1. Ask Copilot to add a new feature to the website.

    ```txt
    Hey Copilot. Edit the area where activities are listed on the website to show what participants are already signed for that activity.
    ```

    Copilot will generate inline edits for you. You can accept them or if this wasn't what you were hoping for, provide Copilot additional instructions.

    > **TIP:** On the bottom part of Copilot Edits you can choose what AI Model Copilot should use. Different models can provide different results.

   <details>
   <summary>Having trouble? 🤷</summary><br/>

   Remember, to add the relevant files to the working set.
    
    
   ![image](https://github.com/user-attachments/assets/bdd7318b-50e3-46d0-88ce-7615f45ce334)

    
   </details>

1. Head back to the website and see your changes!
    <details>
   <summary>Having trouble? 🤷</summary><br/>

    Remember, you can access the website url from the `ports` tab.

    If the website is not available, check that it is still running. You can run in through the left sidebar's `Run and Debug` section.

   </details>

1. Commit and push the changes.
1. Head back to your repository on github.com and open up a pull request to the `main` branch.
   <!-- TODO: Add link -->

1. Wait a moment for the bot to check your work. You will see a comment with progress info and the next lesson.

   <details>
   <summary>Having trouble? 🤷</summary><br/>

   If you don't get feedback, here are some things to check:

   - Make sure your pushed the changes in the `src/static/` directory to the branch `accelerate-with-copilot`.
   - Make sure you opened a pull request to the `main` branch

   </details>
