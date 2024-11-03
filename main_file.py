import sys
from utils import load_excel, send_email
from keyword_actions import KeywordActions
import pandas as pd
def execute_tests(sheet_name):
    actions = KeywordActions()
    results = []

    # Load the test case sheet
    df = load_excel(sheet_name)

    for index, row in df.iterrows():
        step_name = row['Step Name']
        keyword = row['Keyword']
        locator = row['Locator']
        locator_value = row['Locator Value']
        input_value = row['Input Value']

        try:
            if keyword == "Open":
                actions.open_browser(input_value)
            elif keyword == "Click":
                actions.click(locator_value)
            elif keyword == "Type":
                actions.type(locator_value, input_value)
            elif keyword == "Assert":
                actions.assert_text(locator_value, input_value)

            results.append((step_name, "Passed"))
        except Exception as e:
            results.append((step_name, f"Failed: {str(e)}"))

    actions.close_browser()
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the sheet name as an argument.")
        sys.exit(1)

    sheet_name = sys.argv[1]
    results = execute_tests(sheet_name)

    # Prepare the result report
    report_df = pd.DataFrame(results, columns=["Step Name", "Result"])
    report_df.to_excel("report.xlsx", index=False)

    # Send the report via email
    send_email("Test Report", f"Results for {sheet_name}:\n\n{report_df.to_string(index=False)}")