def parse_text_file(fpath):
    fin = open(fpath, "r", encoding="UTF-8")
    minfo = {}
    buf = []
    for ln in fin.readlines():        
        if ln.startswith("#"):
            info = ln[1:]
            toks = [x.strip() for x in info.split(":")]
            try:
                minfo[toks[0]] = int(toks[1])
            except:
                minfo[toks[0]] = toks[1]
            continue
        else:
            buf.append(ln)    
    minfo["text"] = "".join(buf).strip()
    return minfo

def generate_text_sequence(text, vocab_list):
    seq = []
    for x in text:
        try:
            idx = vocab_list.index(x)
            seq.append(idx)
        except:
            pass    
    return seq
    