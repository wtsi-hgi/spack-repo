# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreencrabToolkit(RPackage):
	"""Run 'Stan' Models to Interpret Green Crab Monitoring Assessments

	These Bayesian models written in the 'Stan' probabilistic language can be used to interpret green crab trapping and environmental DNA monitoring data, either independently or jointly. Detailed model information is found in Keller (2022) <doi:10.1002/eap.2561>.
	"""
	
	cran = "greencrab.toolkit" 

	version("0.2", md5="ec9af3c8b6805707a78d6a65fcefb27b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26.23:", type=("build", "run"))
	depends_on("r-rstantools@2.2:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26.22:", type=("build", "run"))
