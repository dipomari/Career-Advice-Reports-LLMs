
# Profile Evaluation System

This system processes a set of profiles using OpenAI's API to generate reports on different areas, such as competency frameworks, skill gaps, educational recommendations, career pathways, and action plans.

## How to Use

1. **Install the required dependencies:**

   Run the following command to install the dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up Environment Variables:**

   You will need to create a `.env` file in the root directory of the project to store your OpenAI API credentials and assistants IDs. This file should contain the following information:

   ```plaintext
   OPENAI_API_KEY="sk-proj-"
   
   ASSISTANTS.competency_framework="asst_"
   ASSISTANTS.skill_gap="asst_"
   ASSISTANTS.educational_recommendation="asst_"
   ASSISTANTS.career_pathway="asst_"
   ASSISTANTS.action_plan="asst_"
   ```

   This `.env` file ensures the correct API key and assistant configurations are used during execution.

3. **Run the Pipeline:**

   Once everything is set up, you can run the system using the following command:

   ```bash
   python3 pipeline.py
   ```

4. **Modifying the Profiles:**

   In the `pipeline.py` script, the system processes the profiles stored in a dictionary. If you wish to adjust the number of profiles being processed, you can modify the loop that iterates through the profiles. For example:

   ```python

   peding_profiles = [profile_1,profile_2,profile_3,]
   
   for profile in peding_profiles:
   ```

   You can customize the number of profiles according to your needs by adjusting the slice or loop conditions.

## Additional Notes

- Ensure your API key is valid and that you have the necessary permissions to use OpenAI's API.
- Refer to the OpenAI API documentation for any potential limitations or usage guidelines regarding the assistants you are using.

Feel free to adjust the code or configurations as needed!
