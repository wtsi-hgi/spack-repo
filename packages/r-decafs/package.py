# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecafs(RPackage):
	"""Detecting Changes in Autocorrelated and Fluctuating Signals

	Detect abrupt changes in time series with local fluctuations as a random walk process and autocorrelated noise as an AR(1) process. See Romano, G., Rigaill, G., Runge, V., Fearnhead, P. (2021) <doi:10.1080/01621459.2021.1909598>.
	"""
	
	cran = "DeCAFS" 

	version("3.3.3", md5="1a113745a2b85c2f362db3c26cc3cac3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
