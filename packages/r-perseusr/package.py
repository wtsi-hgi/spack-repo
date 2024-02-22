# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerseusr(RPackage):
	"""Perseus R Interop

	Enables the interoperability between the Perseus platform for omics data analysis (Tyanova et al. 2016) <doi:10.1038/nmeth.3901> and R. It provides the foundation for developing and running Perseus plugins implemented in R by providing all required input and output handling, including data and parameter parsing as described in Rudolph and Cox 2018 <doi:10.1101/447268>.
	"""
	
	cran = "PerseusR" 

	version("0.3.4", md5="e7e16366b417123631824b7727e88235")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
