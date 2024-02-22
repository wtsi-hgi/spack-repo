# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGvarx(RPackage):
	"""Perform Global Vector Autoregression Estimation and Inference

	Light procedures for learning Global Vector Autoregression model (GVAR) of Pesaran, Schuermann and Weiner (2004) <DOI:10.1198/073500104000000019> and Dees, di Mauro, Pesaran and Smith (2007) <DOI:10.1002/jae.932>.
	"""
	
	cran = "GVARX" 

	version("1.4", md5="945e3bbc29d2d99ac965c6b43dc574a9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-tsdyn", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
