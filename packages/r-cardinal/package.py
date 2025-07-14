# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCardinal(RPackage):
	"""A mass spectrometry imaging toolbox for statistical analysis

	Implements statistical & computational tools for analyzing mass spectrometry imaging datasets, including methods for efficient pre-processing, spatial segmentation, and classification.
	"""
	
	homepage = "http://www.cardinalmsi.org"
	bioc = "Cardinal"

	version("3.10.0", commit="07d927350c2bdd5b852bcf2fbf3c7cdd9131ab22")
	version("3.4.3", commit="eacb164cd82306a03e763ea7da00575a32f4fffd")

	depends_on("r-protgenerics", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-s4vectors@0.27.3:", type=("build", "run"))
	depends_on("r-cardinalio", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matter", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
