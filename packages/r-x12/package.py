# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RX12(RPackage):
	"""Interface to 'X12-ARIMA'/'X13-ARIMA-SEATS' and Structure for
Batch Processing of Seasonal Adjustment

	The 'X13-ARIMA-SEATS' <https://www.census.gov/data/software/x13as.html> methodology and software is a widely used software and developed by the US Census Bureau. It can be accessed from 'R' with this package and 'X13-ARIMA-SEATS' binaries are provided by the 'R' package 'x13binary'.
	"""
	
	homepage = "https://github.com/statistikat/x12"
	cran = "x12" 

	version("1.10.3", md5="855ad2d982e4cce69afce875949c221d", url="https://cran.r-project.org/src/contrib/x12_1.10.3.tar.gz")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-x13binary", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
