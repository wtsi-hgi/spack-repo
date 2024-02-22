# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStfts(RPackage):
	"""Statistical Tests for Functional Time Series

	A collection of statistical hypothesis tests of functional time series. While it will include more tests when the related literature are enriched, this package contains the following key tests: functional stationarity test, functional trend stationarity test, functional unit root test, to name a few.
	"""
	
	cran = "STFTS" 

	version("0.1.0", md5="3fe1dbf4c95ef26615899caf5851cb42")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
