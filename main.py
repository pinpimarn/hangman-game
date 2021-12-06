from outplay import Outplay
from play import Play
from vocab import Vocabulary
from vocabContainer import VocabContainer
from pygame import mixer

mixer.init()
mixer.music.load('bgmusic.wav')
mixer.music.play(loops=-1)
while True:
    o = Outplay(0)
    o.choose_start()
    filename = o.choose_level()
    times = o.times_input()
    c = VocabContainer()
    i = 0
    checklist = []
    while i < times:
        v = Vocabulary(filename, "", 0)
        v.random_word()
        v.count_correct()
        if v.vocab not in checklist:
            c.add_word(v)
            checklist.append(v.vocab)
            i += 1
        else:
            pass
    for w in c.container:
        o.rec(600, 100, "#708090", "#b0b4de", 250)
        o.board()
        word = w.vocab
        cluelist, index_list, count_clue, all_ch = w.index_clue()
        p = Play(word, all_ch)
        p.stage()
        p.show_update(cluelist)
        x = 200
        count_right = 0
        count_wrong = 0
        cor = w.correct - count_clue
        p.header()
        p.draw_heart(0)
        while True:
            status, char = p.pop_up_screen(word, x)
            if status == "None":
                pass
            elif status:
                count_right += 1
                p.update(status, word, char)
                if count_right == cor:
                    o.win()
                    break
                else:
                    pass
            else:
                count_wrong += 1
                x += 30
                p.draw_heart(count_wrong)
                p.hangman(count_wrong)
                if count_wrong == 9:
                    o.lose(word)
                    break
                else:
                    pass
    o.summarize(times)
