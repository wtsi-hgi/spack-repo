# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpmhr(RPackage):
	"""Privacy-Protecting Hazard Ratio Estimation in Distributed Data
Networks

	An implementation of the one-step privacy-protecting method for estimating the overall and site-specific hazard ratios using inverse probability weighted Cox models in distributed data network studies, as proposed by Shu, Yoshida, Fireman, and Toh (2019) <doi: 10.1177/0962280219869742>. This method only requires sharing of summary-level riskset tables instead of individual-level data. Both the conventional inverse probability weights and the stabilized weights are implemented. 
	"""
	
	cran = "ppmHR" 

	version("1.0", md5="069f4041a550d0b7254a3e2d14f50ac4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
