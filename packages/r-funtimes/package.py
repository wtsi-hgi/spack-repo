# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuntimes(RPackage):
	"""Functions for Time Series Analysis

	Nonparametric estimators and tests for time series analysis. The functions use bootstrap techniques and robust nonparametric difference-based estimators to test for the presence of possibly non-monotonic trends and for synchronicity of trends in multiple time series.
	"""
	
	cran = "funtimes" 

	version("9.1", md5="53588083a3112cf89ffdd54d292edf1e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-kendall", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-mlvar", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
