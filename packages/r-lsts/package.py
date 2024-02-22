# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsts(RPackage):
	"""Locally Stationary Time Series

	A set of functions that allow stationary analysis and locally stationary time series analysis.
	"""
	
	homepage = "https://pacha.dev/LSTS/"
	cran = "LSTS" 

	version("2.1", md5="a6a6caa581501a5c456f3453a6584282")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
