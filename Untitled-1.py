
#login
driver = webdriver.Edge(service=service, options=options)
try:
    # Navigate to login page
    driver.get("https://login.taobao.com/havanaone/login/login.htm?bizName=taobao&sub=true&redirectURL=https%3A%2F%2Fliveplatform.taobao.com%2Frestful%2Findex%2Flive%2Foverview")
    print('a1')
    # Wait for page to load
    #WebDriverWait(driver, 10)
    #.until(
    #    EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-automation-id='email']"))
    #)
    print('a')
    time.sleep(5)
    # Find and fill email field
    email_field = driver.find_element(By.CSS_SELECTOR, "input[name='fm-login-id']")
    email_field.clear()
    email_field.send_keys("nike官方旗舰店:直播")
    print('b')
    # Find and fill password field
    password_field = driver.find_element(By.CSS_SELECTOR, "input[name='fm-login-password']")
    password_field.clear()
    password_field.send_keys("Fangbo303080")  # Replace with actual password
    print('c')
    # Find and click login button
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    print('d')
    login_button.click()
   
    # Wait for login to complete (either success or failure)
    time.sleep(5)
    
    # Check if login was successful
    current_url = driver.current_url
    print(f"Current URL: {current_url}")
    
    if "login" not in current_url.lower():
        print("✅ Login successful!")
        print("You were redirected to:", current_url)
        
        # You can now access protected content
        page_source = driver.page_source
        print("Page title:", driver.title)
        
    else:
        print("❌ Login failed - still on login page")
        # Check for error messages
        error_elements = driver.find_elements(By.CSS_SELECTOR, "[data-automation-id='errorMessage']")
        for error in error_elements:
            print("Error message:", error.text)
        
        # Save screenshot for debugging
        driver.save_screenshot("login_error.png")
        print("Screenshot saved as login_error.png")

finally:
    # Keep browser open for inspection, remove if you want it to close automatically
    input("Press Enter to close browser...")
    driver.quit()