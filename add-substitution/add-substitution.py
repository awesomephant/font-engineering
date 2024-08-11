from fontTools import ttLib
import fontTools.feaLib
import fontTools.feaLib.builder
from fontTools.ttLib.tables import otTables as ot
from pprint import pp
import fontTools

input_dir = "./tmp/"
input_files = ["Bitter-Black.ttf"]


with ttLib.TTFont(input_dir + input_files[0]) as f:
    # gs = ttLib.getTableClass("GSUB")
    gs = f.get("GSUB")

    # ns = gs

    
    test = gs.table.FeatureList.FeatureRecord[35]

    # Source: https://github.com/fonttools/fonttools/blob/45bd0637bdc7d9111f3dfe6e73688ce8b84a5868/Lib/fontTools/varLib/featureVars.py#L587

    # Build the Coverage Object
    inputCoverage = ot.Coverage()
    inputCoverage.populateDefaults()
    inputCoverage.glyphs.append("m")
    inputCoverage.glyphs.append("a")
    inputCoverage.glyphs.append("x")

    # Build the SubTable
    ss = ot.ChainContextSubst()
    ss.populateDefaults()
    ss.Format = 3
    ss.InputCoverage = [inputCoverage]
    ss.InputGlyphCount = 1

    # Build the Lookup
    lu = ot.Lookup()
    # lu.populateDefaults()
    lu.LookupType = 6
    lu.SubTableCount = 1
    lu.SubTable = [ss]

    # gs.table.LookupList.Lookup.append(lu)
    # gs.table.LookupList.LookupCount += 1

    # Build the FeatureRecord
    fr = ot.FeatureRecord()
    fr.FeatureTag = "max1"
    fr.Feature = ot.Feature()
    fr.Feature.populateDefaults()
    fr.Feature.LookupListIndex = gs.table.LookupList.LookupCount
    

    test = gs.table.LookupList
    # gs.table.FeatureList.FeatureRecord[36]
    # test = gs.table.ScriptList.ScriptRecord[2].Script
    # test = gs.table.FeatureList

    # gs.table.FeatureList.FeatureRecord.append(fr)
    # pp(vars(test))
    # print("\nMINE")
    # pp(vars(ss))

from fontTools.pens.ttGlyphPen import TTGlyphPen

tt = ttLib.TTFont("./tmp/Bitter-Regular.ttf")
gs = tt.getGlyphSet()
gf = tt["glyf"]
ttPen = TTGlyphPen(None)
gf["m_a_x"] = ttPen.glyph()
tt["hmtx"]["m_a_x"] = (640, 0)

fontTools.feaLib.builder.addOpenTypeFeatures(tt, "./maduro.fea")
tt.save("./output/test.ttf")

# tt.saveXML("./tmp/Bitter-Black.xml")
