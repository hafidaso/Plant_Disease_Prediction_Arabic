import streamlit as st
import tensorflow as tf
import numpy as np

# Function for TensorFlow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to batch
    predictions = model.predict(input_arr)
    confidence = np.max(predictions)
    return np.argmax(predictions), confidence

# Plant disease descriptions
disease_descriptions = {
    'Apple___Apple_scab': {
        "description": "مرض قشرة التفاح ناتج عن فطر، Venturia inaequalis، وهو مرض خطير يؤثر على أشجار التفاح والتفاح البري (جنس مالوس) وينتشر بسرعة وسهولة. عادةً، ستلاحظ هذا المرض أولاً في أوائل الربيع، عندما تساعد الأمطار والرياح ودرجات الحرارة الباردة في انتشار الأبواغ الفطرية.",
        "medicine": "استخدام مبيدات الفطريات مثل Captan أو Myclobutanil."
    },
    'Apple___Black_rot': {
        "description": "العفن الأسود هو مرض مهم يؤثر على التفاح ناتج عن الفطر Botryosphaeria obtusa. يصيب فطر العفن الأسود مجموعة واسعة من أشجار الخشب الصلب، بما في ذلك التفاح والكمثرى. وغالبًا ما تكون الأشجار المصابة مصدر عدوى للكتل الأصغر المجاورة التي تحمل ثمارًا. الأنواع الشمالية، وكورتلاند، وجالا، وهاني كريسب، وماكنتوش، وإمباير هي الأكثر تعرضًا للإصابة، على الرغم من أن جميع أصناف التفاح عرضة لذلك.",
        "medicine": "استخدام مبيدات الفطريات مثل Thiophanate-methyl أو Captan."
    },
    'Apple___Cedar_apple_rust': {
        "description": "صدأ الأرز والتفاح - المرض شائع بشكل أكبر على أشجار التفاح والتفاح البري - بقع الأوراق تكون صفراء أولاً ثم تتحول إلى برتقالية زاهية حمراء، غالبًا مع حافة حمراء زاهية.",
        "medicine": "استخدام مبيدات الفطريات مثل Myclobutanil أو Mancozeb."
    },
    'Apple___healthy': {
        "description": "تفاح صحي خالٍ من الأمراض.",
        "medicine": "لا يحتاج إلى علاج."
    },
    'Blueberry___healthy': {
        "description": "توت صحي خالٍ من الأمراض.",
        "medicine": "لا يحتاج إلى علاج."
    },
    'Cherry_(including_sour)___Powdery_mildew': {
        "description": "العفن المسحوق للكرز الحلو والحامض ناتج عن الفطر Podosphaera clandestina، وهو فطر حيوي متطفل. غالبًا ما تتأثر أصناف الكرز الحلو (Prunus avium) في منتصف الموسم وآخره، مما يجعلها غير قابلة للتسويق بسبب تغطيها بنمو فطري أبيض على سطح الكرز.",
        "medicine": "استخدام مبيدات الفطريات مثل Sulfur أو Potassium bicarbonate."
    },
    'Cherry_(including_sour)___healthy': {
        "description": "كرز صحي خالٍ من الأمراض.",
        "medicine": "لا يحتاج إلى علاج."
    },
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
        "description": "البقعة الورقية الرمادية (GLS) هي مرض فطري يصيب الأوراق يؤثر على الذرة، المعروفة أيضًا باسم الذرة. يُعتبر GLS واحدًا من أهم الأمراض التي تحد من الغلة في الذرة على مستوى العالم. هناك Pathogenين فطريين يسببان GLS: Cercospora zeae-maydis وCercospora zeina.",
        "medicine": "استخدام مبيدات الفطريات مثل Azoxystrobin أو Pyraclostrobin."
    },
    'Corn_(maize)___Common_rust_': {
        "description": "الصدأ الشائع ناتج عن الفطر Puccinia sorghi ويحدث في كل موسم نمو. نادرًا ما يكون مصدر قلق في الذرة الهجينة.",
        "medicine": "استخدام مبيدات الفطريات مثل Mancozeb أو Chlorothalonil."
    },
    'Corn_(maize)___Northern_Leaf_Blight': {
    "description": "داء بقعة ورقة الذرة الشمالية (NCLB) أو داء بقعة ورقة تركيكم (TLB) هو مرض ورقي يصيب الذرة (الذرة) ناتج عن الفطر Exserohilum turcicum، وهو الشكل اللاجنسي للفطر Setosphaeria turcica. مع آثاره المميزة على شكل سيجار، يمكن أن يسبب هذا المرض فقدانًا كبيرًا في الغلة في الهجن الحساسة من الذرة.",
    "medicine": "استخدام مبيدات الفطريات مثل Propiconazole أو Azoxystrobin."
    },
    'Corn_(maize)___healthy': {
        "description": "ذرة صحية خالية من الأمراض.",
        "medicine": "لا يحتاج إلى علاج."
    },
    'Grape___Black_rot': {
        "description": "العفن الأسود للعنب هو مرض فطري ناتج عن فطر من نوع الأسكوميست، Guignardia bidwellii، الذي يهاجم كروم العنب خلال الطقس الحار والرطب. نشأ العفن الأسود للعنب في شرق أمريكا الشمالية، ولكنه يحدث الآن في أجزاء من أوروبا وأمريكا الجنوبية وآسيا.",
        "medicine": "استخدام مبيدات الفطريات مثل Myclobutanil أو Mancozeb."
    },
    'Grape___Esca_(Black_Measles)': {
        "description": "تتمثل الأعراض الورقية لمرض إسكا في ظهور خطوط بين الأوردة . تبدأ هذه الخطوط باللون الأحمر الداكن في الأصناف الحمراء والأصفر في الأصناف البيضاء، ثم تجف وتصبح نخرية. قد تظهر الأعراض الورقية في أي وقت خلال موسم النمو، ولكنها أكثر انتشارًا خلال شهري يوليو وأغسطس.",
        "medicine": "استخدام مبيدات الفطريات مثل Sodium arsenite أو Trifloxystrobin."
    },
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        "description": "مرض احتراق الأوراق، المعروف أيضًا ببقعة ورقة إيزاريوبسيس (Pseudocercospora vitis) على العنب (Vitus sp.)، يتسم بظهور بقع بنفسجية-بنية متفرقة وزاوية إلى حد ما على السطح العلوي للأوراق. وهناك بقع بنية أقل وضوحًا على السطح السفلي للأوراق. تظهر العديد من البقع البنفسجية-البنية المتفرقة وزاوية الشكل إلى حد ما على السطح العلوي للأوراق.",
        "medicine": "استخدام مبيدات الفطريات مثل Copper hydroxide أو Mancozeb."
    },
    'Grape___healthy': {
        "description": "عنب صحي خالٍ من الأمراض.",
        "medicine": "لا يحتاج إلى علاج."
    },
    'Orange___Haunglongbing_(Citrus_greening)': {
        "description": "مرض تليين الحمضيات، المعروف أيضًا باسم هوانغ لونغ بينغ (HLB)، هو عدوى بكتيرية تصيب نباتات الحمضيات. يُعتبر واحدًا من أخطر أمراض الحمضيات في العالم. بمجرد أن تصاب الأشجار، تموت معظمها في غضون بضع سنوات. لا يوجد علاج.",
        "medicine": "لا يوجد علاج فعال حاليًا."
    },
    'Peach___Bacterial_spot': {
        "description": "تسبب بقعة بكتيرية البكتيريا Xanthomonas campestris pv. pruni. يحدث المرض غالبًا في لونغ آيلند، ولكن تم الإبلاغ عنه أحيانًا في وادي هدسون وغرب نيويورك. تظهر الأعراض على الثمار في البداية كبقع بنية دائرية صغيرة على سطح الثمرة.",
        "medicine": "استخدام مبيدات البكتيريا مثل Copper hydroxide أو Streptomycin."
    },
    'Peach___healthy': {
        "description": "خوخ صحي خالٍ من الأمراض.",
        "medicine": "لا يحتاج إلى علاج."
    },
    'Pepper,_bell___Bacterial_spot': {
        "description": "تسبب بقعة الأوراق البكتيرية البكتيريا Xanthomonas campestris pv. vesicatoria، وهي أكثر الأمراض شيوعًا وتدميرًا للفلفل في شرق الولايات المتحدة. إنها بكتيريا سلبية الغرام، على شكل عصيات، يمكن أن تعيش في البذور وبقايا النباتات من موسم إلى آخر.",
        "medicine": "استخدام مبيدات البكتيريا مثل Copper hydroxide أو Streptomycin."
    },
    'Pepper,_bell___healthy': {
        "description": "فلفل صحي خالٍ من الأمراض.",
        "medicine": "لا يحتاج إلى علاج."
    },
    'Potato___Early_blight': {
        "description": "داء الاحتراق المبكر للبطاطس ناتج عن الفطر Alternaria solani، الذي يمكن أن يسبب المرض في البطاطس، والطماطم، وأعضاء آخرين من عائلة البطاطس، وبعض أنواع الخردل. يُعرف هذا المرض أيضًا باسم بقعة الهدف، ونادرًا ما يؤثر على النباتات الصغيرة التي تنمو بقوة. يظهر المرض أولاً على الأوراق القديمة.",
        "medicine": "استخدام مبيدات الفطريات مثل Chlorothalonil أو Mancozeb."
    },
    'Potato___Late_blight': {
        "description": "الاحتراق المتأخر ناتج عن العامل المسبب الفطري الشبيه بالفطريات Oomycete Phytophthora infestans. العائل الرئيسي هو البطاطس، لكن P. infestans يمكن أن يصيب أيضًا نباتات أخرى من عائلة الباذنجان، بما في ذلك الطماطم، والبتونيا، وسم الفلفل المشعر. يمكن أن تعمل هذه الأنواع المصابة كمصدر للعدوى للبطاطس.",
        "medicine": "استخدام مبيدات الفطريات مثل Metalaxyl أو Mancozeb."
    },
    'Potato___healthy': {
        "description": "بطاطا صحية خالية من الأمراض.",
        "medicine": "لا يحتاج إلى علاج."
    },
    'Raspberry___healthy': {
        "description": "توت صحي خالٍ من الأمراض.",
        "medicine": "لا يحتاج إلى علاج."
    },
    'Soybean___healthy': {
        "description": "فول الصويا صحي خالٍ من الأمراض.",
        "medicine": "لا يحتاج إلى علاج."
    },
    'Squash___Powdery_mildew': {
        "description": "العفن المسحوق على اليقطين (وعلى النباتات الأخرى) سهل التعرف عليه. أول شيء ستلاحظه على الأرجح هو بقع غير متساوية من البودرة البيضاء-الرمادية التي تكون جافة عند اللمس على سطح الأوراق. تنتشر هذه البقع بسرعة ويمكن أن تغطي معظم الأوراق والسيقان.",
        "medicine": "استخدام مبيدات الفطريات مثل Sulfur أو Potassium bicarbonate."
    },
    'Strawberry___Leaf_scorch': {
        "description": "يُسبب احتراق الأوراق بقعًا بنية إلى بنفسجية على السطح العلوي لأوراق الفراولة. عندما تكون العدوى وفيرة، غالبًا ما يأخذ نسيج الورقة بين الآفات لونًا أحمر زاهيًا إلى بنفسجي، لكن اللون يختلف باختلاف الصنف ودرجة الحرارة وعوامل أخرى.",
        "medicine": "استخدام مبيدات الفطريات مثل Myclobutanil أو Captan."
    },
    'Strawberry___healthy': {
        "description": "فراولة صحية خالية من الأمراض.",
        "medicine": "لا يحتاج إلى علاج."
    },
    'Tomato___Bacterial_spot': {
        "description": "تحتوي أوراق الطماطم على بقع دائرية صغيرة (أقل من 1/8 بوصة) بنية محاطة بهالة صفراء. أما بقع الثمار فهي بحجم 1/4 بوصة، مرتفعة قليلاً، بنية وقشرية.",
        "medicine": "استخدام مبيدات البكتيريا مثل Copper hydroxide أو Streptomycin."
    },
    'Tomato___Early_blight': {
        "description": "الاحتراق المبكر هو مرض شائع في الطماطم، يمكن أن يؤدي إلى خسائر اقتصادية كبيرة. يتسبب في هذا المرض الفطريات Alternaria solani أو Alternaria tomatophila. يفضل المرض درجات الحرارة الدافئة بين 24-29 درجة مئوية والرطوبة العالية. قد يحدث في أي وقت خلال دورة نمو محصول الطماطم.",
        "medicine": "استخدام مبيدات الفطريات مثل Chlorothalonil أو Mancozeb."
    },
    'Tomato___Late_blight': {
        "description": "مرض عفن الطماطم (المعروف أيضًا باسم الاحتراق المتأخر) هو مرض ناتج عن كائن يشبه الفطر (Oomycete) ينتشر بسرعة من خلال أوراق وثمار الطماطم في الطقس الدافئ والرطب، مما يتسبب في الانهيار والتعفن. يمكن أن يكون مرضًا خطيرًا جدًا على الطماطم المزروعة في الهواء الطلق.",
        "medicine": "استخدام مبيدات الفطريات مثل Metalaxyl أو Mancozeb."
    },
    'Tomato___Leaf_Mold': {
        "description": "Cladosporium fulvum هو فطر من فئة الأسكوميست يُعرف باسم Passalora fulva، وهو مُسبب مرض غير إلزامي يسبب المرض المعروف باسم عفن أوراق الطماطم. يهاجم P. fulva نباتات الطماطم فقط، وخاصة الأوراق، ويُعتبر مرضًا شائعًا في البيوت الزجاجية، لكنه يمكن أن يحدث أيضًا في الحقول. من المحتمل أن ينمو العامل المسبب في الظروف الرطبة والباردة. في البيوت الزجاجية، يتسبب هذا المرض في مشاكل كبيرة خلال الخريف، وفي أوائل الشتاء والربيع، بسبب الرطوبة النسبية العالية للهواء ودرجة الحرارة، مما يوفر ظروفًا ملائمة لتطوير عفن الأوراق.",
        "medicine": "استخدام مبيدات الفطريات مثل Chlorothalonil أو Copper hydroxide."
    },
    'Tomato___Septoria_leaf_spot': {
        "description": "بقعة ورقة Septoria ناتجة عن فطر Septoria lycopersici. يُعتبر من أكثر الأمراض تدميرًا لأوراق الطماطم، ويكون شديدًا بشكل خاص في المناطق التي تستمر فيها الأحوال الجوية الرطبة والمبللة لفترات طويلة.",
        "medicine": "استخدام مبيدات الفطريات مثل Chlorothalonil أو Mancozeb."
    },
    'Tomato___Spider_mites Two-spotted_spider_mite': {
        "description": "العنكبوت الأحمر ذو البقعتين هو أكثر أنواع العناكب شيوعًا التي تهاجم المحاصيل الزراعية والفواكه في نيو إنجلاند. يمكن أن تحدث العناكب الحمراء على الطماطم، والباذنجان، والبطاطس، والمحاصيل المتسلقة مثل البطيخ، والخيار، ومحاصيل أخرى. تُعتبر العناكب الحمراء ذات البقعتين واحدة من أهم الآفات التي تصيب الباذنجان.",
        "medicine": "استخدام مبيدات العناكب مثل Abamectin أو Bifenazate."
    },
    'Tomato___Target_Spot': {
        "description": "بقعة الهدف في الطماطم ناتجة عن العامل المسبب الفطري Corynespora cassiicola. يحدث المرض على الطماطم المزروعة في الحقول في المناطق الاستوائية وشبه الاستوائية من العالم. تم ملاحظة بقعة الهدف لأول مرة على الطماطم في الولايات المتحدة في إيموكالي، فلوريدا، في عام 1967. توزيع المرض في الولايات المتحدة محدود في المنطقة الجنوبية الشرقية، وخاصة في الأجزاء الجنوبية من فلوريدا. ومع ذلك، يحدث المرض أيضًا على الطماطم المزروعة في البيوت الزجاجية ونظم الإنتاج في الأنفاق العالية في مناطق أخرى من أمريكا الشمالية.",
        "medicine": "استخدام مبيدات الفطريات مثل Chlorothalonil أو Mancozeb."
    },
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        "description": "فيروس تجعد الأوراق الصفراء في الطماطم (TYLCV) يمكن أن يصيب أكثر من 30 نوعًا مختلفًا من النباتات، لكنه معروف بشكل رئيسي بتسبب في خسائر مدمرة تصل إلى 100 بالمئة في إنتاج الطماطم. الطماطم المزروعة في الحقول والبيوت الزجاجية معرضة للإصابة. يُنقل TYLCV بواسطة ذبابة البياض الفضية (Bemisia tabaci). بعد الكشفات الأخيرة، تُعتبر ذبابة البياض الفضية الآن راسخة في فيكتوريا.TYLCV هو فيروس من نوع البيغومو، مما يعني أنه له نطاق واسع من المضيفين من ذوات الفلقتين. هناك سلالتان من TYLCV، سلالة خفيفة وسلالة شديدة. كانت السلالة الخفيفة تُعتبر مسؤولة عن الكشف الأخير عن TYLCV في نباتات الطماطم والأعشاب في شمال فيكتوريا (ديفيد لوفلوك، اتصال شخصي). السلالة الشديدة تصيب الفاصوليا والطماطم.",
        "medicine": "استخدام مبيدات الحشرات مثل Imidacloprid أو Thiamethoxam."
    },
    'Tomato___Tomato_mosaic_virus': {
        "description": "فيروس فسيفساء الطماطم (ToMV) هو فيروس م pathogenic للنباتات. يوجد في جميع أنحاء العالم ويؤثر على الطماطم والعديد من النباتات الأخرى.",
        "medicine": "لا يوجد علاج فعال حاليًا."
    },
    'Tomato___healthy': {
        "description": "طماطم صحية خالية من الأمراض.",
        "medicine": "لا يحتاج إلى علاج."
    }
}

# Custom CSS for right-to-left text and overall design improvements
st.markdown("""
<style>
    body {
        direction: rtl; /* Right-to-left layout */
    }
    h1, h2, h3, h4 {
        text-align: right; /* Align headings to the right */
    }
    .stButton, .stFileUploader, .stImage {
        display: block;
        margin: 0 auto; /* Center align buttons and images */
    }
    .stMarkdown {
        padding: 10px;
        border-radius: 5px; /* Rounded corners */
    }
</style>
""", unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.title("لوحة التحكم")
app_mode = st.sidebar.selectbox("اختر الصفحة", ["الرئيسية", "عنا", " التعرف على الأمراض"])

# Main Page
if app_mode == "الرئيسية":
    st.header("نظام التعرف على أمراض النباتات")
    image_path = "home_page.jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
    مرحبًا بكم في نظام الكشف عن أمراض النباتات! 🌿🔍

    هدفنا هو مساعدتك في التعرف على أمراض النباتات بسرعة وبدقة. ببساطة قم بتحميل صورة لنبتتك، وسيقوم نظامنا بتحليلها للكشف عن أي علامات تدل على وجود مرض. معًا يمكننا حماية المحاصيل وضمان حصاد أكثر صحة!

    ### كيفية عمل النظام:
    - **تحميل الصورة:** قم بزيارة صفحة **الكشف عن الأمراض** وحمّل صورة للنبتة التي تظهر عليها الأعراض.
    - **تحليل الصورة:** ستقوم الخوارزميات المتقدمة لدينا بتحليل الصورة لتحديد الأمراض المحتملة.
    - **النتائج:** احصل على النتائج الفورية مع توصيات لاتخاذ الإجراءات المناسبة.

    **لماذا تختار نظامنا؟**
    - **دقة عالية:** يعتمد على تقنيات تعلم الآلة المتطورة للتعرف الدقيق على الأمراض.
    - **سهل الاستخدام:** مصمم بواجهة بسيطة وسهلة الاستخدام لتجربة سلسة.
    - **نتائج سريعة:** احصل على نتائج الكشف عن الأمراض في ثوانٍ لاتخاذ القرارات بسرعة.

    **هل أنت جاهز للبدء؟**
    توجه إلى صفحة **الكشف عن الأمراض** من خلال الشريط الجانبي لتحميل الصورة ورؤية كيف يمكن لنظامنا أن يساعد في تحسين صحة محاصيلك!

    **لمعرفة المزيد:**
    قم بزيارة صفحة **حول** للتعرف أكثر على مشروعنا، وفريقنا، وأهدافنا.
    """)

# About Project
elif app_mode == "عنا":
    st.header("عنا")
    st.markdown("""
    ### نظرة عامة على مجموعة البيانات
    تم إنشاء هذه المجموعة من البيانات من خلال تعزيز البيانات الأصلية باستخدام التعديلات غير المتصلة بالإنترنت. يمكن العثور على مجموعة البيانات الأصلية في مستودع GitHub. تحتوي هذه المجموعة على حوالي 87,000 صورة RGB لأوراق محاصيل صحية ومصابة، مصنفة ضمن 38 فئة مختلفة. تم تقسيم مجموعة البيانات إلى مجموعتين للتدريب والتحقق بنسبة 80/20 مع الحفاظ على هيكل الدليل الأصلي. بالإضافة إلى ذلك، تم إنشاء دليل جديد يحتوي على 33 صورة لغرض الاختبار والتنبؤ.

    ### هيكل مجموعة البيانات:
    - **مجموعة التدريب:** 70,295 صورة
    - **مجموعة التحقق:** 17,572 صورة
    - **مجموعة الاختبار:** 33 صورة
    """)

# Prediction Page
elif app_mode == " التعرف على الأمراض":
    st.header(" التعرف على الأمراض")
    test_image = st.file_uploader("اختر صورة:")
    
    if test_image is not None:
        # Display the uploaded image
        if st.button("عرض الصورة"):
            st.image(test_image, width=400, use_column_width=True)
        
        # Predict button
        if st.button("تنبؤ"):
            st.write("تنبؤاتنا")
            result_index, confidence = model_prediction(test_image)
            
            # Set a confidence threshold
            CONFIDENCE_THRESHOLD = 0.85  # Adjust this value as needed

            if confidence < CONFIDENCE_THRESHOLD:
                st.error("خطأ: الصورة المدخلة لا تحتوي على أوراق أو نباتات معروفة. يرجى تحميل صورة لنبات أو ورقة.")
            else:
            # Class names for predictions
                class_name = [
                    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 
                    'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 
                    'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 
                    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 
                    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 
                    'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
            ]

            # Get the predicted disease name
            predicted_disease = class_name[result_index]

            # Display the predicted disease and its description
            st.subheader("المرض المتوقع:")
            st.write(predicted_disease)
            st.write(f"نسبة الثقة: {confidence:.2%}")
            if predicted_disease in disease_descriptions:
                st.subheader("الوصف:")
                st.write(disease_descriptions[predicted_disease]["description"])
                st.subheader("العلاج المناسب:")
                st.write(disease_descriptions[predicted_disease]["medicine"])
            else:
                st.write("معلومات غير متوفرة لهذا المرض.")

# Footer
st.markdown("---")
st.markdown("© 2024 نظام الكشف عن أمراض النباتات | Created with ❤️ by Hafida Belayd")
