# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpei(RPackage):
	"""Calculation of the Standardized Precipitation-Evapotranspiration
Index

	A set of functions for computing potential evapotranspiration and several widely used drought indices including the Standardized Precipitation-Evapotranspiration Index (SPEI).
	"""
	
	homepage = "https://spei.csic.es"
	cran = "SPEI" 

	version("1.8.1", md5="efd14f3c3d112ada1c27868f1dc6eadd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lmomco", type=("build", "run"))
	depends_on("r-lmom", type=("build", "run"))
	depends_on("r-tlmoments", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
