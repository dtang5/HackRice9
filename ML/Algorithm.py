import numpy as np
# import random as random
import io


class OtherMethods:
    def __init__(self):
        pass

    @staticmethod
    def load_vectors(f_name):
        fin = io.open(f_name, 'r', encoding='utf-8', newline='\n', errors='ignore')
        # n, d = map(int, fin.readline().split())
        data = {}
        for line in fin:
            tokens = line.rstrip().split(' ')
            data[tokens[0]] = map(float, tokens[1:])
        return data


class Algorithm:
    def __init__(self):
        pass

    vector_data = OtherMethods.load_vectors("wiki-news-300d-1M.vec")

    weights = {"good": 1, "bad": 1}

    def set_weights(self, weight_type, weight):
        self.weights[weight_type] = weight

    num_comment = 1.0

    def machine_learning(self, predicted, expected):
        change = 1 + (expected - predicted) / 5 * 100 / self.num_comment
        # the more comments the machine has looked at, the smaller influence a single comment should have on its weights
        self.num_comment += 1
        Algorithm.set_weights(self, 'good', self.weights['good'] * change)
        Algorithm.set_weights(self, 'bad', self.weights['bad'] * change)

    # @staticmethod
    def normalization(self, data):
        return [np.percentile(data, 10),
                np.percentile(data, 20),
                np.percentile(data, 30),
                np.percentile(data, 40),
                np.percentile(data, 50),
                np.percentile(data, 60),
                np.percentile(data, 70),
                np.percentile(data, 80),
                np.percentile(data, 90),
                np.percentile(data, 100)]

    def assign_plus_minus_values_tuple(self, word1):
        good_score = np.linalg.norm(np.array([a_i - b_i for a_i, b_i in zip(self.vector_data[word1],
                                                                            self.vector_data["good"])]))
        bad_score = np.linalg.norm(np.array([a_i - b_i for a_i, b_i in zip(self.vector_data[word1],
                                                                           self.vector_data["bad"])]))
        return good_score, bad_score

    list_plus = []
    list_minus = []
    for word in vector_data:
        list_plus.append(assign_plus_minus_values_tuple(word)[0])
        list_minus.append(assign_plus_minus_values_tuple(word)[1])
    normalized = normalization(list_plus), normalization(list_plus)

    def do_stuff_comment(self, comment):
        scores = []
        for index in range(len(comment) - 2):
            scores.append((Algorithm.assign_plus_minus_values_tuple(self, comment[index]),
                           Algorithm.assign_plus_minus_values_tuple(self, comment[index + 1]),
                           Algorithm.assign_plus_minus_values_tuple(self, comment[index + 2])))
        return scores

    def parse_for_list(self, some_string):
        # Returns some_string as a list of 'words'
        # words include grammar shit.
        special_char_list = ["!", '.', "?", "\'", ";", ":", ",", "(", ")", "\"", "-", "#", "%", "^", "&", "*", "`", "~",
                             "{", "}", "[", "]", "\\", "+", "@", "$"]
        word_list1 = some_string.split()
        word_list2 = []

        for word in word_list1:
            check_once = False
            for idx in range(len(word)):
                if word[idx] in special_char_list:
                    if idx == 0:
                        word_list2.append(word[idx])
                    elif idx >= len(word) - 2:
                        if check_once:
                            word_list2.append(word[1:idx])
                        else:
                            word_list2.append(word[0:idx])
                        word_list2.append(word[idx:len(word)])
                    check_once = True
            if check_once == False:
                word_list2.append(word)

        return word_list2
    
    def main(self, initial_text, expected_score):
        text_as_list = self.parse_for_list(initial_text)
        tuple_distances = self.do_stuff_comment(text_as_list)
        pos_sum = 0
        neg_sum = 0
        for triplet in tuple_distances:
            pos_sum += triplet[0][0] + triplet[1][0] + triplet[2][0]
            neg_sum += triplet[0][1] + triplet[1][1] + triplet[2][1]
        pos_score = pos_sum / (3 * len(tuple_distances)) / self.normalized[0][9] * 2.5
        neg_score = neg_sum / (3 * len(tuple_distances)) / self.normalized[1][9] * 2.5
        prediction = 2.5 + self.weights["good"] * pos_score - self.weights["bad"] * neg_score
        if expected_score == -1:
            return prediction
        self.machine_learning(prediction, expected_score)

    def train(self):
        with open("../HackRice9_Dataset/small_reviews_to_stars.txt", 'r') as f:
            for line in f:
                self.main(line[2:-7], float(line[-5:-2]))
        f.close()

    def run(self, txt_input):
        self.main(txt_input, -1)

    # train()
    # run("Stopped by this location based on a recommendation from a friend. When I seen the number of reviews and the "
    #    "rating I was very excited to try it out. So a couple things that I wish I would have known prior: 1. You wait "
    #    "in line and when it's your turn to sit you have to place your order. 2. You don't get taken to a seat you "
    #    "have to find one and they bring you your order. 3. They don't have Bloody Marys. Okay, so with that being "
    #    "said, the meal was very good and the service was also acceptable. I'm not a fan of paying before I eat but "
    #    "okay it's what you do.  What I can't understand is why no Bloody Marys?  I'm mean isn't it a part of a well "
    #    "balanced brunch? So I'm really torn on this place. It was good but I think there's better brunch locations (at"
    #    " least in my opinion) but it's worth a try, just remember #3")

    def determine_category(self, distance):
        if distance < self.normalized[0][0]:
            category_good = 1
        elif distance < self.normalized[0][1]:
            category_good = 2
        elif distance < self.normalized[0][2]:
            category_good = 3
        elif distance < self.normalized[0][3]:
            category_good = 4
        elif distance < self.normalized[0][4]:
            category_good = 5
        elif distance < self.normalized[0][5]:
            category_good = 6
        elif distance < self.normalized[0][6]:
            category_good = 7
        elif distance < self.normalized[0][7]:
            category_good = 8
        elif distance < self.normalized[0][8]:
            category_good = 9
        elif distance < self.normalized[0][9]:
            category_good = 10
        else:
            category_good = None

        if distance < self.normalized[1][0]:
            category_bad = 1
        elif distance < self.normalized[1][1]:
            category_bad = 2
        elif distance < self.normalized[1][2]:
            category_bad = 3
        elif distance < self.normalized[1][3]:
            category_bad = 4
        elif distance < self.normalized[1][4]:
            category_bad = 5
        elif distance < self.normalized[1][5]:
            category_bad = 6
        elif distance < self.normalized[1][6]:
            category_bad = 7
        elif distance < self.normalized[1][7]:
            category_bad = 8
        elif distance < self.normalized[1][8]:
            category_bad = 9
        elif distance < self.normalized[1][9]:
            category_bad = 10
        else:
            category_bad = None

        return category_good, category_bad


algo = Algorithm()
algo.train()
algo.run("Stopped by this location based on a recommendation from a friend. When I seen the number of reviews and the "
         "rating I was very excited to try it out. So a couple things that I wish I would have known prior: 1. "
         "You wait "
         "in line and when it's your turn to sit you have to place your order. 2. You don't get taken to a seat you "
         "have to find one and they bring you your order. 3. They don't have Bloody Marys. Okay, so with that being "
         "said, the meal was very good and the service was also acceptable. I'm not a fan of paying before I eat but "
         "okay it's what you do.  What I can't understand is why no Bloody Marys?  I'm mean isn't it a part of a well "
         "balanced brunch? So I'm really torn on this place. It was good but I think there's better brunch locations "
         "(at"
         " least in my opinion) but it's worth a try, just remember #3")
