import pandas as pd


def calculate_demographic_data(print_data=True):
    # Leer los datos desde el archivo CSV
    df = pd.read_csv("adult.data.csv")

    # 1. ¿Cuántas personas de cada raza están representadas en este dataset?
    race_count = df["race"].value_counts()

    # 2. ¿Cuál es la edad promedio de los hombres (Male)?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. ¿Cuál es el porcentaje de personas que tienen un título de Bachillerato (Bachelors)?
    percentage_bachelors = round(
        (df["education"] == "Bachelors").sum() / len(df) * 100, 1
    )

    # 4. Porcentaje de personas con y sin educación avanzada que ganan >50K
    # Educación avanzada: Bachelors, Masters, o Doctorate
    higher_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )
    lower_education = ~higher_education

    # Porcentaje de los que tienen educación avanzada y ganan >50K
    higher_education_rich = round(
        (df[higher_education]["salary"] == ">50K").sum()
        / len(df[higher_education])
        * 100,
        1,
    )

    # Porcentaje de los que NO tienen educación avanzada y ganan >50K
    lower_education_rich = round(
        (df[lower_education]["salary"] == ">50K").sum()
        / len(df[lower_education])
        * 100,
        1,
    )

    # 5. ¿Cuál es el número mínimo de horas que una persona trabaja por semana?
    min_work_hours = df["hours-per-week"].min()

    # 6. ¿Qué porcentaje de las personas que trabajan el mínimo de horas ganan >50K?
    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        (num_min_workers["salary"] == ">50K").sum()
        / len(num_min_workers)
        * 100,
        1,
    )

    # 7. ¿Qué país tiene el mayor porcentaje de personas que ganan >50K y cuál es ese porcentaje?
    # Contamos el total de personas por país
    country_total = df["native-country"].value_counts()
    # Contamos cuántos ganan >50K por país
    country_rich = df[df["salary"] == ">50K"]["native-country"].value_counts()

    # Calculamos el porcentaje por país
    country_percentage = (country_rich / country_total) * 100

    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 8. Identificar la ocupación más popular para los que ganan >50K en India
    india_rich = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    top_IN_occupation = india_rich["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print(
            "Country with highest percentage of rich:", highest_earning_country
        )
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
