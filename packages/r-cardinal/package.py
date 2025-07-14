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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Cardinal_3.4.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Cardinal/Cardinal_3.4.3.tar.gz"]

    version("3.10.0", tag="RELEASE_3_21")
	version("3.4.3", sha256="e14668ea2cd59cb757524ce0b222a1edb71d0cb5da1c8f8b39b4936a9356c07e")

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
