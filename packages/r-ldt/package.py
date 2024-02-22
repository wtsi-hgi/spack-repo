# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdt(RPackage):
	"""Automated Uncertainty Analysis

	Methods and tools for model selection and multi-model inference (Burnham and Anderson (2002) <doi:10.1007/b97636>, among others). 
             'SUR' (for parameter estimation), 'logit'/'probit' (for binary classification), and 'VARMA' (for time-series forecasting) are implemented.
             Evaluations are both in-sample and out-of-sample. 
             It is designed to be efficient in terms of CPU usage and memory consumption.
	"""
	
	homepage = "https://github.com/rmojab63/LDT"
	cran = "ldt" 

	version("0.5.2", md5="aa317ac11991e3f95bbe821158a82ebf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tdata", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
