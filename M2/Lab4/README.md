# M2 Lab 3 Deploying to Streamlit Community Cloud

In Module 2 Lab 3, you'll deploy the Streamlit app you have previously built and deployed on the Snowflake platform onto the [Streamlit Community Cloud](https://streamlit.io/cloud).

**Before attempting to deploy your app to the cloud, make sure you have completed the steps in Module 2 Lab 1 and Module 2 Lab 2.**

## Deploying the app
To deploy your apps to the cloud, you’ll need to sign up for Streamlit Community Cloud account using your Github login, so that we can link the two accounts for easy deployment. 

1. Navigate to Streamlit Community Cloud
2. Click on “Join Community Cloud”
3. Another browser window will pop-up. From here, click on “Continue to Sign-in”
4. Click on “Continue with Github”
5. Click on “Authorize Streamlit”
6. An email will be sent to the email address used on your Github account called “Verify your email address” sent from Streamlit Community Cloud
7. Open that email and copy the verification code
8. Go back to the Streamlit Community Cloud sign in and enter the verification code to verify your account

You’re now able to use your Streamlit Community Cloud account and deploy directly from your Github repository

## Deploying to the Community Cloud
To deploy the app you’ve just built: 
1. From the home page of Streamlit Community Cloud, click on the “Create App” button on the top-right of your screen
2. Select the option on the left to “Deploy a public app from Github” by clicking on “Deploy Now”
3. In the Repository field, enter the Github URL for the repo you want to deploy (in our case, the main course repo address)
4. In the Main File Path field, click on the drop-down menu to drill down to the file for the streamlit_app.py file that you want to deploy
5. Click on Deploy and give it a few moments to spin up your new app
6. Once deployed, you will be provided with a link where you can view and share your new app. 
