# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantregranger(RPackage):
	"""Quantile Regression Forests for 'ranger'

	This is the implementation of quantile regression forests for the fast random forest package 'ranger'.
	"""
	
	homepage = "https://github.com/PhilippPro/quantregRanger"
	cran = "quantregRanger" 

	version("1.0", md5="0260c9359daa383a667c5bc6976742c6")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
