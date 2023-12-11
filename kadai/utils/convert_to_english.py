def convert_prefecture_to_english(prefecture):
    prefecture_dict = {
        "全国": "National",
        "北海道": "Hokkaido",
        "青森": "Aomori",
        "岩手": "Iwate",
        "宮城": "Miyagi",
        "秋田": "Akita",
        "山形": "Yamagata",
        "福島": "Fukushima",
        "茨城": "Ibaraki",
        "栃木": "Tochigi",
        "群馬": "Gunma",
        "埼玉": "Saitama",
        "千葉": "Chiba",
        "東京": "Tokyo",
        "神奈川": "Kanagawa",
        "新潟": "Niigata",
        "富山": "Toyama",
        "石川": "Ishikawa",
        "福井": "Fukui",
        "山梨": "Yamanashi",
        "長野": "Nagano",
        "岐阜": "Gifu",
        "静岡": "Shizuoka",
        "愛知": "Aichi",
        "三重": "Mie",
        "滋賀": "Shiga",
        "京都": "Kyoto",
        "大阪": "Osaka",
        "兵庫": "Hyogo",
        "奈良": "Nara",
        "和歌山": "Wakayama",
        "鳥取": "Tottori",
        "島根": "Shimane",
        "岡山": "Okayama",
        "広島": "Hiroshima",
        "山口": "Yamaguchi",
        "徳島": "Tokushima",
        "香川": "Kagawa",
        "愛媛": "Ehime",
        "高知": "Kochi",
        "福岡": "Fukuoka",
        "佐賀": "Saga",
        "長崎": "Nagasaki",
        "熊本": "Kumamoto",
        "大分": "Oita",
        "宮崎": "Miyazaki",
        "鹿児島": "Kagoshima",
        "沖縄": "Okinawa"
    }

    return prefecture_dict.get(prefecture, "Unknown")


def convert_column_to_english(term) -> str:
    japanese_to_english = {
        '名目県内総生産': 'Nominal Prefectural GDP',
        '市': 'City',
        '町': 'Town',
        '村': 'Village',
        '総面積': 'Total Area',
        '0歳から14歳': '0 to 14 Years Old',
        '15歳から64歳': '15 to 64 Years Old',
        '65歳以上': '65 Years and Older'
    }

    return japanese_to_english.get(term, term)