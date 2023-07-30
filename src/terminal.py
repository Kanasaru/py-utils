def clrs():
    return '\033[H\033[J'

class FORMAT:
    INFO        = '\033[96m'
    SUCCESS     = '\033[92m'
    WARNING     = '\033[93m'
    FAILED      = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'

class MsgPrefix:
    INFO        = f'[  {FORMAT.INFO}INFO{FORMAT.ENDC}  ]'
    SUCCESS     = f'[   {FORMAT.SUCCESS}OK{FORMAT.ENDC}   ]'
    FAILED      = f'[ {FORMAT.FAILED}FAILED{FORMAT.ENDC} ]'
    WARNING     = f'[  {FORMAT.WARNING}WARN{FORMAT.ENDC}  ]'
    PROCESS     = '[ {}% ]'

def get_process_msg_prefeix(value) -> None:
    x = '{: >5.2f}'.format(float(value))
    return MsgPrefix.PROCESS.format(x)


if __name__ == '__main__':
    print(get_process_msg_prefeix(2))
    print(get_process_msg_prefeix(96.2852))
    print(MsgPrefix.INFO)
    print(MsgPrefix.SUCCESS)
    print(MsgPrefix.FAILED)
    print(MsgPrefix.WARNING)

