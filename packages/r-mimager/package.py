# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMimager(RPackage):
	"""mimager: The Microarray Imager

	Easily visualize and inspect microarrays for spatial artifacts.
	"""
	
	homepage = "https://github.com/aaronwolen/mimager"
	bioc = "mimager"

	version("1.32.0", commit="14a123d3268b40b12afb22c3df7111d7e22ab1f1")
	version("1.26.0", commit="13cf7b33dad315eda0040919ae31bd70d3ac6e50")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-affyplm", type=("build", "run"))
	depends_on("r-oligo", type=("build", "run"))
	depends_on("r-oligoclasses", type=("build", "run"))
