class Solution:
    def compress(self, chars: List[str]) -> int:
        write, read = 0, 0

        while read < len(chars):
            ch = chars[read]
            start = read

            while read < len(chars) and chars[read] == ch:
                read += 1
            count = read - start

            chars[write] = ch
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
        return write