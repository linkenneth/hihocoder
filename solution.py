import sys

DEBUG = False


def format_word(pos, lines, word, N, M):
    # Format word
    if pos + len(word) <= M:
        # Format word on current line
        if DEBUG:
            sys.stdout.write(word)
        pos += len(word)
    else:
        # Line break; format word on next line
        if DEBUG:
            print
            sys.stdout.write(word)
        lines += 1
        pos = len(word)
    return pos, lines


def main():
    N, M = (int(x) for x in raw_input().split())
    text = raw_input().replace(' ', '  ').split(' ')
    text = [w if w else ' ' for w in text]

    if DEBUG:
        print '=== PARAMETERS: ==='
        print 'N: %d' % N
        print 'M: %d' % M
        print 'text: %s' % text
        print '==================='
        print

    # NOTE: everything is 0-indexed, but final answer is 1-indexed.
    pos = 0
    lines = 0

    if DEBUG:
        print ''.join((str(i + 1) for i in xrange(M)))

    for times in xrange(N):
        for word in text:
            pos, lines = format_word(pos, lines, word, N, M)
        if times < N - 1:
            # Format space
            pos, lines = format_word(pos, lines, ' ', N, M)

    if DEBUG:
        print
        print

    # Adjust from 0-index to 1-index. Note that pos does not need to be adjusted
    # because we actually care about pos - 1. Also, pos is not modded until
    # line break so pos == M is possible.
    lines += 1

    print lines, pos

if __name__ == '__main__':
    main()
