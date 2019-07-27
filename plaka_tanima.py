#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import re, argparse
import configparser

from openalpr import Alpr

import locale

locale.setlocale(locale.LC_ALL, 'C')

CONF_PATH = "config.ini"

PARSER = argparse.ArgumentParser(description="### PLAKA ANALIZI ###")
PARSER.add_argument('--image', help="<Image>", type=str)
PARSER.add_argument('--folder', help="<Folder>", type=str)

ARG, _ = PARSER.parse_known_args()

ARGS = vars(ARG)

CONFIG = configparser.ConfigParser()
CONFIG.read(CONF_PATH)
REGION = CONFIG.get('openalpr', 'region')
OPENALPR_CONF = CONFIG.get('openalpr', 'conf')
RUNTIME_DIR = CONFIG.get('openalpr', 'runtime')


def process():
    alpr = Alpr(REGION, OPENALPR_CONF, RUNTIME_DIR)

    if not alpr.is_loaded():
        sys.exit(1)
    f = open("result.html", "w")
    f.write(
        "<table style='width:100%' cellpadding='30'><tr><th>Dosya Adi</th><th>Plaka</th><th>Plaka Adaylari</th><th>Plaka Adaylari Confidence</th>")
    alpr.set_top_n(7)
    plateRegEx = "(0[1-9]|[1-7][0-9]|8[01])(([A-PR-VYZ])(\d{4,5})|([A-PR-VYZ]{2})(\d{3,4})|([A-PR-VYZ]{3})(\d{2,3}))"

    if ARGS['image'] is not None:
        results = alpr.recognize_file(ARGS['image'])
        for plate in results['results']:
            print("%-12s%-12s%-10s" % ("Plaka", "Dogruluk", ARGS['image'][ARGS['image'].find('/') + 1:-4]))
            for candidate in plate['candidates']:
                if re.match(plateRegEx, candidate['plate']):
                    a = 1
                    print("%-12s%-12f%s" % (candidate['plate'], candidate['confidence'], ""))
    elif ARGS['folder'] is not None:
        files = os.listdir(ARGS['folder'])
        accrcy = {}
        accrcy[-1] = 0
        accrcy[1] = 0
        accrcy[2] = 0
        accrcy[3] = 0
        accrcy[4] = 0
        accrcy[5] = 0
        accrcy[6] = 0
        accrcy[7] = 0
        counter = 0
        for file in files:
            counter = counter + 1
            results = alpr.recognize_file(ARGS['folder'] + file)
            for plate in results['results']:
                candidates = []
                nonregex_cands = []
                nonregex_conf = []
                cand_conf = []
                file_path = ARGS['folder'] + file
                f.write(
                    "<tr><td align='center'>{}</td><td align='center'><img src={} border=3 height=150></img></td>".format(
                        file[:file.find('.')], file_path))
                temp = 0
                hasMatch = 0
                for candidate in plate['candidates']:
                    if re.match(plateRegEx, candidate['plate']):
                        temp = temp+1
                        if file[:-4] == candidate['plate']:
                            accrcy[temp] = accrcy[temp]+1
                            hasMatch = 1
                        candidates.append(candidate['plate'])
                        cand_conf.append(candidate['confidence'])
                    else:
                        nonregex_cands.append(candidate['plate'])
                        nonregex_conf.append(candidate['confidence'])
                if hasMatch == 0:
                    print(file+" has no match")
                    accrcy[-1] = accrcy[-1]+1
                f.write("<td align='center'><b>{}</b><br>{}</br></td>".format(
                    str(candidates).replace('\', \'', '<br/>')[2:-2],
                    str(nonregex_cands).replace('\', \'', '<br/>')[2:-2]))
                f.write("<td align='center'><b>{}</b><br>{}</br></td></tr>".format(
                    str(cand_conf).replace(', ', '<br/>')[1:-1], str(nonregex_conf).replace(', ', '<br/>')[1:-1]))

    print(list(accrcy.items()))
    alpr.unload()
    f.close()

if __name__ == "__main__":
    process()