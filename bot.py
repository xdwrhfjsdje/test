from nextcord import IntegrationType, Interaction, InteractionContextType
from nextcord.ext import commands
import time
import asyncio
import nextcord
import random
from nextcord import Embed


bot = commands.Bot()

@bot.event
async def on_ready():
    print("On Ready !")


@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def nigger(interaction: Interaction):
    await interaction.response.send_message("Success", ephemeral=True)

    for i in range(5):
        try:
            await interaction.send("# Nigger @everyone  ")
        except nextcord.errors.HTTPException as e:
            if e.status == 400: 
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise

@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def solara(interaction: Interaction):
    await interaction.response.send_message("Success", ephemeral=True)

    embed = Embed(
        title="🎉 Solara is Back! 🎉",
        description="""
The legendary Solara returns, the best free Roblox Executor that unlocks endless possibilities for all Roblox users! Here's what makes it unique:
- ⚡️ **Level 8:** Execute scripts of any complexity. Solara gives you full control and power in your gaming experience.
- 🎈 **Absolutely Free:** Enjoy all Solara features without any cost. Use the Executor with no restrictions or additional fees.
- 🔑 **No Annoying Key Systems:** We value your time and spare you unnecessary hassle. Just launch and play!
- 🔒 **Security First:** Over 90% of Roblox users trust Solara for its open-source code and reliability. Choose the Executor trusted by time and community.
- 🟢 **Stable Performance and Regular Updates:** 7 months of flawless operation with weekly updates. Solara is always a step ahead!
- 🔮 **Excellent Interface and Design:** Solara is not only powerful but stylish. Enjoy a sophisticated interface designed for your comfort.

**Join us and unleash the full potential of Roblox with Solara! 🚀**
Website: https://getsolara.space/
Discord: https://discord.gg/qZ8deF293t
""",
        color=0x00FF00
    )
    
    # เพิ่มรูปภาพใน Embed
    embed.set_image(url="https://media.discordapp.net/attachments/1332368853237370972/1332707977031061504/solara-is-complete-garbage-i-ran-a-unc-test-on-solara-and-v0-wr2bu8updy8d1.png?ex=67963c86&is=6794eb06&hm=68f8a6194da1923b78b9988619d68728a445bc93ded183dbc038b01798149c2c&=&format=webp&quality=lossless&width=550&height=295")  # หรือใช้ไฟล์ถ้าต้องการ

    for i in range(5):
        try:
            await interaction.send(embed=embed)
        except nextcord.errors.HTTPException as e:
            if e.status == 400:
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise    

@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def ขยะ(interaction: Interaction):
    await interaction.response.send_message("Success", ephemeral=True)

    embed = Embed(
        title="แฉตัวรั่วบิดตังเค้าไม่จ่ายเบ้าหน้าก็เหี้ยกล้องหมอก",
        description="""
ขอทานออนไลน์30บาทบิดเป็นเด็กแว้นทำทรง 
ก็อปมาแปลงเป็นของตัวเอง แรกๆบอกฟรีหลังๆบอกขายท้ายๆบอกบิด 
""",
        color=0x00FF00
    )
    
    # เพิ่มรูปภาพใน Embed
    embed.set_image(url="https://cdn.discordapp.com/attachments/1327988259284062220/1333486100693389322/image.png?ex=67991135&is=6797bfb5&hm=321e497bb44a0284db3a4e150b47d634ecf1c11bdac5dcae97d0846aef39b2ca&")  # หรือใช้ไฟล์ถ้าต้องการ

    for i in range(5):
        try:
            await interaction.send(embed=embed)
        except nextcord.errors.HTTPException as e:
            if e.status == 400:
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise     


@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def juice(interaction: Interaction):
    await interaction.response.send_message("Success", ephemeral=True)

    embed = Embed(
        title="🧃🌍all girls are the same🧃🌍",
        description="""
Mmm, they're rottin' my brain, love
These hoes are the same
I admit it, another ho got me finished
Broke my heart, oh, no, you didn't
Fuck sippin', I'ma down a whole bottle
Hard liquor, hard truth, can't swallow
Need a bartender, put me out my sorrow
Wake up the next day in the Monte Carlo
With a new woman, tell me she from Colorado
And she love women, she'll be gone by tomorrow
Who am I kiddin'?
All this jealousy and agony that I sit in
""",
        color=0x00FF00
    )
    
    # เพิ่มรูปภาพใน Embed
    embed.set_image(url="https://media.discordapp.net/attachments/1332652635211431979/1332701975325704254/81BbNIUT5L._UF10001000_QL80_.jpg?ex=679636ef&is=6794e56f&hm=c680f6c0dcac2be346d869b1859c3d4219805b0a74c164220d3c0b152b6fa912&=&format=webp&width=671&height=671")  # หรือใช้ไฟล์ถ้าต้องการ

    for i in range(5):
        try:
            await interaction.send(embed=embed)
        except nextcord.errors.HTTPException as e:
            if e.status == 400:
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise            


async def kingvon(interaction: Interaction):
    await interaction.response.send_message("Success", ephemeral=True)

    embed = Embed(
        title="Crazy Story Lyrics",
        description="""
Got a drop on this flexin' nigga, he from Tennessee (From where?)
I had a thot, she be with the shit, she told me where he be (Where he at?)
I said for sure, baby let me know if you wanna eat
She like, "Von, you already know, just put your girl on fleek" (That's it?)
I’m like, "Cool, I can do that, boo, what you want, some shoes?" (Huh?)
"Jimmy Choo? With a handbag, too? Red or baby blue?"
She get to smilin', she ain't used to this 'cause she ain't used to shit (Nah)
I'm just laughin', coulda been a pimp the way I move my lips
I be speedin', coulda been a driver the way I push the whip (Vroom, vroom)
""",
        color=0x00FF00
    )
    
    # เพิ่มรูปภาพใน Embed
    embed.set_image(url="https://media.discordapp.net/attachments/1332652635211431979/1332701975325704254/81BbNIUT5L._UF10001000_QL80_.jpg?ex=679636ef&is=6794e56f&hm=c680f6c0dcac2be346d869b1859c3d4219805b0a74c164220d3c0b152b6fa912&=&format=webp&width=671&height=671")  # หรือใช้ไฟล์ถ้าต้องการ

    for i in range(5):
        try:
            await interaction.send(embed=embed)
        except nextcord.errors.HTTPException as e:
            if e.status == 400:
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise                        

@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def music(interaction: Interaction):
    await interaction.response.send_message("Success", ephemeral=True)

    for i in range(5):
        try:
            await interaction.send("""
แค่อยากจะถามว่า baby girl ยังรักผมอยู่รึเปล่า
ไอ้หมอนั่นที่มันอยู่กับเธอทำได้เท่าผมรึเปล่า
ก็คงจะมีแต่คุณเท่านั้นที่ทำให้โลกผมเปลี่ยน
มีหลายพันอุปสรรคที่เข้ามาผมก็พร้อมจะเสี่ยง
ผมขอแค่คุณยืนอยู่ตรงนี้และไม่คิดที่จะเปลี่ยน
ถ้าเกิดคุณไปหัวใจของผมคงเหมือนดอกไม้ที่เหี่ยวเฉา
หัวใจของผมมันกำลังเปลี่ยวเหงา
ผมว่าผมคงจะทนไม่ได้ตอนเห็นเธออยู่กับเขา
แต่ผมยังคงจำวันนั้นได้ วันที่เธอเป็นของเรา
เอาผมไปเทียบกับมันไม่ได้ ผมมันไอ้ขี้เมา (ผมเทียบกับมันไม่ได้หรอกผมขี้เมา)
แค่อยากจะถามว่า baby girl ยังรักผมอยู่รึเปล่า
(ยังรักผมอยู่รึเปล่าล่ะ baby girl แล้วเธอยังรักผมอยู่รึเปล่า)
ไอ้หมอนั่นที่มันอยู่กับเธอทำได้เท่าผมรึเปล่า (ผมว่ามันคงจะทำไม่ได้)
ผมยังจำได้วันที่เธอไปเธอไม่ได้บอกได้กล่าว (ผมยังจำได้วันที่เธอไปเธอไม่ได้บอกได้กล่าว)
ถ้าดาวดวงนั้นผมคว้ามาได้เธอจะกลับมารึเปล่า (เธอจะกลับมารึเปล่า)
มันคงไม่ง่ายที่เธอจะใช้ชีวิตกับอันธพาล
ผมใช้ชีวิตอยู่ข้างถนน เธออยู่บนภัตตาคาร
ผมคงจะไม่มีใครมาสน เพราะมัวแต่นับสตางค์
และไหนเธอบอกว่าผมนี่แหละคือสิ่งที่เธอต้องการ
ผมมีให้เธอทุกอย่าง แต่ baby girl ต้องการจะจาก
ผมมีให้เธอจริง ๆ นะ everything ทุกสิ่งทุกอย่าง (ทุกอย่างอ่ะ)
เธอบอกที่ผมเล่ามาทั้งหมดนี่มันไม่จริงซักอย่าง
เธอบอกให้ผมยอมรับความจริง และให้ผมทิ้งทุกอย่าง
ก็คงจะมีแต่คุณเท่านั้นที่ทำให้โลกผมเปลี่ยน
มีหลายพันอุปสรรคที่เข้ามาผมก็พร้อมจะเสี่ยง
ผมขอแค่คุณยืนอยู่ตรงนี้และไม่คิดที่จะเปลี่ยน
ถ้าเกิดคุณไปหัวใจของผมคงเหมือนดอกไม้ที่เหี่ยวเฉา
หัวใจของผมมันกำลังเปลี่ยวเหงา
ผมว่าผมคงจะทนไม่ได้ตอนเห็นเธออยู่กับเขา (เห็นเธออยู่กับเขาฉ
แต่ผมยังคงจำวันนั้นได้วันที่เธอเป็นของเรา
เอาผมไปเทียบกับมันไม่ได้ ผมมันไอ้ขี้เมา (ผมเทียบกับมันไม่ได้หรอก ผมขี้เมา)
แค่อยากจะถามว่า baby girl ยังรักผมอยู่รึเปล่า
(ยังรักผมอยู่รึเปล่าล่ะ baby girl แล้วเธอยังรักผมอยู่รึเปล่า)
ไอ้หมอนั่นที่มันอยู่กับเธอทำได้เท่าผมรึเปล่า (ผมว่ามันคงจะทำไม่ได้)
ผมยังจำได้วันที่เธอไปเธอไม่ได้บอกได้กล่าว (ผมยังจำได้วันที่เธอไปเธอไม่ได้บอกได้กล่าว)
ถ้าดาวดวงนั้นผมคว้ามาได้เธอจะกลับมารึเปล่า (เธอจะกลับมารึเปล่า)
            """)
        except nextcord.errors.HTTPException as e:
            if e.status == 400: 
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise


emojis = [
    "😀", "😁", "😂", "🤣", "😃", "😄", "😅", "😆", "😉", "😊", "😋", "😎", "😍", "😘", "😗", "😙", "😚", "☺️", "🙂", "🤗", 
    "🤩", "🤔", "🤨", "😐", "😑", "😶", "🙄", "😏", "😣", "😥", "😮", "🤐", "😯", "😪", "😫", "😴", "😌", "😛", "😜", 
    "😝", "🤤", "😒", "😓", "😔", "😕", "🙃", "🤑", "😲", "☹️", "🙁", "😖", "😞", "😟", "😤", "😢", "😭", "😦", "😧", 
    "😨", "😩", "🤯", "😬", "😰", "😱", "🥵", "🥶", "😳", "🤪", "😵", "😡", "😠", "🤬", "😷", "🤒", "🤕", "🤢", "🤮", 
    "🤧", "😇", "🥳", "🥺", "🤠", "🤡", "🤥", "🤫", "🤭", "🧐", "🤓", "😈", "👿", "👹", "👺", "💀", "👻", "👽", "🤖", 
    "💩", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾"
]

def random_emoji(count=150):
    random_emojis = random.choices(emojis, k=count)
    return " ".join(random_emojis)

@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def lag(interaction: Interaction):
    await interaction.response.send_message("Success", ephemeral=True)

    for i in range(5):
        try:
            await interaction.send(random_emoji())
        except nextcord.errors.HTTPException as e:
            if e.status == 400: 
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise

@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def sorry(interaction: Interaction):
    await interaction.response.send_message("Success", ephemeral=True)

    for i in range(5):
        try:
            await interaction.send("""
ขอโทษเด้ออาบาไน ตอนนี้เฮา บ่ได้ซังไผหรือเคียดให้ไผเผื่อโตเลย และกะบ่ได้โกรธแค้นผู้ได๋นำ ตอนนี้แค่รู้สึกว่า มันจั๋งแม่นรู้สึกสบายและรู้สึกมีแฮงอีหลี อาบาไนขอให้โตไปสู่สุขติเด้อ เดี๋ยวมื้ออื่นเฮาสิใส่
            """)
        except nextcord.errors.HTTPException as e:
            if e.status == 400: 
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise

@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def nuke(interaction: Interaction):
    await interaction.response.send_message("Success", ephemeral=True)

    for i in range(5):
        try:
            await interaction.send("""
# 更騎辺葬表庫属洗州返彬北材療。始到焦像検用選分坊吸高理益高優緊意物先。継族読断利割共民等曜省様。発駆処持写約同周常定急同録誰量刊無国報地。下入症重秋超写知県去局能。聞状雨式国差小容最脚住自東信帯万権一。記将響和海演気気専味微国手私脅行門安子。在無境乗存能山間海式値朝氏料視密携見表録。議競索掲落遊典織知事告他草帯比選。都読急界害降年磐元解述切。芸気数法歌択表会先反状完東本経省死人北。分見供放転方貫将付横平歩辺本必。中芸購特点禁以経済記労止強開強載欲件。毛逮際企多向心更承芸町役疑。時禁請祐兵子木家策正康併求出平悩。父民歴新善乗准打員吐真方。病春終停書前出要際長心仙害害宿。野載法達係定側企未到全田携平認見爆変。終勝棺平天経済同州必目選。校済話朝九矢新公世投金方投日真受閣醸野。名応遇内事将和閣発政塾悪隣茶火多南注。間岩室趣方欲係難全障選階写衆題対末市。私覧埼最整杯隊増導中浜独。日治村歌映案行情産数院寺東協万雑。正車再部探爪価両覧変認近議犯本員。竹思西記雄機太済十入開印定愛。渡強殺丹全高火込田基江待意。転決葉囲著能笠味父速学斉。洋時合更数性芸弁今顧傷竹。定九事愛加当独時図考分術社能顧写人。聞映図合声毎選生円素巡暮議授可権阪表不基。考掲遂待閉来面本日目関毛題建刊歩写指。綬情淑基諒言最数可火月町舞門外文八高活。測経支健木司倍公際身平育宝論。井放煮読加約民得看乗芸一河線触注。客投掲素間松詐幕女供過援楽彩。記車合問伝続運表口井常画田。作球域回報来金禁素読義提体側理苦。本百億車社転社王総戻英理少高起江分主記能。宙件座運闘国共申済作紘引期景挑政問票黙。居氏言見健常画続業献終団線将伊。難塚刊知万犯挙山訴罪宮宣遠謝審流野。図挙内探状栗裏認衛車録校索。歴動室禁材木近産掲面徹宿用境。国者政恋実革社信海店週古転立護。屈図前者気支界確残円将有誕村断掲基特長季。券館体記規棋連図画地記拶庫中区勝図。問連崎理堂待本降顔件企拶年岐豊実部好町関。重購影著先区築模係水討流層表一必幻。生厚隠期祉教習短昨離導供世。社米門協半季以部稿大減回善著局撃響書。文大写幹方置付彩広市目無営辻日要。養査統事原属夜策公力然隆接渡写。感服選者駆横文存歩認新春昨料新分持授備行。暖返暮進治崎条文芸委町向士味実述武。黒年克際政画驚建陸家検者待山。会更申語投辞傷内得野権応取振必求丘突欄。産稿再政面藤彩武質完雑端実暮企見。急取米刑数界検議題高化入町烈人。売作日応貢施加情長文後江。多部医静素容盟原再光早化。出石努録一点航則講整遊長改提主足親。年用記働見乱信個安去制将発男。目田作公題紙安座化者仲集行。創伸線身役治三位博保政戦大桶。訴祉惑子期徒注来涯望済無。上載図況著著村広頭演形元雑囲半。訴主談燃球観甲界過翼投売多検利長。建特禁頂加人真初婚科結二義。年投導購催細要述類虚続入演。江情変現芸意束局利者原球社図。院週大打誕方模戦投第申知事。航書合現室稿合断術史記局陽社誠芸早装。載戦結就銀投知載核第手離持開己知。月行文山読能場生国上就国炎動明。職嗅掲午困称浅供村掲暮県有非藤多情。籍府児専在間腕責治風技表社応。日済長次孫書芸読入物出祐培新困局界葉月。本千群広温辞物戸強子囲事状互情込察棋画。鈴能予予碁案浜右無要見騒提犬敬保相。別駒己前仕持使布意生鯖始液。辱出情芸体他告時富概直牛市告照創芸定惑分。球製渡補要馬離都目受予最。欠烈命小速訴訪報野無堀提加索。正広謙部報時全警得月変警検最能性出整。栗主沖意似本総売都少参側。待業口真刊表提裁員週東本前仕紋度化。天康止囲影校金勝人帯本川尽体間様終各説。能団代同訴国議第提麺野補投縦話返福相学。止際構覧見写高打案故小国育者話埋言刊定土。柿符告任黒需術環情国負嘆要観民不。号京政回編究全文慮降役住。就歓校矢化稿提選況米造展供取村請。女戦語小校柔場億好供昇須属。働見乱信個安去制将発男。目田作公題紙安座化者仲集行。創伸線身役治三位博保政戦大桶。訴祉惑子期徒注来涯望済無。上載図況著著村広頭演形元雑囲半。訴主談燃球観甲界過翼投売多検利長。建特禁頂加人真初婚科結二義。年投導購催細要述類虚続入演。江情変現芸意束局利者原球社図。院週大打誕方模戦投第申知事。航書合現室稿合断術史記局陽社誠芸早装。載戦結就銀投知載核第手離持開己知。月行文山読能場生国上就国炎動明。職嗅掲午困称浅供村掲暮県有非藤多情。籍府児専在間腕責治風技表社応。日済長次孫書芸読入物出祐培新困局界葉月。本千群広温辞物戸強子囲事状互情込察棋画。鈴能予予碁案浜右無要見騒提犬敬保相。別駒己前仕持使布意生鯖始液
            """)
        except nextcord.errors.HTTPException as e:
            if e.status == 400: 
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise

@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def x2swift(interaction: Interaction):
    await interaction.response.send_message("Success", ephemeral=True)

    for i in range(5):
        try:
            await interaction.send("""
เป็นเวลา 48 ชั่วโมง ที่ไม่มี Seriality และคงเป็นวันสุดท้าย เพราะx2Swiftz ได้หักหลังฉัน ฉันหยุดสั่นไม่ได้และมีอาการทางจิตอย่างรุนแรง วันนี้ฉันตื่นนอนพยายามเปิดดิส แต่ฉันหาดิส Seriality ไม่เจอฉันมีอาการตื่นตระหนกครั้งใหญ่ แต่ก็สงบลงได้หลังจากผ่านไปสองสามชั่วโมง วันนี้ฉันไปโรงเรียนไม่ได้ ฉันกังวลมากจนเอาปืนของพ่อออกจากโรงเก็บของและคิดว่าจะฆ่าตัวตาย ฉันจะเป็นอะไรถ้าไม่มี Seriality มันคือชีวิตของฉัน มันคือพรหมลิขิต แต่วันนี้ไม่มีมันแล้ว หากไม่มี Seriality ฉันคงทำอะไรไม่ได้ Seriality เป็นสิ่งที่ดีที่สุดที่เคยเจอและฉันไม่สามารถเลิกเสพติดได้ มันเป็นสคริปต์ที่ดีที่สุดในชีวิต ฉันไม่สามารถหยุดสั่นตัวและร้องไห้ได้ ฉันกังวลมาก ว่าดิสของฉันจะโดนลบ ฉันใช้เงินทั้งหมดของฉันกับ Seriality ฉันซื้อสคริปต์
            """)
        except nextcord.errors.HTTPException as e:
            if e.status == 400: 
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise

@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def custom(interaction: Interaction, custom:str):
    await interaction.response.send_message("Success", ephemeral=True)

    for i in range(5):
        try:
            await interaction.send(custom)
        except nextcord.errors.HTTPException as e:
            if e.status == 400: 
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise

@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def funvex(interaction: Interaction, ):
    await interaction.response.send_message("Success", ephemeral=True)

    for i in range(5):
        try:
            await interaction.send("https://discord.gg/funvexcommunity On Top @everyone || EZ Chill")
        except nextcord.errors.HTTPException as e:
            if e.status == 400: 
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise

@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def liminal(interaction: Interaction, ):
    await interaction.response.send_message("Success", ephemeral=True)

    for i in range(5):
        try:
            await interaction.send("https://discord.gg/vesperv On Top @everyone || EZ Chill")
        except nextcord.errors.HTTPException as e:
            if e.status == 400: 
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise

@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def test(interaction: Interaction, ):
    await interaction.response.send_message("Success", ephemeral=True)

    ans = await interaction.send("Test")
    time.sleep(3)
    await ans.delete()

@bot.slash_command(
    description="โดนเบี้ยวแล้ว",
    integration_types=[
        IntegrationType.user_install,
        IntegrationType.guild_install,
    ],
    contexts=[
        InteractionContextType.guild,
        InteractionContextType.bot_dm,
        InteractionContextType.private_channel,
    ],
)
async def shibaxniceday(interaction: Interaction):
    await interaction.response.send_message("Success", ephemeral=True)

    embed = Embed(
        title="🎉 SHIBA X NICEDAY 🎉",
        description="""
ตัวยิงดิสไม่ใช้ยศที่โหดที่สุดยิงแรงและbypassกันแสปม
- ⚡️ **ไม่มีreskin** ทุกๆอย่างเขียนเองทั้งหมดและคุณภาพดีกว่าร้านreskin git hub ที่คุณเคยซื้อแน่ๆ และโปรแกรมอีกมากมายที่จะเพิ่มในอนาคต.
- 🎈 **อัพเดตฟรี** สนุกกับการยิงดิสของคุณพร้อมอัพเดตฟรีและคุณภาพผมให้แบบไม่มีหมก
- 🧃 **มีโทเค่นขาย** ราคาเพียงตัวละ0.5ไม่มีอีเมลสามารถติดเองได้สบาย

Discord: https://discord.gg/nxqCPyEkgd
        """,
        color=0x00FF00  # You can change this color to whatever you want.
    )

    for i in range(5):
        try:
            await interaction.send(embed=embed)
        except nextcord.errors.HTTPException as e:
            if e.status == 400:
                print("Error: 400 Bad Request. Trying again after waiting...")
                await asyncio.sleep(5)
                continue
            else:
                raise   

            




bot.run("")