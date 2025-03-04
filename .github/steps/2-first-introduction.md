## Step 2: First interaction with Copilot

There are many Copilot Features and interaction modes. In this step you will get to use some of them:

- **Code completions**: As you type, Copilot suggests code completions directly in your editor. Can generate entire functions based on comments or existing code context.
- **Copilot Chat**: A chat interface that lets you ask coding-related questions. You will see different modes in which you can use Copilot chat

> [!NOTE]
> You can see see all currently available GitHub Copilot features that are live or in preview in the documentation. See [GitHub Copilot Features](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features)

**What is context?**: GitHub Copilot context refers to comments or existing code that Copilot uses to understand your intent and generate relevant code suggestions.

### :keyboard: Activity: Getting to know basic Copilot features :robot:

1. Open `src/app.py` file and let's start working on improving our High School API :robot:!.

   To start off - you will add additional validation to the `signup_for_activity` endpoint. Right now there is no logic to prevent users to sign to the same activity twice.

   Within the code of `signup_for_activity` endpoint, write a comment to provide Copilot context of what it is you are trying to do

   ```python
   # Validate student is not already signed
   ```

   Then press `Enter` to go to newline and Copilot will provide you with autocompletion suggestions!

   Press `Tab` to accept your first Copilot suggestion :tada: :robot:


   <details>
   <summary>Example suggestion</summary><br/>

   ```python
   @app.post("/activities/{activity_name}/signup")
   def signup_for_activity(activity_name: str, email: str):
      """Sign up a student for an activity"""
      # Validate activity exists
      if activity_name not in activities:
         raise HTTPException(status_code=404, detail="Activity not found")

      # Validate student is not already signed
      if email in activities[activity_name]["participants"]:
         raise HTTPException(status_code=400, detail="Student is already signed up")
      
      activity = activities[activity_name]

      # Add student
      activity["participants"].append(email)
      return {"message": f"Signed up {email} for {activity_name}"}
   ```
   </details>

   > **TIP**: If you would like to see other suggestions, instead of pressing `Tab`, hover over the suggestion and a small panel will show up. On it's right side click the three dots `...` and select `Open Completions Panel`


1. Open up Copilot Chat window and ask Copilot to help you create a completely new endpoint to the API

   ```txt
   Hey Copilot! Create a endpoint that will allow students to sign themselves out from an activity
   ```

   On the bottom part of Copilot Chat you can choose what AI Model Copilot should use. Different models can provide different results.
   ![image](https://github.com/user-attachments/assets/2668c5f8-1f28-4361-bf07-0b67d6a4e7c4)

1. You can use Copilot Chat inline to stay in the flow. It's often used when you are dealing with problems or want to understand a specific part of the code.

   Hold down left button of your mouse and select this part of the file.

   ```python
   current_dir = Path(__file__).parent
   app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")
   ```

   Then `Right click` =>`Copilot` => `Editor Inline Chat` and use the `/explain` function.

1. In the `Source Control` section on the left sidebar of VS Code.
   1. Click the `+` sign next to  `app.py` file to stage your changes.
   1. On the right side of the commit message window click :sparkles: to generate commit message with copilot
   1. Commit and sync your changes with the automatically generated message

   ![image](https://github.com/user-attachments/assets/7d3daf4e-4125-4775-88a7-33251cd7293e)


1. Wait a moment for the bot to check your work. You will see a comment with progress info and the next lesson.

   <details>
   <summary>Having trouble? 🤷</summary><br/>

   If you don't get feedback, here are some things to check:

   - Make sure your pushed the `src/app.py` file changes to the branch `accelerate-with-copilot`.

   </details>
