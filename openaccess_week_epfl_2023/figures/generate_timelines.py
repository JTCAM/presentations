#!/bin/env python

from Slides import timeline_helper as th
import matplotlib.pyplot as plt
import pandas as pd
import datetime

source = pd.DataFrame([
    ['1534', 'Foundation of Cambridge University Press, the oldest university press and publishing house in the world'],
    ['1665', 'Creation of Le Journal des Sçavans in France, the first academic journal. Soon after, the Philosophical Transactions of the Royal Society appears in the UK. It still exists today[5]. The familiar functions of the scientific journal –registration, certification, dissemination, and archiving– are already present[6]'],
    ['1710',
        'Royal assent to the Statute of Anne. The British authors are granted the right to control the copying of their books. The duration of copyright is 14 years(renewable once), after which the books enter the public domain[7]. This new regime follows a period of censorship and monopoly(by the Stationer’s Company) and a period of no regulation, which called for a new licensing protecting the authors'],
    ['1852', 'Signature of a bilateral treaty between the UK and France: all articles published abroad in periodicals can be freely reprinted and translated, unless reserved rights are explicitly mentioned[8]'],
    ['1869', 'Foundation of the British scientific journal Nature[9]'],
    ['1880', 'Foundation of the Dutch publishing company Elsevier[10]'],
    ['1886', 'Signature of the Berne Convention, an international agreement governing copyright. Its article 7 states: “Articles from newspapers or periodicals published'],
], columns=['date', 'description'])


# labels with associated dates
source['date'] = source['date'].apply(
    lambda x: datetime.datetime.strptime(x, '%Y'))
labels = source[['date', 'description']].apply(
    lambda x: f'{x[0]: %Y}: {x[1]}', axis=1)

th.display_timeline_horizontal(labels, source['date'])
plt.show()
