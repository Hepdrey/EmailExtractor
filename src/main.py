import os
import constant
import prep
import verifier
import emails
from multiprocessing import Process


if __name__ == '__main__':
    
    fnames = os.listdir(constant.RAW_DIR)
    for fname in fnames:    
        people = prep.rearrange_info(fname)
        for person in people.values():
            print(person)
            email_prob_list = emails.get_emails(person)
            people[person['id']]['email_list_crawl'] = email_prob_list
            
        verifier.verify(fname,people,'server')
        p = Process(target=verifier.verify, args=(fname,people,False))
        print('start verify')
        p.start()
        print('end verify')