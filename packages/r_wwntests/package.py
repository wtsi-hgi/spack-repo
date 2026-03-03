# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWwntests(RPackage):
	"""Hypothesis Tests for Functional Time Series

	Provides a collection of white noise hypothesis tests for functional time series and related visualizations. 
  These include tests based on the norms of autocovariance operators that are built under both strong and weak 
  white noise assumptions. Additionally, tests based on the spectral density operator and on principal component
  dimensional reduction are included, which are built under strong white noise assumptions. 
  Also, this package provides goodness-of-fit tests for functional autoregressive of order 1 models.
  These methods are described in Kokoszka et al. (2017) <doi:10.1016/j.jmva.2017.08.004>, Characiejus and Rice (2019) 
  <doi:10.1016/j.ecosta.2019.01.003>, Gabrys and Kokoszka (2007) <doi:10.1198/016214507000001111>, 
  and Kim et al. (2023) <doi: 10.1214/23-SS143>
  respectively.
	"""
	
	cran = "wwntests" 

	version("1.1.0", md5="4caeae52a9359fde147deb50643faef4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sde", type=("build", "run"))
	depends_on("r-ftsa", type=("build", "run"))
	depends_on("r-rainbow", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
