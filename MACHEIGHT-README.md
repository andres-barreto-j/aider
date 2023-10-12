Welcome to the initial technical evaluation for joining macheight. In this assessment, we expect you to showcase your debugging proficiency, ability to write clean code, and your expertise in algorithms and data structures.

## Instructions
- Begin by cloning this repository: `git clone https://github.com/jahelsantiago/aider.git`
- Establish a new branch with your name: `git checkout -b <your-name>`
- Set up a virtual environment: `python3 -m venv venv`
- Activate the virtual environment: `source venv/bin/activate`
- Install the necessary dependencies: `pip install -r requirements.txt`
- Execute the LLM litellm `--model huggingface/codellama/CodeLlama-34b-Instruct-hf --max_tokens 2048`
- Open a new terminal tab
- Launch the application using: `python -m aider.main --openai-api-base http://0.0.0.0:8000 --openai-api-key "fake"`


## Tasks
You are required to address two challenges. The first task involves investigating a bug report from a user, while the second task involves resolving failing unit tests.


- [ ] A user reported that the application hangs after following a specific sequence of steps:

    * Initially, navigate to the `AIDER` folder and run the application using the command `python -m aider.main --openai-api-base http://0.0.0.0:8000 --openai-api-key "fake"`
    * Subsequently, write the command `/drop` and then the command `/clear`
    * After doing this, inpu thet command `/show-chat-history`, which make the application hang for a few seconds and then it showed the message:
    
    ```bash
    Invalid command: /show-chat-history
    Type /help for a list of commands.
    ```

    The unusual behavior is observed when other invalid commands like `/close` or `/report` are entered; the application does not hang for as long as it does with the `/show-chat-history` command. Can you rectify this reported issue and solve it? 

---

- [ ] Some of the unit tests are failing, your task is to run these tests and correct the ones that are failing.




## Deliverables
- [ ] Create one commit for each task. Upload a Pull request with your changes to the repository that was assigned to you.
- [ ] Add a comment to the Pull request with the time you spent on the test.
- [ ] Send us an email once it you are finished.
