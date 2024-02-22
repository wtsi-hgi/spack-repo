# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJackstrap(RPackage):
	"""Correcting Nonparametric Frontier Measurements for Outliers

	Provides method used to check whether data have outlier in efficiency measurement 
  of big samples with data envelopment analysis (DEA). In this jackstrap method, the package 
  provides two criteria to define outliers: heaviside and k-s test. The technique was developed 
  by Sousa and Stosic (2005) "Technical Efficiency of the Brazilian Municipalities: Correcting 
  Nonparametric Frontier Measurements for Outliers." <doi:10.1007/s11123-005-4702-4>.
	"""
	
	cran = "jackstrap" 

	version("0.1.0", md5="c8cf3e629d7975933e3deb7ff2b371ad")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-benchmarking", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
