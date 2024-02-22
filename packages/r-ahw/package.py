# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhw(RPackage):
	"""Calculates Continuous Time Likelihood Ratio Weights Assuming
Multiplicative Intensity Models and Additive Hazard Models

	Estimates continuous time weights for performing causal survival
             analysis. For instance, weighted Nelson-Aalen or Kaplan-Meier
             estimates can be given a causal interpretation. See Ryalen, Stensrud, 
             and Røysland (2019) <doi:10.1007/s10985-019-09468-y> and Ryalen (2019)
             <https://www.duo.uio.no/handle/10852/70353>
             for theory and examples.
	"""
	
	cran = "ahw" 

	version("0.1.0", md5="00749f8484a5bcaae785b1335f92d306")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-timereg", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
