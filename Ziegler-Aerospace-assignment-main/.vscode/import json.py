import json

# Your data
data = [
    {
        "PersonAssessmentId": 1,
        "PeopleKey": 924509,
        "AssessedSkillId": "80004546",
        "PSRSkillId": 122920,
        "ProficiencyCd": 5,
        "ProficiencyScaleCd": 1,
        "SkillId": "80004546",
        "CompoundSkillId": "80010231",
        "SkillCollectionId": "80008020",
        "AssessmentStatusId": 2,
        "AssessmentTypeId": 2,
        "AssessmentMethodId": 3,
        "SourceSystemId": 8,
        "ValidationStatusId": 4,
        "SourceSystemAssessmentMethodIdentifierId": None,
        "CompletionDttm": 1613605658000,
        "AssessorPeopleKey": 734102,
        "LatestInd": 1,
        "SourceTransactionId": 572305,
        "ExperienceInMonths": 90,
        "LastUsedYear": 2021,
        "DeletedInd": 0,
        "CreateUserId": "CAMSPDC",
        "CreateDttm": 1431150190000,
        "UpdateUserId": "CAMSPDC",
        "UpdateDttm": 1614563836000,
        "LevelOfInterestId": None,
        "Duration": None,
        "DataPrivacySettingId": 1
    }
]

# Initialize an empty list to store repeated data
repeated_data = []

# Repeat the data 1000 times
for i in range(1, 1001):
    # Copy the data and update the "PersonAssessmentId"
    for item in data:
        new_item = item.copy()
        new_item["PersonAssessmentId"] = i
        repeated_data.append(new_item)

# Print the repeated data
print(json.dumps(repeated_data, indent=4))
