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
    raw_text = raw_input()
    text = raw_text.replace(' ', '  ').split(' ')
    text = [w if w else ' ' for w in text]

    if DEBUG:
        print '=== PARAMETERS: ==='
        print 'N: %d' % N
        print 'M: %d' % M
        print 'text: %s' % text
        print '==================='
        print

    # To optimize, we can determine number of full divisions of text into M
    # and only work with O(N * len(text) / M).
    total_len = len(raw_text)

    # NOTE: everything is 0-indexed, but final answer is 1-indexed.
    pos = 0
    lines = 0
    times = 0

    if DEBUG:
        print ''.join((str(i + 1) for i in xrange(M)))

    # Cache of position of first word in sentence. Used for vertical skipping.
    vcache = {}
    while times < N:
        # Vertical skipping
        if pos in vcache:
            last_times, last_lines = vcache[pos]
            times_per_vskip = times - last_times
            lines_per_vskip = lines - last_lines
            vskip_count = (N - times - 1) // times_per_vskip
            if times + times_per_vskip < N - 1:
                # print '\nVSKIP factor found @ (%d, %d, %d)' % (times, lines, pos)
                # print 'vskip_count: %d, times_per_vskip: %d, lines_per_vskip: %d' % (
                #     vskip_count, times_per_vskip, lines_per_vskip)
                # print 'skip_times: %d, skip_lines: %d' % (vskip_count * times_per_vskip,
                #                                           vskip_count * lines_per_vskip)
                times += vskip_count * times_per_vskip
                lines += vskip_count * lines_per_vskip
                continue
        else:
            vcache[pos] = (times, lines)
        # print vcache

        # Horizontal skipping
        hskip_times = (M - pos) // (total_len + 1)
        if hskip_times > 0 and times < N - 1:
            # Manually count last time for proper space handling
            if times + hskip_times >= N - 1:
                hskip_times = N - times - 1
            # print
            # print 'pre-times: %d, hskip_times: %d, pre-pos: %d' % (times, hskip_times, pos)
            pos += (total_len + 1) * hskip_times
            times += hskip_times
            if DEBUG:
                sys.stdout.write((raw_text + ' ') * hskip_times)
            continue

        # Manual formatting
        for word in text:
            pos, lines = format_word(pos, lines, word, N, M)
        if times < N - 1:
            # Format space
            pos, lines = format_word(pos, lines, ' ', N, M)
        times += 1

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
