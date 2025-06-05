def time_to_seconds(time_str):
    """Convert 'h:m' string to total seconds."""
    try:
        parts = time_str.strip().split(":")
        if len(parts) != 2:
            return None
        hours = int(parts[0])
        minutes = int(parts[1])
        return hours * 3600 + minutes * 60
    except:
        return None

def seconds_to_hms(seconds):
    """Convert seconds to 'HH : MM : SS' format."""
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d} : {m:02d} : {s:02d}"

def generate_study_plan(time_have_str, lesson_count_str):
    total_seconds = time_to_seconds(time_have_str)
    if total_seconds is None:
        return "Khatâ: Lotfan zaman ra be sorat 'hour:minute' vared konid (mesal: 2:35)."

    try:
        lesson_count = int(lesson_count_str)
        if lesson_count <= 0:
            return "Khatâ: Tedad dars-ha bayad mosbat bashad."
    except:
        return "Khatâ: Tedad dars-ha ra be dorosti vared konid."

    break_ratio = 0.15
    break_count = max(lesson_count - 1, 0)
    total_units = lesson_count + break_count * break_ratio

    seconds_per_unit = total_seconds / total_units
    lesson_time_sec = seconds_per_unit
    break_time_sec = seconds_per_unit * break_ratio

    plan = f"🌟 Barname Darsi 🌟\n\n"
    plan += f"📚 Tedad dars-ha: {lesson_count}\n"
    plan += f"⏰ Zaman koll: {seconds_to_hms(total_seconds)} (HH : MM : SS)\n"
    plan += f"🔍 Esteraahat: {int(break_ratio * 100)}%\n\n"
    plan += "📋 Barname zamani:\n"

    total_used_sec = 0
    for i in range(lesson_count):
        plan += f"▶️ Dars {i+1}: {seconds_to_hms(int(lesson_time_sec))} (HH : MM : SS)\n"
        total_used_sec += lesson_time_sec
        if i < lesson_count - 1:
            plan += f"   ⏸️ Esteraahat: {seconds_to_hms(int(break_time_sec))} (HH : MM : SS)\n"
            total_used_sec += break_time_sec

    plan += f"\n⌛ Zaman koll ba esteraahat: {seconds_to_hms(int(total_used_sec))} (HH : MM : SS)\n"
    plan += "\n💡 No'kat motâle'e:\n"
    plan += "• Dar mohiti arâm va bedoon havas-pardazi motâle'e kon\n"
    plan += "• Az Pomodoro estefâde kon (25 daghighe motâle'e, 5 daghighe esteraahat)\n"
    plan += "• Kholâse-nevisi ro farâmoush nakon\n"

    return plan

if __name__ == "__main__":
    time_input = input("Zaman ra be sorat 'saat:daghighe' vared konid (mesal 2:35): ")
    lesson_input = input("Tedad dars-ha ra vared konid: ")

    result = generate_study_plan(time_input, lesson_input)
    print("\n" + result)
