# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlts(RPackage):
	"""Nonlinear Time Series Analysis

	R functions for (non)linear time series analysis with an emphasis on nonparametric autoregression and order estimation, and tests for linearity / additivity.
	"""
	
	homepage = "http://ento.psu.edu/directory/onb1"
	cran = "nlts" 

	version("1.0-2", md5="409a8ec2b992b07cad7dc90c546c8813")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-locfit@1.5.3:", type=("build", "run"))
	depends_on("r-acepack", type=("build", "run"))
