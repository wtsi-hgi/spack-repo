# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNirstat(RPackage):
	"""Novel Statistical Methods for Studying Near-Infrared
Spectroscopy (NIRS) Time Series Data

	Provides transfusion-related differential tests on Near-infrared spectroscopy (NIRS) time series with detection limit, which contains two testing statistics: Mean Area Under the Curve (MAUC) and slope statistic. This package applied a penalized spline method within imputation setting. Testing is conducted by a nested permutation approach within imputation. Refer to Guo et al (2018) <doi:10.1177/0962280218786302> for further details.
	"""
	
	cran = "NIRStat" 

	version("1.1", md5="d4547c6781cf4fccb2e1d835487b7a55")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
