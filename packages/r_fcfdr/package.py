# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcfdr(RPackage):
	"""Flexible cFDR

	Provides functions to implement the Flexible cFDR (Hutchinson et al. (2021) <doi:10.1371/journal.pgen.1009853>) and Binary cFDR (Hutchinson et al. (2021) <doi:10.1101/2021.10.21.465274>) methodologies to leverage auxiliary data from arbitrary distributions, for example functional genomic data, with GWAS p-values to generate re-weighted p-values. 
	"""
	
	cran = "fcfdr" 

	version("1.0.0", md5="256a5beca713eb4651d6bf4a59c48ef0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-locfdr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-polycub", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-bigsplines", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
