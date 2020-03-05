import unittest

from referenceparser.webparser import ScriptureParser


class TestScriptureParser(unittest.TestCase):
    def test_scripture_parser(self):
        text = """<p class="verse" data-aid="128449643" id="p39"><span class="verse-number">39 </span>For behold, this is my <a class="study-note-ref" href="#note39a"><sup class="marker">a</sup>work</a> and my <a class="study-note-ref" href="#note39b"><sup class="marker">b</sup>glory</a>&#x2014;to bring to pass the <a class="study-note-ref" href="#note39c"><sup class="marker">c</sup>immortality</a> and <a class="study-note-ref" href="#note39d"><sup class="marker">d</sup>eternal</a> <a class="study-note-ref" href="#note39e"><sup class="marker">e</sup>life</a> of man.</p>"""
        parser = ScriptureParser()
        parser.feed(text)
        self.assertEqual(
            '39 For behold, this is my work and my glory—to bring to pass the immortality and eternal life of man.',
            parser.text
        )
