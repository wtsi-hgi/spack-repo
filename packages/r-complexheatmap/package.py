# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComplexheatmap(RPackage):
	"""Make Complex Heatmaps.

	Complex heatmaps are efficient to visualize associations between
	different sources of data sets and reveal potential patterns. Here the
	ComplexHeatmap package provides a highly flexible way to arrange
	multiple heatmaps and supports various annotation graphics."""

	bioc = "ComplexHeatmap"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ComplexHeatmap_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ComplexHeatmap/ComplexHeatmap_2.18.0.tar.gz"]
	version("2.6.2", commit="0383bada2c76dc3dde71cf6a625016b619aec4d3")
	version("2.18.0", sha256="8eb9912d9897c3914fadeb002bab1dff16a059db4d99b2fd754eb512d904f77f")
	version("2.16.0", commit="01eb55ca9b783c6d99bdfe88aa131cc102bae5b3")
	version("2.14.0", commit="57fcaa040b08917c97fb66b963eb240d5fd5a8c7")
	version("2.12.1", commit="2c5fe70724219008174d4e6f83189cddbd895ec6")
	version("2.12.0", commit="8a5f060b06646f9d6a5032832ea72e3f183ca5d7")
	version("2.10.0", commit="170df82a1568e879e4019e0ff6feb0047851684f")
	version("2.0.0", commit="97863d8ddfe36a52df0149b0b040dc386a03d2e4")
	version("1.20.0", commit="1501ecc92fda07efa3652e41626b21741951ce0f")
	version("1.18.1", commit="be0dd9d666a219c61335efe0dac50b2eed2a8825")
	version("1.17.1", commit="f647c97e556d9e918a17be15883a0b72a91d688f")
	version("1.14.0", commit="0acd8974fb5cedde8cd96efea6dfa39324d25b34")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-circlize@0.4.14:", type=("build", "run"))
	depends_on("r-getoptlong", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-globaloptions@0.1:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
