import streamlit as st

st.set_page_config(
    page_title="El primer mes de dos personas separadas por fronteras",
    page_icon="❤️",
    layout="centered"
)

# Inicializar variables
if "pregunta" not in st.session_state:
    st.session_state.pregunta = 0
    st.session_state.puntos = 0

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

preguntas = [
    {
        "texto": "Se que probablemente te acuerdas de los nombres de mi familia, entonces he decidido hacerlo un poco mas complicado jajaja. Y porque no, he pensado que esto sería una buena idea, disfruta de los calculos😉.",
        "pregunta": "Sumas todas las letras que componen el nombre de mi padre, mi madre y mi hermana. Multiplica este numero (X) por 3, sumale 6, divide entre 3 y restale el valor que has calculado inicialmente (X). Cuanto da el resultado ?",
        "opciones": ["2", "10", "4", "Yo que se, no me ralles"],
        "correcta": "2"
    },
    {
        "texto": "Oleeeeee, espero que hayas acertado a la primera😊. Aunque independientemente del numero que te haya dado la suma de las letras que componen los nombres de mi familia, la respuesta siempre era 2 jajajajajaj. Bueno toca ponerse serios, espero que te acuerdes de esto🫢.",
        "pregunta": "¿Cual es mi pelicula favorita?",
        "opciones": ["Fight Club", "Shutter Island", "Interestellar", "これを翻訳して何してるの、頑張れよ若い子（笑笑笑）"],
        "correcta": "Shutter Island"
    },
    {
        "texto": "No habras sido tan pringada como para traducir la Japonesa no? JAJAJAJAAJAJAJ. Bueno creo que tambien era algo q te había dicho bastante así que no creo que fuera complicado. Bueno ahora vamos con uno de mis topics favoritos, comida :)",
        "pregunta": "¿Cual es mi comida favorita?",
        "opciones": ["Carbonara", "Pizza con piña", "Entrecot", "Brocoli a la parrilla"],
        "correcta": "Entrecot"
    },
    {
        "texto": "Espero que ni de coña hayas marcado el Brocoli, aunq tmb te digo que ninguna de esas es mi comida favorita. Mi comida favorita esta leyendo esto ahora mismo🫢. Para esta pregunta no te lo he dejado tan facil, es algo que te dije una vez por llamada, así que a ver que tal vamos de memoria jajajaja.",
        "pregunta": "¿Cual es el nombre de mi primer perro?",       
        "opciones": ["Floc", "Baloo", "Copo", "Simba"],
        "correcta": "Floc"
    },
    {
        "texto": "Ya me diras si has acertado la pregunta anterior a la primera, la verdad esq no estaba seguro de si te acordarias. Y por ultimo, pero no menos importante, de hecho, bastante importante:",
        "pregunta": "¿Que crees que es lo que mas me gusta de ti?", 
        "opciones": ["Tus ojos", "Tu pelo", "Tu sonrisa", "Tu forma de ser. Como te preocupas por los demas, lo das todo por ayudar al resto de personas y hacer que se sientan incluidas, independentientemente de tu situación y con una sonrisa brillante en la cara."],
        "correcta": "Tu forma de ser. Como te preocupas por los demas, lo das todo por ayudar al resto de personas y hacer que se sientan incluidas, independentientemente de tu situación y con una sonrisa brillante en la cara."
    }
]

# Pantalla inicial
if st.session_state.pregunta == 0 and not st.session_state.autenticado:

    st.title("El primer mes de dos personas separadas por fronteras ❤️")

    st.markdown("""
    ## Hola peque :)

    Tengo que volver a recaer en mi friquismo para tener un detalle,
    la verdad es que no está siendo fácil ya que no soy el mejor
    programador del mundo.

    Pero me encanta invertir mi tiempo en detalles para ti,
    qué le voy a hacer jajaja.

    Espero que te guste la sorpresa 😘.

    He pensado que para el primer mes sería divertido ver qué has
    aprendido sobre mí durante este corto pero intenso período
    de tiempo jajajajaja.

    Una pequeña sorpresa te espera al final 😮.

    T'estimoooo ❤️
    """)

    if st.button("✨ Empezar ✨"):
        st.session_state.autenticado = "password"
        st.rerun()

# Pantalla contraseña

elif st.session_state.autenticado == "password":

    st.title("🔐 Acceso restringido")

    st.markdown("""
    Ups, hecha el freno madaleno, donde te penabas que ibas. Con tal de aegurarme de que eres la Lucia a la que tanto me quiero
    he tenido que crear una contraseña que solo ella podria descifrar. PISTA: deberias tenerlo claro ya que es algo que te repites
    cada dia antes de empezar a trabajar 😉.
    En caso de fracaso estrepitoso (esperemos que no sea el caso jajajajajajaj) profavor contacte con el creador de esto (yo😎), para que otra 
    pista sea proporcionada. 
    """)

    password = st.text_input(
        "Contraseña",
        type="password"
    )

    if st.button("Entrar ❤️"):

        if password.lower() == "loconseguire":

            st.success(
                "Sabia que lo conseguirias jajaja"
            )

            st.session_state.autenticado = True
            st.session_state.pregunta = 1

            st.rerun()

        else:

            st.error(
                "Ups... me da a mi que esa no es jeje"
            )

# Preguntas
elif 1 <= st.session_state.pregunta <= len(preguntas):

    indice = st.session_state.pregunta - 1
    pregunta_actual = preguntas[indice]

    st.title(f"Pregunta {st.session_state.pregunta}")

    st.progress(st.session_state.pregunta / len(preguntas))

    st.caption(
        f"Pregunta {st.session_state.pregunta} de {len(preguntas)} ❤️"
    )

    st.write(pregunta_actual["texto"])

    respuesta = st.radio(
        pregunta_actual["pregunta"],
        pregunta_actual["opciones"]
    )

    mensajes_error = [
        "On vas envàs, anda tira y piénsatelo otra vez 😒",
        "Esa era facililla eh... vuelve a intentarlo 😂",
        "Te voy a quitar el carnet de novia como sigas así 😤",
        "No no no... esa no cuela 😏",
        "La recompensa está cerca, ¡concéntrate! ❤️"
    ]

    if st.button("Siguiente ❤️"):

        if respuesta == pregunta_actual["correcta"]:

            st.session_state.puntos += 1

            st.session_state.pregunta += 1

            st.rerun()

        else:

            st.error(
                mensajes_error[indice]
            )
# Resultado final
else:

    st.balloons()

    st.title("Felicidades 🎉")

    st.success(
        "Parece que por lo menos los basicos los tienes claros jajajajajaja. Aquí tienes tu recompensa, como tu dirias es algo muy ñoño, pero espero que te guste."
    )

    st.markdown("---")

    if st.button("💌 Reflexiones de un amor separado por fronteras"):

        st.markdown("""
## Para ti ❤️
Hola luuu, sinceramente nunca he sido de escribir ni redactar cartas. De hecho es algo que podria decir que me parece incluso aburrido.
Pero si algo he aprendido durante este mes, es que me motivas a hacer cosas por las que no moveria un dedo si las tuviera que hacer para mi mismo. 
Tampoco sabria decirte si eso es bueno o malo, pero lo que si que se esque aunque estes lejos, el hecho de levantarme o irme a dormir cada dia con buenos dias o buenas noches seguido de un t'estimo, lleva sacandome una sonrisa diariamente desde hace un mes. 
El que me cuentes como ha ido tu dia, compartas tus preocupaciones o frustraciones, el recibir una foto repentina de ti sonriendo o tu cara de dormida😉, son cosas que hacen mis dias mas llevaderos. 
Quien me habría dicho después de la noche del 26 de Julio en Sitges, que me dedicaría a escribir esta carta hoy exactamente dos meses despues (26 de Septiembre). 
Me acuerdo de tus dudas y de las mias, de esa charla inacabable y de los largos silencios llenos de pensamientos que nadie se atrebia a compartir. Y aun así miranos ahora.
Creo que hemos sido dos personas muy valientes, sobretodo tu. Entendía y entiendo perfectamente los miedos que tenias antes de iniciar esta relación y creo que aun así has tenido la valentia de dar una paso a ciegas y dar lo maximo de ti. 
Porque creo que no es facil querer mas allá de las fronteras. No es fácil querer dar un abrazo y no poder. Pero también creo que: el encontrar formas de comunicarse, el tener detalles el uno con el otro (aun y la complejidad de la distancia), el ser capaz de demostrar tu amor através de una pantalla y el confiar el uno en el otro ciegamente fortalecen una relación.
Porque si, las relaciones a distancia dan asco, y no es facil echar de menos. Pero creo que también demuestran que tan fuerte es la conexión y hasta donde pueden llegar a quererse dos personas.
Hasta aquí llegan las reflexiones de un ingeniero perdido en dinamarca a las 2AM sobre el compartir un més con una persona estupenda y magnifica. 
Diría que me ha gustado bastante esto de poner mis sentimientos y pensamientos en una carta, es la primera vez que lo hago, pero creo que es algo que debería hacer mas comunmente la verdad. 
Como detalle final, acordandome de como tu cara a veces parece una estrellita de lo que brilla. He pensado que sería bonito mirar que fotos tomo la nasa el dia que inició esta historia y el dia que se formalizó.

T'estimoooo ❤️
        """)

        st.markdown("---")

        st.markdown(
            "[🌠 Ver imagen NASA 15/07/2026](https://apod.nasa.gov/apod/ap260715.html)"
        )

        st.markdown(
            "[🌠 Ver imagen NASA 29/08/2026](https://apod.nasa.gov/apod/ap260829.html)"
        )