# Testcases

### **Test Case 1: Login with Valid Credentials**

**Objective:** To verify that users can successfully log in to Any.do with valid credentials.

**Preconditions:**

- Any.do is installed on the device.
- The user has a valid Any.do account.

**Test Steps:**

1. **Launch Any.do:**
    - Open the Any.do application on the device.
2. **Navigate to the Login Screen:**
    - Tap on the "Login" option on the application's main screen.
3. **Enter Valid Credentials:**
    - Enter a valid username (email) in the "Username" field.
    - Enter a valid password in the "Password" field.
4. **Initiate Login:**
    - Tap on the "Login" button to submit the entered credentials.
5. **Verify Successful Login:**
    - Check if the application navigates to the user's dashboard or home screen.
    - Verify that user-specific information (tasks, lists) is displayed.
6. **Logout (if applicable):**
    - If the application has a logout option, navigate to the logout functionality.
    - Confirm that the user is successfully logged out.

**Expected Results:**

- The application should successfully launch without errors.
- The login screen should be displayed after selecting the "Login" option.
- Valid credentials should be accepted without any error messages.
- After successful login, the application should navigate to the user's dashboard.
- User-specific information (tasks, lists) should be visible, confirming a successful login.
- If applicable, the logout process should work correctly.

### **Test Case 2: Task Creation and Confirmation**

**Objective:** To verify that users can successfully create a new task in Any.do.

**Preconditions:**

- Any.do is installed on the device.
- The user has logged in to his [Any.do](http://Any.do) account.

**Test Steps:**

1. **Launch Any.do:**
    - Open the Any.do application on the device.
2. **Add Task:**
    - Locate and select the "+" sign for adding a task depending on the day.
3. **Enter Task Details:**
    - Enter a valid title for the task in the designated field.
    - Set a valid date and time for the task, if applicable.
4. **Save the Task:**
    - Tap on the "Up Arrow" button to save the entered task details.
5. **Verify Task Creation:**
    - Check if the task is successfully created and displayed in the task list.
    - Verify that the entered details (title, date, time) match the created task.

**Expected Results:**

- The application should successfully launch without errors.
- The user should be able to enter a title for the task.
- If applicable, the user should be able to set a date and time for the task.
- The task should be saved successfully without any error messages.
- The created task should be visible in the task list.
- The displayed task details (title, date, time) should match the entered information.

**Postconditions:**

- The task is successfully created and added to the task list in Any.do.

### **Test Case 3: Task Reminder Notification Validation**

**Objective:** To validate that users receive a timely reminder notification for a scheduled task in Any.do.

**Preconditions:**

- Any.do is installed on the device.
- The user has logged in to his [Any.do](http://Any.do) account.
- A task with a reminder is already added to Any.do.
- Verify that notifications are enabled for Any.do in the device settings.

**Test Steps:**

1. **Wait for the Reminder Notification:**
    - Allow the scheduled time for the task reminder to elapse.
    - Keep the application in the background or lock the device.

**Expected Results:**

- The user should receive a timely reminder notification for the scheduled task.
- The notification content should include relevant information about the task (title, date, time).

**Postconditions:**

- The user receives the reminder notification as expected.

### **Test Case 4: Task Deletion**

**Objective:** To verify that users can successfully delete an existing task in Any.do.

**Preconditions:**

- Any.do is installed on the device.
- The user has logged in to his [Any.do](http://Any.do) account.
- At least one task is already added to Any.do.

**Test Steps:**

1. **Launch Any.do:**
    - Open the Any.do application on the device.
2. **Locate an Existing Task:**
    - Identify an existing task that needs to be deleted.
3. **Delete the Task:**
    - Select the identified task.
    - Initiate the task deletion process (e.g., drag the task to the right, press “x” sign for deletion).

**Expected Results:**

- The application should successfully launch without errors.
- The task is successfully deleted, and it no longer appears in the task list.

**Postconditions:**

- The task is successfully deleted from Any.do.

### **Test Case 5: Offline Task Management**

**Objective:** To verify that users can manage tasks in offline mode, and changes made are synchronized when the device is back online in Any.do.

**Preconditions:**

- Any.do is installed on the device.
- The user has logged in to his [Any.do](http://Any.do) account in online mode before.

**Test Steps:**

1. **Turn Off Device's Internet Connection:**
    - Disable the device's internet connection (e.g., turn off Wi-Fi, mobile data).
2. **Manage Tasks in Offline Mode:**
    - Open the Any.do application on the device.
    - Create a new task in offline mode.
    - Edit an existing task in offline mode.
    - Delete a task in offline mode.
3. **Reconnect to the Internet:**
    - Enable the device's internet connection (e.g., turn on Wi-Fi, mobile data).

**Expected Results:**

- The application should successfully launch without errors.
- The user should turn off the device's internet connection.
- Tasks can be created, edited, and deleted in offline mode without errors.
- Upon reconnecting to the internet, changes made in offline mode are synchronized.
- The synchronized tasks should reflect accurately in the online mode.

**Postconditions:**

- Changes made in offline mode are successfully synchronized when the device is back online.

### **Test Case 6: Cross-Device Sync**

**Objective:** To verify that tasks are seamlessly synchronized across multiple devices in Any.do.

**Preconditions:**

- Any.do is installed on multiple devices.
- The user has a valid Any.do account and is logged in on all devices.

**Test Steps:**

1. **Create a Task on One Device:**
    - Open the Any.do application on one of the devices.
    - Navigate to the task list.
    - Create a new task on the selected device.
2. **Verify Task Sync on Another Device:**
    - Open Any.do on another synced device.
    - Navigate to the task list on the second device.

**Expected Results:**

- The application should successfully launch without errors on both devices.
- A task is created on one device successfully.
- On the second device, the created task should seamlessly appear in the task list.
- The task details (title, date, time) on both devices should match.

**Postconditions:**

- Tasks are seamlessly synchronized across multiple devices.

### **Test Case 7: Scaling Print Page Size**

**Objective:** To verify that users can successfully navigate to the print page within the application and scale up and down the size.

**Preconditions:**

- Any.do is installed on the device.
- The user has logged in to his [Any.do](http://Any.do) account in online mode before.

**Test Steps:**

1. **Navigate to the Print Page:**
    - Open the application on the device.
    - Access the menu or navigation options to find and select the "Print Page."
2. **Scale Up the Page Size:**
    - On the print page, attempt to scale up the size using the provided controls (e.g., pinch-to-zoom gestures, buttons).
3. **Verify Increased Size:**
    - Confirm that the size of the print page increases as intended.
    - Check for any visual artifacts or distortion in the content due to scaling.
4. **Scale Down the Page Size:**
    - On the print page, attempt to scale down the size using the provided controls.
5. **Verify Decreased Size:**
    - Confirm that the size of the print page decreases as intended.
    - Check for any visual artifacts or distortion in the content due to scaling.

**Expected Results:**

- The application should successfully launch without errors.
- The user should be able to navigate to the print page from the application's main screen.
- Scaling up the page size should increase the size of the print page without visual issues.
- Scaling down the page size should decrease the size of the print page without visual issues.

**Postconditions:**

- The user can successfully navigate to the print page and adjust the size as desired.

### **Test Case 8: Changing Theme Color and Dynamic Button State in Settings**

**Objective:** To verify that users can successfully change the theme color and toggle the dynamic button state in the Settings tab.

**Preconditions:**

- Any.do is installed on the device.
- The user has logged in to their [Any.do](http://any.do/) account.

**Test Steps:**

1. **Open the Settings Tab:**
    - Launch the Any.do application on the device.
    - Navigate to the "Settings" tab.
2. **Change Theme Color:**
    - Locate the option to change the theme color.
    - Choose the "Black," "White," or "Blue" theme color.
3. **Verify Theme Color Change:**
    - Confirm that the application's theme color changes according to the selected option.
    - Check for any visual artifacts or issues with the selected theme.
4. **Toggle Dynamic Button State:**
    - Find the option to toggle the dynamic button state (e.g., on/off).
    - Toggle the state of the dynamic button to the opposite setting.
5. **Verify Dynamic Button State Change:**
    - Confirm that the dynamic button state changes as intended.
    - Check for any visual indicators confirming the dynamic button's new state.

**Expected Results:**

- The Any.do application should launch without errors.
- The user should be able to navigate to the "Settings" tab from the application's main screen.
- Changing the theme color should reflect the selected color throughout the application without introducing visual issues.
- Toggling the dynamic button state should change the state of the dynamic button as intended.

**Postconditions:**

- The user can successfully change the theme color and toggle the dynamic button state in the Settings tab.

### **Test Case 9: Managing Notifications in Notification Tab**

**Objective:** To verify that users can successfully manage notifications in the Notification tab by utilizing the options available in the three dots menu.

**Preconditions:**

- Any.do is installed on the device.
- The user has logged in to their [Any.do](http://any.do/) account.

**Test Steps:**

1. **Open the Notification Tab:**
    - Launch the Any.do application on the device.
    - Navigate to the "Notification" tab.
2. **Explore Three Dots Menu Options:**
    - Locate the three dots menu on the Notification tab.
    - Click on the menu to reveal options.
3. **Select "All" Option:**
    - Choose the "All" option from the menu.
    - Observe the impact on the displayed tips and notifications.
4. **Verify "All" Option Reflection:**
    - Confirm that all tips and notifications, regardless of importance, are displayed.
    - Ensure there are no missing or hidden notifications.
5. **Select "Important" Option:**
    - Choose the "Important" option from the menu.
    - Observe the impact on the displayed tips and notifications.
6. **Verify "Important" Option Reflection:**
    - Confirm that only important tips and notifications are displayed.
    - Ensure there are no non-important notifications visible.
7. **Select "Clear All Notifications" Option:**
    - Choose the "Clear All Notifications" option from the menu.
    - Observe the impact on the displayed tips and notifications.
8. **Verify "Clear All Notifications" Option Reflection:**
    - Confirm that all tips and notifications are cleared or removed.
    - Ensure there are no remaining tips or notifications after selecting this option.

**Expected Results:**

- The Any.do application should launch without errors.
- The user should be able to navigate to the "Notification" tab from the application's main screen.
- Selecting the "All" option should display all tips and notifications.
- Selecting the "Important" option should display only important tips and notifications.
- Selecting the "Clear All Notifications" option should remove all tips and notifications.

**Postconditions:**

- Notifications are successfully managed in the Notification tab, reflecting the chosen options from the three dots menu.

### **Test Case 10: Testing the Filter Feature in Settings**

**Objective:** To verify that users can successfully utilize the filter feature in the Settings menu.

**Preconditions:**

- Any.do is installed on the device.
- The user has logged in to their [Any.do](http://any.do/) account.

**Test Steps:**

1. **Open the Settings Menu:**
    - Launch the Any.do application on the device.
    - Navigate to the "Settings" menu.
2. **Locate the Filter Feature:**
    - Identify the presence of the filter feature within the Settings menu.
3. **Activate the Filter:**
    - Enable the filter feature by selecting or toggling the corresponding option.
4. **Apply a Filter Criterion:**
    - Choose a filter criterion (e.g., task category, due date, priority) from the available options.
5. **Verify Filter Application:**
    - Confirm that the filter is successfully applied to the relevant content (e.g., task list, notifications).
    - Ensure that only items meeting the specified filter criterion are displayed.
6. **Deactivate the Filter:**
    - Disable the filter feature by selecting or toggling the corresponding option.
7. **Verify Filter Deactivation:**
    - Confirm that the filter is deactivated.
    - Ensure that all items are displayed without any filtering.

**Expected Results:**

- The Any.do application should launch without errors.
- The user should be able to navigate to the "Settings" menu from the application's main screen.
- The filter feature should be present within the Settings menu.
- Activating the filter and applying a criterion should display only relevant items.
- Deactivating the filter should revert to displaying all items.

**Postconditions:**

- Users can successfully utilize the filter feature in the Settings menu to customize the displayed content based on their preferences.

### **Test Case 11: Accessing Support Options in Settings**

**Objective:** To verify that users can successfully navigate to the support section in the Settings page and access "FAQ," "Report a Bug," and "Feature Request" options.

**Preconditions:**

- Any.do is installed on the device.
- The user has logged in to their [Any.do](http://any.do/) account.

**Test Steps:**

1. **Open the Settings Menu:**
    - Launch the Any.do application on the device.
    - Navigate to the "Settings" menu.
2. **Navigate to Support:**
    - Find and select the "Support" option within the Settings menu.
3. **Access "FAQ":**
    - Within the Support section, locate and click on the "FAQ" option.
4. **Verify "FAQ" Page:**
    - Confirm that the "FAQ" page opens successfully.
    - Check for the presence of frequently asked questions and relevant information.
5. **Access "Report a Bug":**
    - Return to the Support section.
    - Locate and click on the "Report a Bug" option.
6. **Verify "Report a Bug" Page:**
    - Confirm that the "Report a Bug" page opens successfully.
    - Check for the presence of a bug reporting form or relevant instructions.
7. **Access "Feature Request":**
    - Return to the Support section.
    - Locate and click on the "Feature Request" option.
8. **Verify "Feature Request" Page:**
    - Confirm that the "Feature Request" page opens successfully.
    - Check for the presence of a feature request form or relevant instructions.

**Expected Results:**

- The Any.do application should launch without errors.
- Users should be able to navigate to the "Settings" menu from the application's main screen.
- The "Support" option should be available within the Settings menu.
- Clicking on "FAQ" should open the FAQ page with relevant information.
- Clicking on "Report a Bug" should open the bug reporting page or provide instructions.
- Clicking on "Feature Request" should open the feature request page or provide instructions.

**Postconditions:**

- Users can successfully access support options in the Settings page to find answers to frequently asked questions, report bugs, and submit feature requests.

### **Test Case 12: Navigating to Any.do Community Page and Accessing Community Features**

**Objective:** To verify that users can successfully navigate to the Any.do Community page in the Settings and access features such as "I Love Any.do," "Become a Super User - test new features!," and "Help translate Any.do."

**Preconditions:**

- Any.do is installed on the device.
- The user has logged in to their [Any.do](http://any.do/) account.

**Test Steps:**

1. **Open the Settings Menu:**
    - Launch the Any.do application on the device.
    - Navigate to the "Settings" menu.
2. **Navigate to Any.do Community:**
    - Find and select the "Any.do Community" option within the Settings menu.
3. **Access "I Love Any.do":**
    - Within the Any.do Community page, locate and click on the "I Love Any.do" option.
4. **Verify "I Love Any.do" Page:**
    - Confirm that the "I Love Any.do" page opens successfully.
    - Check for any relevant content, testimonials, or community engagement features.
5. **Access "Become a Super User - Test New Features!":**
    - Return to the Any.do Community page.
    - Locate and click on the "Become a Super User - Test New Features!" option.
6. **Verify "Become a Super User" Page:**
    - Confirm that the "Become a Super User" page opens successfully.
    - Check for information on becoming a super user, testing new features, and any associated benefits.
7. **Access "Help Translate Any.do":**
    - Return to the Any.do Community page.
    - Locate and click on the "Help Translate Any.do" option.
8. **Verify "Help Translate Any.do" Page:**
    - Confirm that the "Help Translate Any.do" page opens successfully.
    - Check for information on contributing to the translation of Any.do and relevant instructions.

**Expected Results:**

- The Any.do application should launch without errors.
- Users should be able to navigate to the "Settings" menu from the application's main screen.
- The "Any.do Community" option should be available within the Settings menu.
- Clicking on "I Love Any.do" should open a page with relevant community engagement content.
- Clicking on "Become a Super User - Test New Features!" should open a page with information on becoming a super user and testing new features.
- Clicking on "Help Translate Any.do" should open a page with information on contributing to the translation of Any.do.

**Postconditions:**

- Users can successfully navigate to the Any.do Community page in the Settings and access community features, including expressing their love for Any.do, becoming a super user, and contributing to translations.

### **Test Case 13: Changing Language in Language and Speech Settings**

**Objective:** To verify that users can successfully navigate to the Language and Speech page in the Settings, change the language of the application, and confirm the language change.

**Preconditions:**

- Any.do is installed on the device.
- The user has logged in to their [Any.do](http://any.do/) account.

**Test Steps:**

1. **Open the Settings Menu:**
    - Launch the Any.do application on the device.
    - Navigate to the "Settings" menu.
2. **Navigate to Language and Speech:**
    - Find and select the "Language and Speech" option within the Settings menu.
3. **Change the Language:**
    - Locate the language settings within the Language and Speech page.
    - Choose a different language from the available options.
4. **Verify Language Change:**
    - Confirm that the language of the application changes as intended.
    - Check for any visual indicators or prompts confirming the language change.

**Expected Results:**

- The Any.do application should launch without errors.
- Users should be able to navigate to the "Settings" menu from the application's main screen.
- The "Language and Speech" option should be available within the Settings menu.
- Changing the language should result in the application's content being displayed in the newly selected language.
- Visual indicators or prompts should confirm the successful change of language.

**Postconditions:**

- Users can successfully navigate to the Language and Speech page in the Settings, change the language of the application, and experience the application in the newly selected language.

### **Test Case 14: Setting Day Reset Time in Settings**

**Objective:** To verify that users can successfully navigate to the Day Reset Time settings in the application's Settings menu and configure the desired reset time.

**Preconditions:**

- Any.do is installed on the device.
- The user has logged in to their [Any.do](http://any.do/) account.

**Test Steps:**

1. **Open the Settings Menu:**
    - Launch the Any.do application on the device.
    - Navigate to the "Settings" menu.
2. **Navigate to Day Reset Time:**
    - Find and select the "Day Reset Time" option within the Settings menu.
3. **Configure Reset Time:**
    - Within the Day Reset Time settings, locate the options to configure the reset time.
    - Choose a specific time for the day reset.
4. **Verify Reset Time Configuration:**
    - Confirm that the selected time for the day reset is saved successfully.
    - Check for any visual indicators or prompts confirming the reset time configuration.

**Expected Results:**

- The Any.do application should launch without errors.
- Users should be able to navigate to the "Settings" menu from the application's main screen.
- The "Day Reset Time" option should be available within the Settings menu.
- Configuring the reset time should result in the selected time being saved.
- Visual indicators or prompts should confirm the successful configuration of the day reset time.

**Postconditions:**

- Users can successfully navigate to the Day Reset Time settings in the Settings menu, configure the desired reset time, and have the change reflected in the application's behavior.

## Test Cases with priority

#1 

(Essentials for the user include logging in and the support page)|

Test Case 1: Login with Valid Credentials

Test Case 6: Cross-Device Sync 

Test Case 11: Accessing Support Options in Settings

#2 

(Basic functionality of the application, any task-related test case)

Test Case 2: Task Creation and Confirmation

Test Case 3: Task Reminder Notification Validation

Test Case 4: Task Deletion

Test Case 5: Offline Task Management

Test Case 8: Changing Theme Color and Dynamic Button State in Settings

#3

(Featured functionality, maybe number of users don’t affect them)

Test Case 7: Scaling Print Page Size

Test Case 9: Managing Notifications in Notification Tab

Test Case 10: Testing the Filter Feature in Settings

Test Case 13: Changing Language in Language and Speech Settings

Test Case 14: Setting Day Reset Time in Settings

#4 

(Not All Users are interested in such pages)

Test Case 12: Navigating to Any.do Community Page and Accessing Community




# Bugs

### #1 **Bug Report**

**Bug Title:** Application crashes when pressing "Report a Bug"

**Reproducible Steps:**

1. Open the Any.do application on the device.
2. Navigate to the "Settings" menu.
3. Click on the "Support" option.
4. Select "Report a Bug."

**Attachments:**

**Affected Devices:**

- Device: IPhone 8
- Os: iOS 16.7.2

**Network:**

- Home Wifi, 4G, Offline mode

**Severity:**

- Major

**Priority:**

- High

**Impact:**

- No users will be allowed to report any bugs - if found

### 

### #2 **Bug Report**

**Bug Title:** Dynamic Theme Issue - Only Black Theme Applied

**Reproducible Steps:**

1. Open the Any.do application on the device.
2. Navigate to the "Settings" tab.
3. Find and select the option to change the theme color.
4. Choose the "Black" theme color.
5. Toggle the dynamic button state to "ON."
6. Attempt to change the theme color to "White" or any other color.

**Attachments:**

**Affected Devices:**

- Device: IPhone 8
- Os: iOS 16.7.2

**Network:**

- Home Wifi, 4G, Offline mode

**Severity:**

- Minor

**Priority:**

- Medium

**Impact:**

- Users are unable to apply themes other than the black theme when the dynamic theme is turned ON, impacting customization options.

### #3 **Bug Report**

**Bug Title:** Scaling Down the Page Size Not Working

**Reproducible Steps:**

1. Open the Any.do application on the device.
2. Navigate to the print page.
3. Attempt to scale down the page size using the provided controls.

**Attachments:**

**Affected Devices:**

- Device: IPhone 8
- Os: iOS 16.7.2

**Network:**

- Home Wifi, 4G, Offline mode

**Severity:**

- Minor

**Priority:**

- Medium

**Impact:**

- Users are unable to scale down the page size on the print page, affecting the ability to adjust the content size.

### #4 **Bug Report**

**Bug Title:** Notification Filter hidden after changing it to important

**Reproducible Steps:**

1. Launch the Any.do application on the device.
2. Navigate to the "Notification" tab.
3. Locate the three dots menu on the Notification tab.
4. Click on the menu to reveal options.
5. Choose the "Important" option from the menu.
6. Observe the impact on the tips page.

**Attachments:**

**Affected Devices:**

- Device: IPhone 8
- Os: iOS 16.7.2

**Network:**

- Home Wifi, 4G, Offline mode

**Severity:**

- Minor

**Priority:**

- Low

**Impact:**

- Users are unable to open again the options for the notification except refreshing the page or turn to the notification section

### #5 **Bug Report**

**Bug Title:** Filter Feature is not Working

**Reproducible Steps:**

1. Launch the Any.do application on the device.
2. Navigate to the "Settings" menu.
3. Identify the presence of the filter feature within the Settings menu.

**Attachments:**

**Affected Devices:**

- Device: IPhone 8
- Os: iOS 16.7.2

**Network:**

- Home Wifi, 4G, Offline mode

**Severity:**

- Critical

**Priority:**

- Medium

**Impact:**

- Filter feature not actually working

### #6 **Bug Report**

**Bug Title:** Language Change require page refreshing.

**Reproducible Steps:**

1. Launch the Any.do application on the device.
2. Navigate to the "Settings" menu.
3. Find and select the "Language and Speech" option within the Settings menu.
4. Locate the language settings within the Language and Speech page.
5. Choose a different language from the available options.

**Attachments:**

**Affected Devices:**

- Device: IPhone 8
- Os: iOS 16.7.2

**Network:**

- Home Wifi, 4G, Offline mode

**Severity:**

- Minor

**Priority:**

- Low

**Impact:**

- The language isn’t as changed in the page, you should go to the homepage, and then open the tasks page again for it to be changed visually.

### #7 **Bug Report (UX)**

**Bug Title:** Language Change require page refreshing.

**Reproducible Steps:**

1. Launch the Any.do application on the device.
2. Navigate to the "Settings" menu.
3. Find and press the "Day Reset Time" option within the Settings menu.

**Attachments:**

**Affected Devices:**

- Device: IPhone 8
- Os: iOS 16.7.2

**Network:**

- Home Wifi, 4G, Offline mode

**Severity:**

- Minor

**Priority:**

- Low

**Impact:**

- The section for editing Day Reset Time does not close if navigated to other pages and you can access the background page in the app




# UI Automation

# Test cases

1. **Valid Login:**
    - Test Steps:
        1. Open the login page.
        2. Enter valid username and password.
        3. Click on the login button.
    - Expected Outcome: User should be successfully logged in and redirected to the next page.
2. **Invalid Login:**
    - Test Steps:
        1. Open the login page.
        2. Enter an invalid username and an invalid password.
        3. Click on the login button.
    - Expected Outcome: User should not be able to log in, and an error message stating "Username and password do not match" should be displayed.
3. **Logout:**
    - Test Steps:
        1. Open the login page.
        2. Enter valid username and password.
        3. Click on the login button.
        4. Open the hidden menu bar.
        5. Click on the logout button.
    - Expected Outcome: User should be successfully logged in and logged out successfully.
4. **Add Product to Cart:**
    - Test Steps:
        1. Open the login page.
        2. Enter valid username and password.
        3. Click on the login button.
        4. Add a product to the cart.
    - Expected Outcome: The product should be successfully added to the cart, and the cart indicator should reflect the addition.
5. **Remove Product from Cart:**
    - Test Steps:
        1. Open the login page.
        2. Enter valid username and password.
        3. Click on the login button.
        4. Add a product to the cart.
        5. Remove the product from the cart.
    - Expected Outcome: The product should be successfully removed from the cart, and the cart indicator should not display any badge.
6. **Navigate to About Page:**
    - Test Steps:
        1. Open the login page.
        2. Enter valid username and password.
        3. Click on the login button.
        4. Open the side menu.
        5. Navigate to the About page.
    - Expected Outcome: User should be successfully logged in and redirected to the About page.