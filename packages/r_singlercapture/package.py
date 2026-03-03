# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglercapture(RPackage):
	"""Single-Source Capture-Recapture Models

	Implementation of single-source capture-recapture methods for population size estimation using zero-truncated, zero-one truncated and zero-truncated one-inflated Poisson, Geometric and Negative Binomial regression as well as Zelterman's and Chao's regression. Package includes point and interval estimators for the population size with variances estimated using analytical or bootstrap method. Details can be found in: van der Heijden et all. (2003) <doi:10.1191/1471082X03st057oa>, Böhning and van der Heijden (2019) <doi:10.1214/18-AOAS1232>, Böhning et al. (2020) Capture-Recapture Methods for the Social and Medical Sciences or Böhning and Friedl (2021) <doi:10.1007/s10260-021-00556-8>.
	"""
	
	homepage = "https://github.com/ncn-foreigners/singleRcapture"
	cran = "singleRcapture" 

	version("0.2.1.1", md5="520240db06b5619c32c5747146b41215")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lamw", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
