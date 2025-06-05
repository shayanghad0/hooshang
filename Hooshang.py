def generate_study_plan(time_have, lesson_count):
    try:
        time_have_float = float(time_have)
        lesson_count_int = int(lesson_count)
    except ValueError:
        return "Khatâ: Lotfan adad dorost vared konid."

    if lesson_count_int <= 0 or time_have_float <= 0:
        return "Khatâ: Meghdâr-ha bayad mosbat bashand."

    break_ratio = 0.15  # 15% baraye esteraahat
    break_count = max(lesson_count_int - 1, 0)
    total_unit = lesson_count_int + break_count * break_ratio

    unit_time = time_have_float / total_unit
    lesson_time = unit_time
    break_time = unit_time * break_ratio

    study_plan = f"🌟 Barname Darsi 🌟\n\n"
    study_plan += f"📚 Tedad dars-ha: {lesson_count_int}\n"
    study_plan += f"⏰ Zaman koll: {time_have_float} sâ'at\n"
    study_plan += f"🔍 Esteraahat: {int(break_ratio * 100)}%\n\n"
    study_plan += "📋 Barname zamani:\n"

    total_used = 0
    for i in range(lesson_count_int):
        study_plan += f"▶️ Dars {i+1}: {lesson_time:.2f} sâ'at\n"
        total_used += lesson_time
        if i < lesson_count_int - 1:
            study_plan += f"   ⏸️ Esteraahat: {break_time:.2f} sâ'at\n"
            total_used += break_time

    study_plan += f"\n⌛ Zaman koll ba esteraahat: {total_used:.2f} sâ'at\n"

    study_plan += "\n💡 No'kat motâle'e:\n"
    study_plan += "• Dar mohiti arâm va bedoon havas-pardazi motâle'e kon\n"
    study_plan += "• Az Pomodoro estefâde kon (25 daghighe motâle'e, 5 daghighe esteraahat)\n"
    study_plan += "• Kholâse-nevisi ro farâmoush nakon\n"

    return study_plan

if __name__ == "__main__":
    time_have = input("Zaman dar sâ'at ra vared konid: ")
    lesson_count = input("Tedad dars-ha ra vared konid: ")

    result = generate_study_plan(time_have, lesson_count)
    print("\n" + result)
