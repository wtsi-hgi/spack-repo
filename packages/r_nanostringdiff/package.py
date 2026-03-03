# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanostringdiff(RPackage):
	"""Differential Expression Analysis of NanoString nCounter Data

	This Package utilizes a generalized linear model(GLM) of the negative binomial family to characterize count data and allows for multi-factor design. NanoStrongDiff incorporate size factors, calculated from positive controls and housekeeping controls, and background level, obtained from negative controls, in the model framework so that all the normalization information provided by NanoString nCounter Analyzer is fully utilized.
	"""
	
	bioc = "NanoStringDiff" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NanoStringDiff_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NanoStringDiff/NanoStringDiff_1.32.0.tar.gz"]

	version("1.32.0", md5="3614c5bcf8aeea002875aa005d746092")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
