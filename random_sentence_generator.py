import random
def get_random_word(words):
    return random.choice(words)

names = [
    "Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Katie", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rose", "Sam", "Sophia",
    "Thomas", "Uma", "Victor", "Wendy", "Xavier", "Yara", "Zachary", "Amelia", "Benjamin",
    "Charlotte", "Daniel", "Ella", "Finn", "Georgia", "Hannah", "Isaac", "Jasmine", "Kevin",
    "Lily", "Matthew", "Nora", "Oscar", "Penelope", "Quentin", "Rachel", "Simon", "Tara",
    "Ulysses"
]
cities = [
    "Tokyo", "Delhi", "Shanghai", "São Paulo", "Mumbai", "Mexico City", "Beijing", "Osaka",
    "Cairo", "Dhaka", "Karachi", "Buenos Aires", "Istanbul", "Kolkata", "Lagos", "Kinshasa",
    "Manila", "Rio de Janeiro", "Tianjin", "Lahore", "Guangzhou", "Shenzhen", "Bangalore",
    "Moscow", "Los Angeles", "Paris", "Jakarta", "Lima", "Seoul", "London", "Chicago", "New York",
    "Bangkok", "Nagoya", "Lima", "Bogotá", "Ho Chi Minh City", "Tehran", "Chennai", "Hyderabad",
    "Hong Kong", "Ahmedabad", "Bangkok", "Baghdad", "Santiago", "Wuhan", "Toronto", "Ho Chi Minh City",
    "Riyadh"
]
verbs = [
    "runs", "jumps", "eats", "sleeps", "studies", "dances", "sings", "plays", "works", "swims",
    "reads", "writes", "talks", "listens", "laughs", "cries", "thinks", "drives", "walks", "cooks",
    "cleans", "draws", "paints", "climbs", "rides", "flies", "builds", "teaches", "learns", "creates",
    "explores", "discovers", "solves", "exercises", "meditates", "travels", "volunteers", "plants",
    "bakes", "composes", "designs", "composes", "performs", "programs", "codes", "decorates", "investigates",
    "analyzes", "calculates"
]
nouns = [
    "dog", "cat", "house", "car", "book", "computer", "table", "chair", "apple", "banana",
    "tree", "flower", "river", "mountain", "sun", "moon", "star", "ocean", "bird", "fish",
    "child", "parent", "friend", "teacher", "student", "school", "city", "country", "food", "drink",
    "music", "movie", "game", "toy", "phone", "wallet", "key", "door", "window", "street",
    "park", "garden", "cloud", "rain", "snow", "fire", "earth", "wind", "time", "money"
]
adverbs = [
    "quickly", "slowly", "happily", "sadly", "loudly", "quietly", "angrily", "calmly", "carefully", "carelessly",
    "eagerly", "reluctantly", "politely", "rudely", "generously", "selfishly", "kindly", "cruelly", "cheerfully", "gloomily",
    "patiently", "impatiently", "bravely", "fearfully", "boldly", "timidly", "wisely", "foolishly", "correctly", "incorrectly",
    "freely", "hesitantly", "firmly", "gently", "roughly", "neatly", "messily", "properly", "improperly", "quietly", "noisily",
    "gracefully", "clumsily", "politely", "impolitely", "honestly", "dishonestly", "sincerely", "insincerely", "modestly"
]
details = [
    "near the river", "at home", "in the park", "under the tree", "on the beach", "in the city", "at school", "in the forest", "on the mountain", "in the garden",
    "at the mall", "on the street", "at the restaurant", "in the library", "at the office", "at the airport", "in the supermarket", "in the kitchen", "in the bedroom", "in the living room",
    "in the basement", "on the balcony", "on the roof", "in the car", "on the bus", "on the train", "on the plane", "on the boat", "in the tent", "in the cave",
    "at the party", "at the concert", "at the beach", "at the museum", "at the zoo", "at the stadium", "in the classroom", "in the hospital", "in the cinema", "in the theater",
    "in the bathroom", "in the shower", "in the basement", "in the attic", "in the backyard", "in the garage", "in the alley", "in the desert", "in the jungle", "in the ocean"
]
print("Hello this is your first random sentence:")
while True:
    name = get_random_word(names)
    city = get_random_word(cities)
    verb = get_random_word(verbs)
    noun = get_random_word(nouns)
    adverb = get_random_word(adverbs)
    detail = get_random_word(details)
    print(f"{name} from {city} {adverb} {verb} {noun} {detail}.")
    input("Click [Enter] to generate a new one.")