# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdssamplesize(RPackage):
	"""RDS Sample Size Estimation and Power Calculation

	Provides functionality for carrying out sample size estimation and power calculation in Respondent-Driven Sampling. 
	"""
	
	cran = "RDSsamplesize" 

	version("0.5.0", md5="ffa0634e59482eb63de5031eedfb89bc")

	depends_on("r@3.6.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
