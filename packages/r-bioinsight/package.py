# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioinsight(RPackage):
	"""Filter and Plot RNA Biotypes

	Analyze and plot the abundance of different RNA biotypes present in a count matrix, this evaluation can be useful if you want to test different strategies of normalization or analyze a particular biotype in a differential gene expression analysis.
	"""
	
	cran = "BioInsight" 

	version("0.3.1", md5="aae65b7decd864978293e49be41953bc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
