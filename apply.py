# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.common.exceptions import NoSuchElementException
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import os

# # Read job URLs from a file
# def read_job_urls(filename="jobs.txt"):
#     with open(filename, "r") as file:
#         return [line.strip() for line in file if line.strip()]

# # Personal details for job applications
# JOB_APP = {
#     "first_name": "Foo",
#     "last_name": "Bar",
#     "email": "test@test.com",
#     "phone": "123-456-7890",
#     "resume": os.path.abspath("resume.pdf"),  # Ensure full path
#     "linkedin": "https://www.linkedin.com/in/foobar",
#     "location": "San Francisco, CA, USA",
#     "school": "MIT",
#     "degree": "Bachelor's",
#     "work_auth": "Authorized to work for any employer"
# }

# def apply_greenhouse(url):
#     print(f"Applying to: {url}")
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     driver.get(url)
#     time.sleep(3)

#     try:
#         # Check if there's an "Apply" or "Apply Now" button and click it
#         apply_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Apply') or contains(text(), 'Apply Now')]")
#         if apply_buttons:
#             print("Clicking 'Apply' button...")
#             apply_buttons[0].click()
#             time.sleep(2)  # Wait for the page to scroll

#         # If no "Apply" button, manually scroll down
#         else:
#             print("No 'Apply' button found. Scrolling to the bottom...")
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(2)

#         # Fill out the form fields
#         driver.find_element(By.ID, "first_name").send_keys(JOB_APP["first_name"])
#         driver.find_element(By.ID, "last_name").send_keys(JOB_APP["last_name"])
#         driver.find_element(By.ID, "email").send_keys(JOB_APP["email"])
#         driver.find_element(By.ID, "phone").send_keys(JOB_APP["phone"])

#         # Upload resume
#         driver.find_element(By.ID, "resume").send_keys(JOB_APP["resume"])

#         # Fill LinkedIn if present
#         try:
#             driver.find_element(By.XPATH, "//label[contains(.,'LinkedIn')]").send_keys(JOB_APP["linkedin"])
#         except NoSuchElementException:
#             pass

#         # Fill location
#         try:
#             loc = driver.find_element(By.ID, "job_application_location")
#             loc.send_keys(JOB_APP["location"])
#             loc.send_keys(Keys.DOWN, Keys.RETURN)
#         except NoSuchElementException:
#             pass

#         # Select school, degree, and work authorization if options exist
#         for field in ["school", "degree", "work_auth"]:
#             try:
#                 driver.find_element(By.XPATH, f"//option[contains(text(),'{JOB_APP[field]}')]").click()
#             except NoSuchElementException:
#                 pass

#         # Click submit button
#         try:
#             driver.find_element(By.ID, "submit_app").click()
#             print("Application submitted successfully.")
#         except NoSuchElementException:
#             print("Submit button not found.")

#     except NoSuchElementException as e:
#         print(f"Error: {e}")

#     time.sleep(5)
#     driver.quit()

# if __name__ == "__main__":
#     job_urls = read_job_urls("jobs.txt")  # Read job URLs from the file
#     for job_url in job_urls:
#         apply_greenhouse(job_url)  # Apply to each job


# -------------------------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.common.exceptions import NoSuchElementException
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import os

# # Read job URLs from a file
# def read_job_urls(filename="jobs.txt"):
#     with open(filename, "r") as file:
#         return [line.strip() for line in file if line.strip()]

# # Personal details for job applications
# JOB_APP = {
#     "first_name": "Foo",
#     "last_name": "Bar",
#     "email": "test@test.com",
#     "phone": "123-456-7890",
#     "resume": os.path.abspath("resume.pdf"),  # Ensure full path
#     "linkedin": "https://www.linkedin.com/in/foobar",
#     "location": "San Francisco, CA, USA",
#     "school": "MIT",
#     "degree": "Bachelor's",
#     "work_auth": "Authorized to work for any employer"
# }

# def apply_greenhouse(url):
#     print(f"Applying to: {url}")
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     driver.get(url)
#     time.sleep(3)

#     try:
#         # Check if there's an "Apply" or "Apply Now" button and click it
#         apply_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Apply') or contains(text(), 'Apply Now')]")
#         if apply_buttons:
#             print("Clicking 'Apply' button...")
#             apply_buttons[0].click()
#             time.sleep(2)  # Wait for the page to scroll

#         # If no "Apply" button, manually scroll down
#         else:
#             print("No 'Apply' button found. Scrolling to the bottom...")
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(2)

#         # Fill out the form fields
#         driver.find_element(By.ID, "first_name").send_keys(JOB_APP["first_name"])
#         driver.find_element(By.ID, "last_name").send_keys(JOB_APP["last_name"])
#         driver.find_element(By.ID, "email").send_keys(JOB_APP["email"])
#         driver.find_element(By.ID, "phone").send_keys(JOB_APP["phone"])

#         # Upload resume
#         driver.find_element(By.ID, "resume").send_keys(JOB_APP["resume"])

#         # Fill LinkedIn if present
#         try:
#             driver.find_element(By.XPATH, "//label[contains(.,'LinkedIn')]").send_keys(JOB_APP["linkedin"])
#         except NoSuchElementException:
#             pass

#         # Fill location
#         try:
#             loc = driver.find_element(By.ID, "job_application_location")
#             loc.send_keys(JOB_APP["location"])
#             loc.send_keys(Keys.DOWN, Keys.RETURN)
#         except NoSuchElementException:
#             pass

#         # Select school, degree, and work authorization if options exist
#         for field in ["school", "degree", "work_auth"]:
#             try:
#                 driver.find_element(By.XPATH, f"//option[contains(text(),'{JOB_APP[field]}')]").click()
#             except NoSuchElementException:
#                 pass

#         # Click submit button
#         try:
#             driver.find_element(By.ID, "submit_app").click()
#             print("Application submitted successfully.")
#         except NoSuchElementException:
#             print("Submit button not found.")

#     except NoSuchElementException as e:
#         print(f"Error: {e}")

#     time.sleep(5)
#     driver.quit()

# if __name__ == "__main__":
#     job_urls = read_job_urls("jobs.txt")  # Read job URLs from the file
#     for job_url in job_urls:
#         apply_greenhouse(job_url)  # Apply to each job




# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
# from webdriver_manager.chrome import ChromeDriverManager

# # Load job URLs from a text file
# def load_job_urls(filename="jobs.txt"):
#     with open(filename, "r") as file:
#         return [line.strip() for line in file.readlines() if line.strip()]

# # Job application details
# JOB_APP = {
#     "first_name": "Foo",
#     "last_name": "Bar",
#     "email": "test@test.com",
#     "phone": "123-456-7890",
#     "resume": os.path.abspath("resume.pdf"),  # Ensure full path
#     "linkedin": "https://www.linkedin.com/in/foobar",
#     "location": "San Francisco, CA, USA",
#     "school": "MIT",
#     "degree": "Bachelor's",
#     "work_auth": "Authorized to work for any employer"
# }

# # Apply to a Greenhouse job
# def apply_greenhouse(url):
#     print(f"\n🔹 Applying to: {url}")

#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     wait = WebDriverWait(driver, 10)

#     try:
#         driver.get(url)
#         time.sleep(3)

#         # Try clicking "Apply" or "Apply Now" button if available
#         try:
#             apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]")
#             apply_button.click()
#             print("✅ 'Apply' button found and clicked.")
#         except NoSuchElementException:
#             print("❌ No 'Apply' button found. Scrolling to the bottom...")
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(2)

#         # Fill out the application form
#         try:
#             driver.find_element(By.ID, "first_name").send_keys(JOB_APP["first_name"])
#             driver.find_element(By.ID, "last_name").send_keys(JOB_APP["last_name"])
#             driver.find_element(By.ID, "email").send_keys(JOB_APP["email"])
#             driver.find_element(By.ID, "phone").send_keys(JOB_APP["phone"])
#             print("✅ Basic details filled.")
#         except NoSuchElementException:
#             print("❌ Basic fields not found.")

#         # Upload resume
#         try:
#             resume_input = driver.find_element(By.ID, "resume")
#             driver.execute_script("arguments[0].scrollIntoView();", resume_input)
#             time.sleep(1)
#             resume_input.send_keys(JOB_APP["resume"])
#             print("✅ Resume uploaded.")
#         except (NoSuchElementException, ElementNotInteractableException):
#             print("❌ Resume upload field not interactable or missing.")

#         # Fill LinkedIn (if available)
#         try:
#             linkedin_input = driver.find_element(By.XPATH, "//input[contains(@id, 'linkedin')]")
#             linkedin_input.send_keys(JOB_APP["linkedin"])
#             print("✅ LinkedIn profile added.")
#         except NoSuchElementException:
#             print("❌ LinkedIn field not found.")

#         # Fill location (with scroll fix)
#         try:
#             loc = wait.until(EC.presence_of_element_located((By.ID, "job_application_location")))
#             driver.execute_script("arguments[0].scrollIntoView();", loc)
#             time.sleep(1)
#             loc.send_keys(JOB_APP["location"])
#             loc.send_keys(Keys.DOWN, Keys.RETURN)
#             print("✅ Location filled.")
#         except (NoSuchElementException, ElementNotInteractableException):
#             print("❌ Location field not interactable. Using JavaScript to set value.")
#             driver.execute_script("document.getElementById('job_application_location').value = arguments[0];", JOB_APP["location"])

#         # Select school
#         try:
#             driver.find_element(By.XPATH, f"//option[contains(text(),'{JOB_APP['school']}')]").click()
#             print("✅ School selected.")
#         except NoSuchElementException:
#             print("❌ School field not found.")

#         # Select degree
#         try:
#             driver.find_element(By.XPATH, f"//option[contains(text(),'{JOB_APP['degree']}')]").click()
#             print("✅ Degree selected.")
#         except NoSuchElementException:
#             print("❌ Degree field not found.")

#         # Select work authorization
#         try:
#             driver.find_element(By.XPATH, f"//option[contains(text(),'{JOB_APP['work_auth']}')]").click()
#             print("✅ Work authorization selected.")
#         except NoSuchElementException:
#             print("❌ Work authorization field not found.")

#         # Submit application
#         try:
#             submit_button = driver.find_element(By.ID, "submit_app")
#             submit_button.click()
#             print("🎉 Application submitted successfully!")
#         except NoSuchElementException:
#             print("❌ Submit button not found.")

#     except Exception as e:
#         print(f"⚠️ Error: {e}")

#     finally:
#         time.sleep(5)  # Wait before closing
#         driver.quit()

# # Main script execution
# if __name__ == "__main__":
#     job_urls = load_job_urls()

#     print(f"\n✅ Found {len(job_urls)} job(s) to apply for.\n")
    
#     for index, job_url in enumerate(job_urls, start=1):
#         print(f"\n🔹 Applying for job {index}/{len(job_urls)}: {job_url}")
#         apply_greenhouse(job_url)
#         print("⏳ Waiting 5 seconds before next application...\n")
#         time.sleep(5)  # Pause between applications


# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
# from webdriver_manager.chrome import ChromeDriverManager

# # Load job URLs from a text file
# def load_job_urls(filename="jobs.txt"):
#     with open(filename, "r") as file:
#         return [line.strip() for line in file.readlines() if line.strip()]

# # Job application details
# JOB_APP = {
#     "first_name": "Foo",
#     "last_name": "Bar",
#     "email": "test@test.com",
#     "phone": "123-456-7890",
#     "resume": os.path.abspath("resume.pdf"),  # Ensure full path
#     "linkedin": "https://www.linkedin.com/in/foobar",
#     "location": "San Francisco, CA, USA",
#     "school": "MIT",
#     "degree": "Bachelor's",
#     "work_auth": "Authorized to work for any employer"

# def apply_greenhouse(driver, url):
#     print(f"\n🔹 Applying to: {url}")
#     driver.get(url)
#     time.sleep(3)

#     try:
#         # Click 'Apply' button if available
#         try:
#             apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]")
#             apply_button.click()
#             print("✅ 'Apply' button found and clicked.")
#         except NoSuchElementException:
#             print("❌ No 'Apply' button found.")

#         # Fill out the form
#         fields = {
#             "first_name": "first_name",
#             "last_name": "last_name",
#             "email": "email",
#             "phone": "phone",
#             "linkedin": "linkedin",
#             "location": "job_application_location"
#         }
        
#         for key, field_id in fields.items():
#             try:
#                 field = driver.find_element(By.ID, field_id)
#                 field.clear()
#                 field.send_keys(JOB_APP[key])
#                 print(f"✅ {key} filled.")
#             except NoSuchElementException:
#                 print(f"⚠️ {key} field not found. Please fill it manually.")

#         # Upload Resume
#         try:
#             resume_input = driver.find_element(By.ID, "resume")
#             driver.execute_script("arguments[0].scrollIntoView();", resume_input)
#             resume_input.send_keys(JOB_APP["resume"])
#             print("✅ Resume uploaded.")
#         except NoSuchElementException:
#             print("⚠️ Resume upload field not found. Please upload manually.")

#         print("🛑 Waiting for manual input. Please fill missing fields and submit.")
#         input("Press Enter after manually submitting the application...")
#         time.sleep(2)

#     except Exception as e:
#         print(f"⚠️ Error: {e}")

# # Main execution
# if __name__ == "__main__":
#     job_urls = load_job_urls()
#     print(f"\n✅ Found {len(job_urls)} job(s) to apply for.\n")
    
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
    
#     for index, job_url in enumerate(job_urls, start=1):
#         print(f"\n🔹 Applying for job {index}/{len(job_urls)}: {job_url}")
#         apply_greenhouse(driver, job_url)
#         print("⏳ Waiting 2 seconds before next application...\n")
#         time.sleep(2)
    
#     driver.quit()
#     print("✅ All applications completed!")



# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
# from webdriver_manager.chrome import ChromeDriverManager

# # Load job URLs from a text file
# def load_job_urls(filename="jobs.txt"):
#     with open(filename, "r") as file:
#         return [line.strip() for line in file.readlines() if line.strip()]

# # Job application details
# JOB_APP = {
#     "first_name": "Foo",
#     "last_name": "Bar",
#     "email": "test@test.com",
#     "phone": "123-456-7890",
#     "resume": os.path.abspath("resume.pdf"),  # Ensure full path
#     "linkedin": "https://www.linkedin.com/in/foobar",
#     "location": "San Francisco, CA, USA",
#     "school": "MIT",
#     "degree": "Bachelor's",
#     "work_auth": "Authorized to work for any employer"
# }

# def apply_greenhouse(driver, url):
#     print(f"\n🔹 Applying to: {url}")
#     driver.get(url)
#     time.sleep(3)

#     try:
#         # Click 'Apply' button if available
#         try:
#             apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]")
#             apply_button.click()
#             print("✅ 'Apply' button found and clicked.")
#             time.sleep(2)  # Wait for form to load
#         except NoSuchElementException:
#             print("❌ No 'Apply' button found.")

#         # Fill out the form **ONLY ONCE** (before manual input)
#         fields = {
#             "first_name": "first_name",
#             "last_name": "last_name",
#             "email": "email",
#             "phone": "phone"
#         }

#         for key, field_id in fields.items():
#             try:
#                 field = driver.find_element(By.ID, field_id)
#                 field.clear()
#                 field.send_keys(JOB_APP[key])
#                 print(f"✅ {key} filled.")
#             except NoSuchElementException:
#                 print(f"⚠️ {key} field not found. Please fill it manually.")

#         # Upload Resume
#         try:
#             resume_input = driver.find_element(By.ID, "resume")
#             driver.execute_script("arguments[0].scrollIntoView();", resume_input)
#             resume_input.send_keys(JOB_APP["resume"])
#             print("✅ Resume uploaded.")
#         except NoSuchElementException:
#             print("⚠️ Resume upload field not found. Please upload manually.")

#         print("🛑 Waiting for manual input. Please fill missing fields and submit.")
#         time.sleep(10)  # Give user time to manually complete missing fields

#         # Locate the Submit button and click it
#         try:
#             submit_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Submit application')]"))
#             )
#             driver.execute_script("arguments[0].scrollIntoView();", submit_button)
#             time.sleep(2)  # Small delay before clicking
            
#             try:
#                 submit_button.click()
#                 print("✅ 'Submit application' button clicked.")
#                 time.sleep(5) 
#             except ElementClickInterceptedException:
#                 print("⚠️ Submit button not clickable immediately, retrying...")
#                 driver.execute_script("arguments[0].click();", submit_button)  # JavaScript Click

#             # Wait for confirmation (either a success message or a URL change)
#             WebDriverWait(driver, 10).until(
#                 EC.or_(
#                     EC.url_changes(url),
#                     EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Thank you')]"))
#                 )
#             )
#             print("🎉 Application submitted successfully!")

#         except NoSuchElementException:
#             print("❌ 'Submit application' button not found.")
#         except Exception as e:
#             print(f"⚠️ Error while submitting: {e}")

#     except Exception as e:
#         print(f"⚠️ Error: {e}")

# # Main execution
# if __name__ == "__main__":
#     job_urls = load_job_urls()
#     print(f"\n✅ Found {len(job_urls)} job(s) to apply for.\n")
    
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
    
#     for index, job_url in enumerate(job_urls, start=1):
#         print(f"\n🔹 Applying for job {index}/{len(job_urls)}: {job_url}")
#         apply_greenhouse(driver, job_url)
#         print("⏳ Waiting 2 seconds before next application...\n")
#         time.sleep(12)
    
#     driver.quit()
#     print("✅ All applications completed!")


# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
# from webdriver_manager.chrome import ChromeDriverManager

# # Load job URLs from a text file
# def load_job_urls(filename="jobs.txt"):
#     with open(filename, "r") as file:
#         return [line.strip() for line in file.readlines() if line.strip()]

# # Job application details
# JOB_APP = {
#     "first_name": "Foo",
#     "last_name": "Bar",
#     "email": "test@test.com",
#     "phone": "123-456-7890",
#     "resume": os.path.abspath("resume.pdf"),
#     "linkedin": "https://www.linkedin.com/in/foobar",
#     "location": "San Francisco, CA, USA",
#     "school": "MIT",
#     "degree": "Bachelor's",
#     "work_auth": "Authorized to work for any employer"
# }

# def apply_greenhouse(driver, url):
#     print(f"\n🔹 Applying to: {url}")
#     driver.get(url)
#     time.sleep(3)

#     try:
#         # Click 'Apply' button if available
#         try:
#             apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]")
#             apply_button.click()
#             print("✅ 'Apply' button found and clicked.")
#         except NoSuchElementException:
#             print("❌ No 'Apply' button found.")

#         # Fill out the form
#         fields = {
#             "first_name": "first_name",
#             "last_name": "last_name",
#             "email": "email",
#             "phone": "phone",
#             "linkedin": "linkedin",
#             "location": "job_application_location"
#         }
        
#         for key, field_id in fields.items():
#             try:
#                 field = driver.find_element(By.ID, field_id)
#                 field.clear()
#                 field.send_keys(JOB_APP[key])
#                 print(f"✅ {key} filled.")
#             except NoSuchElementException:
#                 print(f"⚠️ {key} field not found. Please fill it manually.")

#         # Upload Resume
#         try:
#             resume_input = driver.find_element(By.ID, "resume")
#             driver.execute_script("arguments[0].scrollIntoView();", resume_input)
#             resume_input.send_keys(JOB_APP["resume"])
#             print("✅ Resume uploaded.")
#         except NoSuchElementException:
#             print("⚠️ Resume upload field not found. Please upload manually.")
    

#         # print("🛑 Waiting for manual input. Please fill missing fields and submit.")
#         # input("Press Enter after manually submitting the application...")  
#         # time.sleep(2)
#         # i added below code 

#         # Detect Required Fields and Fill them Dynamically
#         try:
#             error_elements = driver.find_elements(By.CLASS_NAME, "helper-text--error")
#             for error in error_elements:
#                 field_id = error.get_attribute("id").replace("-error", "")
#                 try:
#                     field = driver.find_element(By.ID, field_id)
#                     field.clear()
#                     field.send_keys("N/A")  # Default value for required fields
#                     print(f"✅ Filled missing field: {field_id}")
#                 except NoSuchElementException:
#                     print(f"⚠️ Could not find field {field_id}, skipping.")
#         except Exception as e:
#             print(f"⚠️ Error checking required fields: {e}")

#         print("🛑 Waiting for manual input. Please fill missing fields and submit.")
#         input("Press Enter after manually submitting the application...")  
#         time.sleep(2)


#         # Locate and click the 'Submit application' button
#         try:
#             submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit application')]")
#             driver.execute_script("arguments[0].scrollIntoView();", submit_button)
#             WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit_button))
#             submit_button.click()
#             print("✅ 'Submit application' button clicked.")
#             time.sleep(3)  # Wait for form submission
#         except NoSuchElementException:
#             print("❌ 'Submit application' button not found. Please check manually.")
#         except ElementClickInterceptedException:
#             print("⚠️ Submit button not clickable immediately, retrying...")
#             driver.execute_script("arguments[0].click();", submit_button)
#             time.sleep(2)

#     except Exception as e:
#         print(f"⚠️ Error while submitting: {e}")

# # Main execution
# if __name__ == "__main__":
#     job_urls = load_job_urls()
#     print(f"\n✅ Found {len(job_urls)} job(s) to apply for.\n")
    
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
    
#     for index, job_url in enumerate(job_urls, start=1):
#         print(f"\n🔹 Applying for job {index}/{len(job_urls)}: {job_url}")
#         apply_greenhouse(driver, job_url)
#         print("⏳ Waiting 2 seconds before next application...\n")
#         time.sleep(2)
    
#     driver.quit()
#     print("✅ All applications completed!")


# import os
# import time
# import random
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
# from webdriver_manager.chrome import ChromeDriverManager

# # Load job URLs from a text file
# def load_job_urls(filename="jobs.txt"):
#     with open(filename, "r") as file:
#         return [line.strip() for line in file.readlines() if line.strip()]

# # Random sleep function to avoid detection
# def random_sleep(min_time=2, max_time=8):
#     sleep_time = random.uniform(min_time, max_time)
#     print(f"⏳ Sleeping for {round(sleep_time, 2)} seconds...")
#     time.sleep(sleep_time)

# # Job application details
# JOB_APP = {
#     "first_name": "Foo",
#     "last_name": "Bar",
#     "email": "test@test.com",
#     "phone": "123-456-7890",
#     "resume": os.path.abspath("resume.pdf"),  # Ensure file exists
#     "linkedin": "https://www.linkedin.com/in/foobar",
#     "location": "San Francisco, CA, USA",
#     "school": "MIT",
#     "degree": "Bachelor's",
#     "work_auth": "Authorized to work for any employer"
# }

# def apply_greenhouse(driver, url):
#     print(f"\n🔹 Applying to: {url}")
#     driver.get(url)
#     random_sleep()

#     try:
#         # Click 'Apply' button if available
#         try:
#             apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]")
#             apply_button.click()
#             print("✅ 'Apply' button found and clicked.")
#         except NoSuchElementException:
#             print("❌ No 'Apply' button found.")

#         random_sleep()

#         # Define fields to fill
#         fields = {
#             "first_name": "first_name",
#             "last_name": "last_name",
#             "email": "email",
#             "phone": "phone",
#             "linkedin": "linkedin",
#             "location": "job_application_location"
#         }

#         # Fill out known fields
#         for key, field_id in fields.items():
#             try:
#                 field = driver.find_element(By.ID, field_id)
#                 field.clear()
#                 field.send_keys(JOB_APP[key])
#                 print(f"✅ {key} filled.")
#             except NoSuchElementException:
#                 print(f"⚠️ {key} field not found. It might be optional.")

#         random_sleep()

#         # Upload Resume Automatically
#         try:
#             resume_input = driver.find_element(By.XPATH, "//input[@type='file']")
#             driver.execute_script("arguments[0].scrollIntoView();", resume_input)
#             resume_input.send_keys(JOB_APP["resume"])
#             print("✅ Resume uploaded automatically.")
#         except NoSuchElementException:
#             print("⚠️ Resume upload field not found. Skipping resume upload.")

#         random_sleep()

#         # # Check for missing required fields
#         # try:
#         #     error_elements = driver.find_elements(By.CLASS_NAME, "helper-text--error")
#         #     if error_elements:
#         #         print("\n🛑 Some required fields are missing! Please fill them manually.")
#         #         input("➡️ Press Enter after manually completing the form...\n")
#         # except Exception as e:
#         #     print(f"⚠️ Error checking required fields: {e}")

#         # Check for missing required fields and wait for manual input
#         wait_time = 0
#         while True:
#             try:
#                 error_elements = driver.find_elements(By.CLASS_NAME, "helper-text--error")
#                 if not error_elements:
#                     print("✅ All required fields filled. Proceeding with submission.")
#                     break  # Exit loop when no errors found

#                 if wait_time == 0:
#                     print("\n🛑 Some required fields are missing! Please fill them manually.")
                
#                 time.sleep(20)  # Wait 5 seconds before checking again
#                 wait_time += 20
                
#                 if wait_time >= 30:  # Allow at least 30 seconds for manual input
#                     print(f"⏳ Waiting... {wait_time} seconds elapsed. Fill the missing details.")
                    
#             except Exception as e:
#                 print(f"⚠️ Error checking required fields: {e}")

#         # Click the 'Submit application' button
#         try:
#             submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit application')]")
#             driver.execute_script("arguments[0].scrollIntoView();", submit_button)
#             WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit_button))
#             submit_button.click()
#             print("✅ 'Submit application' button clicked.")
#         except NoSuchElementException:
#             print("❌ 'Submit application' button not found. Skipping this job.")
#         except ElementClickInterceptedException:
#             print("⚠️ Submit button not clickable immediately, retrying...")
#             driver.execute_script("arguments[0].click();", submit_button)

#         random_sleep()

#     except Exception as e:
#         print(f"⚠️ Error while submitting: {e}")

# # Main execution
# if __name__ == "__main__":
#     job_urls = load_job_urls()
#     print(f"\n✅ Found {len(job_urls)} job(s) to apply for.\n")
    
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
    
#     for index, job_url in enumerate(job_urls, start=1):
#         print(f"\n🔹 Applying for job {index}/{len(job_urls)}: {job_url}")
#         apply_greenhouse(driver, job_url)
#         print("⏳ Waiting before next application...\n")
#         random_sleep()

#     driver.quit()
#     print("✅ All applications completed!")


import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager

# Load job URLs from a text file
def load_job_urls(filename="jobs.txt"):
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

# Random sleep function
def random_sleep(min_time=2, max_time=8):
    sleep_time = random.uniform(min_time, max_time)
    print(f"⏳ Sleeping for {round(sleep_time, 2)} seconds...")
    time.sleep(sleep_time)

# Job application details
JOB_APP = {
    "first_name": "Foo",
    "last_name": "Bar",
    "email": "pkarimulla9@gmail.com",
    "phone": "123-456-7890",
    "resume": os.path.abspath("resume.pdf"),
    "linkedin": "https://www.linkedin.com/in/foobar",
    "location": "San Francisco, CA, USA",
    "school": "MIT",
    "degree": "Bachelor's",
    "work_auth": "Authorized to work for any employer"
}

def submit_button_click(driver):
    """Attempts to click the 'Submit application' button."""
    try:
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit application')]")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit_button))
        submit_button.click()
        print("✅ 'Submit application' button clicked.")
    except NoSuchElementException:
        print("❌ 'Submit application' button not found. Skipping this job.")
    except ElementClickInterceptedException:
        print("⚠️ Submit button not clickable immediately, retrying...")
        driver.execute_script("arguments[0].click();", submit_button)

    random_sleep()

def apply_greenhouse(driver, url):
    print(f"\n🔹 Applying to: {url}")
    driver.get(url)
    random_sleep()

    try:
        # Click 'Apply' button if available
        try:
            apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply')]")
            apply_button.click()
            print("✅ 'Apply' button found and clicked.")
        except NoSuchElementException:
            print("❌ No 'Apply' button found.")

        random_sleep()

        # Define fields to fill
        fields = {
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "email",
            "phone": "phone",
            "linkedin": "linkedin",
            "location": "job_application_location"
        }

        # Fill out known fields
        for key, field_id in fields.items():
            try:
                field = driver.find_element(By.ID, field_id)
                field.clear()
                field.send_keys(JOB_APP[key])
                print(f"✅ {key} filled.")
            except NoSuchElementException:
                print(f"⚠️ {key} field not found. It might be optional.")

        random_sleep()

        # Upload Resume Automatically
        try:
            resume_input = driver.find_element(By.XPATH, "//input[@type='file']")
            driver.execute_script("arguments[0].scrollIntoView();", resume_input)
            resume_input.send_keys(JOB_APP["resume"])
            print("✅ Resume uploaded automatically.")
        except NoSuchElementException:
            print("⚠️ Resume upload field not found. Skipping resume upload.")

        random_sleep()

        # ✅ **OTP Handling - Added Here**
        otp_fields = driver.find_elements(By.XPATH, "//input[starts-with(@id, 'security-input-')]")
        if otp_fields:
            print("🔒 OTP verification detected. Fetching OTP...")
            otp_code = fetch_latest_otp(JOB_APP["email"], JOB_APP["email_password"], JOB_APP["imap_server"])
            if otp_code:
                enter_otp(driver, otp_code)

        # Wait for manual input if required fields are missing
        wait_time = 0
        while True:
            try:
                print("error code is getting called ------------------------------------")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit application')]")
                driver.execute_script("arguments[0].scrollIntoView();", submit_button)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit_button))
                submit_button.click()
                try:
                    submit_button.click()
                except Exception:
                    driver.execute_script("arguments[0].click();", submit_button)
                print("--------------------iam waiting 8 sec-0-----------------------")
                time.sleep(8)

                error_elements = driver.find_elements(By.CLASS_NAME, "helper-text--error")
                print(error_elements )
                if not error_elements:
                    print("✅ All required fields filled. Proceeding with submission.")
                    break  # Exit loop when no errors found

                if wait_time == 0:
                    print("\n🛑 Some required fields are missing! Please fill them manually.")

                random_sleep(15, 30)  # Wait between 15-30 seconds before checking again
                wait_time += 20

                if wait_time >= 60:  # Maximum wait time of 60 seconds
                    print(f"⏳ Waiting... {wait_time} seconds elapsed. Fill the missing details.")

            except Exception as e:
                print(f"⚠️ Error checking required fields: {e}")

        # Click the 'Submit application' button
        submit_button_click(driver)

    except Exception as e:
        print(f"⚠️ Error while submitting: {e}")

# Main execution
# if __name__ == "__main__":
#     job_urls = load_job_urls()
#     print(f"\n✅ Found {len(job_urls)} job(s) to apply for.\n")

#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)

#     for index, job_url in enumerate(job_urls, start=1):
#         print(f"\n🔹 Applying for job {index}/{len(job_urls)}: {job_url}")
#         apply_greenhouse(driver, job_url)
#         print("⏳ Waiting before next application...\n")
#         random_sleep()

#     driver.quit()
#     print("✅ All applications completed!")

if __name__ == "__main__":
    job_urls = load_job_urls()
    print(f"\n✅ Found {len(job_urls)} job(s) to apply for.\n")

    for index, job_url in enumerate(job_urls, start=1):
        print(f"\n🔹 Applying for job {index}/{len(job_urls)}: {job_url}")

        # Start a new browser session for each application
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        try:
            apply_greenhouse(driver, job_url)
            print("✅ Application submitted successfully.")
        except Exception as e:
            print(f"⚠️ Error while applying for {job_url}: {e}")

        driver.quit()  # Close browser before moving to the next job
        print("⏳ Waiting before next application...\n")
        random_sleep()

    print("✅ All applications completed!")

