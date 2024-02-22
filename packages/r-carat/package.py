# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarat(RPackage):
	"""Covariate-Adaptive Randomization for Clinical Trials

	Provides functions and command-line user interface to generate allocation sequence by covariate-adaptive randomization for clinical trials. The package currently supports six covariate-adaptive randomization procedures. Three hypothesis testing methods that are valid and robust under covariate-adaptive randomization are also available in the package to facilitate the inference for treatment effect under the included randomization procedures. Additionally, the package provides comprehensive and efficient tools to allow one to evaluate and compare the performance of randomization procedures and tests based on various criteria. See Ma W, Ye X, Tu F, and Hu F (2023) <doi: 10.18637/jss.v107.i02> for details. 
	"""
	
	cran = "carat" 

	version("2.2.1", md5="2d9e2b0857dbdc64a7333f34a63e61aa")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
