# Github-login-test
> Automated test of login feature on https://github.com/ created using Selenium, WebDriver Manager, unittest and Page Object Model
 
## Technologies
```
* Python 3.8.10
* WebDriver Manager
```

#### Environment
```
The most recent version of Chrome browser (determined by WebDriver Manager)
Ubuntu 20.04.3
```

#### Setup
```
pip install selenium
pip install webdriver-manager
```

## Test Case 1 - Login with valid credentials

#### Steps
```
1. Open https://github.com/
2. Click "Sign in"
3. Enter valid username in the username field
4. Enter valid password in the password field
5. Click "Submit"
```

#### Expected result
```
User is logged in to their Github account
```


#### Actual result
```
As expected
```

## Test Case 2 - Login with invalid credentials

#### Steps
```
1. Open https://github.com/
2. Click "Sign in"
3. Enter "User" in the username field
4. Enter "User123" in the password field
5. Click "Submit"
```

#### Expected result
```
Login fails. "Incorrect username or password." message is displayed
```


#### Actual result
```
As expected
