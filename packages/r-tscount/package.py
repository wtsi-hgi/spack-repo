# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTscount(RPackage):
	"""Analysis of Count Time Series

	Likelihood-based methods for model fitting and assessment, prediction and intervention analysis of count time series following generalized linear models are provided. Models with the identity and with the logarithmic link function are allowed. The conditional distribution can be Poisson or Negative Binomial.
	"""
	
	homepage = "http://tscount.r-forge.r-project.org"
	cran = "tscount" 

	version("1.4.3", md5="3f8dec9f9ceb970551aba7fc80f10c19")

	depends_on("r-ltsa", type=("build", "run"))
