from fontTools.misc.transform import Scale
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen
import pathops

FONT_PATH = "./input/arial.ttf"
OUTPUT_PATH = "./output/arial_transformed.ttf"

with TTFont(FONT_PATH) as f:
    glyfTable = f["glyf"]
    glyphSet = f.getGlyphSet()
   
    for glyphName in glyphSet.keys():
        t = Scale(.88, 1)
        print("Transforming " + glyphName)
    
        # Resolve components
        dc = DecomposingRecordingPen(glyphSet)
        pen = TransformPen(dc, t)
        glyphSet[glyphName].draw(pen)

        # Draw onto path pen
        path = pathops.Path()
        pathPen = path.getPen()
        dc.replay(pathPen)
        path.simplify()

        # create new TTGlyph from Path
        ttPen = TTGlyphPen(None)
        path.draw(ttPen)
        glyfTable[glyphName] = ttPen.glyph()
    
    f.save(OUTPUT_PATH)
    print("done")

