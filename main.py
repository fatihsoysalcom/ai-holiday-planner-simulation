import random

def get_holiday_plan(user_preferences):
    """
    Simulates an AI-powered holiday planning assistant.
    Analyzes user preferences and suggests a tailored holiday plan.
    """
    preferences_lower = user_preferences.lower()

    # Define various holiday profiles with potential destinations, activities, and budget estimates.
    # This dictionary represents the "knowledge base" that an AI would learn from data.
    holiday_profiles = {
        "beach_relax": {
            "keywords": ["beach", "relax", "sun", "sea", "swim", "dinlenmek", "sahil"],
            "destination": "Maldivler",
            "activities": "Güneşlenme, şnorkelle dalış, spa bakımları, gün batımının tadını çıkarma.",
            "budget_estimate": "Yüksek (lüks tatil köyleri)",
            "tip": "Nihai rahatlama için her şey dahil tatil köylerini düşünün."
        },
        "adventure_explore": {
            "keywords": ["adventure", "explore", "hike", "mountains", "trek", "thrill", "macera", "dağ", "keşif"],
            "destination": "Patagonya",
            "activities": "Doğa yürüyüşü, trekking, vahşi yaşam gözlemi, buzul turları.",
            "budget_estimate": "Orta ila Yüksek (ekipman, rehberler)",
            "tip": "Katmanlı giysiler hazırlayın ve değişen hava koşullarına hazırlıklı olun."
        },
        "cultural_city": {
            "keywords": ["city", "culture", "history", "museums", "food", "explore", "şehir", "kültür", "tarih", "yemek"],
            "destination": "Roma",
            "activities": "Tarihi yerleri (Kolezyum, Vatikan) ziyaret etme, sanat galerileri, yerel mutfağı tatma, yürüyüş turları.",
            "budget_estimate": "Orta (konaklama, yemek, giriş ücretleri)",
            "tip": "Uzun kuyruklardan kaçınmak için popüler cazibe merkezlerine önceden rezervasyon yapın."
        },
        "family_fun": {
            "keywords": ["family", "kids", "fun", "theme park", "child-friendly", "aile", "çocuk", "eğlence"],
            "destination": "Orlando, Florida",
            "activities": "Tema parkları (Disney World, Universal Studios), su parkları, aile dostu gösteriler.",
            "budget_estimate": "Yüksek (biletler, konaklama, yemek)",
            "tip": "Park ziyaretlerinizi stratejik olarak planlayın ve varsa hızlı geçişleri kullanın."
        },
        "budget_friendly": {
            "keywords": ["budget", "cheap", "affordable", "save money", "bütçe", "ucuz", "ekonomik"],
            "destination": "Güneydoğu Asya (örn. Tayland)",
            "activities": "Yerel pazarları keşfetme, sokak yemekleri, tapınaklar, plajlar (daha az turistik olanlar).",
            "budget_estimate": "Düşük ila Orta (hosteller, pansiyonlar)",
            "tip": "Daha iyi fırsatlar ve daha az kalabalık için sezon dışında seyahat edin."
        }
    }

    # Simulate AI's preference matching using keyword analysis (simple NLP simulation).
    # In a real AI, this would involve more sophisticated NLP models (e.g., embeddings, sentiment analysis).
    matched_profile = None
    max_matches = 0

    for profile_name, profile_data in holiday_profiles.items():
        current_matches = sum(1 for keyword in profile_data["keywords"] if keyword in preferences_lower)
        if current_matches > max_matches:
            max_matches = current_matches
            matched_profile = profile_data

    if matched_profile:
        # Generate a personalized plan based on the matched profile.
        # This is where the "AI" synthesizes information to provide a tailored recommendation.
        plan = f"\nHarika bir seçim! Tercihlerinize göre size özel bir tatil planı hazırladım:\n" \
               f"Hedef: {matched_profile['destination']}\n" \
               f"Yapılacaklar: {matched_profile['activities']}\n" \
               f"Tahmini Bütçe: {matched_profile['budget_estimate']}\n" \
               f"Ek İpucu: {matched_profile['tip']}\n" \
               f"Umarım bu plan tatil beklentilerinizin ötesinde bir deneyim sunar!"
    else:
        # Fallback for when no specific profile matches strongly.
        # A real AI might ask clarifying questions or suggest a general popular option.
        fallback_options = list(holiday_profiles.values())
        random_suggestion = random.choice(fallback_options)
        plan = f"\nTercihlerinizi tam olarak anlayamadım, ancak size genel bir öneride bulunabilirim:\n" \
               f"Belki de {random_suggestion['destination']} sizin için harika bir seçenek olabilir!\n" \
               f"Orada {random_suggestion['activities']} gibi aktiviteler yapabilirsiniz.\n" \
               f"Tahmini Bütçe: {random_suggestion['budget_estimate']}\n" \
               f"Ek İpucu: {random_suggestion['tip']}\n" \
               f"Daha fazla detay vermek isterseniz, size daha özel bir plan hazırlayabilirim."

    return plan

if __name__ == "__main__":
    print("Yapay Zeka Destekli Tatil Planlayıcısına Hoş Geldiniz!")
    print("Hayalinizdeki tatili tanımlayın (örneğin: 'sahilde dinlenmek istiyorum', 'macera dolu dağ gezisi', 'kültürel bir şehir turu', 'çocuklarla aile tatili', 'bütçe dostu bir seyahat').")
    
    user_input = input("Tercihleriniz nelerdir? ")
    
    # Call the "AI" function to get the personalized plan.
    holiday_plan = get_holiday_plan(user_input)
    
    print(holiday_plan)
