# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
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

	license("MIT")
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ComplexHeatmap_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ComplexHeatmap/ComplexHeatmap_2.18.0.tar.gz"]

	version("2.18.0", md5="f4f19a1339c99471cb23ffc4a7272881")

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
