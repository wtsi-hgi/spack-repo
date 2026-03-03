# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbbnp(RPackage):
	"""A Bias Bound Approach to Non-Parametric Inference

	A novel bias-bound approach for non-parametric inference is introduced, 
    focusing on both density and conditional expectation estimation. 
    It constructs valid confidence intervals that account for the presence of 
    a non-negligible bias and thus make it possible to perform inference with 
    optimal mean squared error minimizing bandwidths. 
    This package is based on Schennach (2020) <doi:10.1093/restud/rdz065>. 
	"""
	
	homepage = "https://doi.org/10.1093/restud/rdz065"
	cran = "rbbnp" 

	version("0.1.0", md5="b78e21711b58621fac819aa42f263ff1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
