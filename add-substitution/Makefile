all: ./BitterPro ./tmp ./output ./output/test.ttf ./output/test.ttx

./BitterPro:
	git clone https://github.com/solmatas/BitterPro.git

./tmp:
	mkdir -p tmp

./output:
	mkdir -p output

./tmp/instance-ttf:
	fontmake -i -o ttf --no-subset --output-dir tmp -- ./BitterPro/sources/Bitter.glyphs

./output/test.ttf:
	python add-substitution.py

./output/test.ttx: 
	ttx ./output/test.ttf