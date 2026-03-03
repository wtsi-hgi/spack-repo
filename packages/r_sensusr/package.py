# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensusr(RPackage):
	"""Sensus Analytics

	Provides access and analytic functions for Sensus data.
	"""
	
	homepage = "https://predictive-technology-laboratory.github.io/sensus/"
	cran = "SensusR" 

	version("2.3.1", md5="e6c12ffbf399fde97e461a4c4fd6374c")

	depends_on("r-jsonlite@0.9.16:", type=("build", "run"))
	depends_on("r-lubridate@1.3.3:", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-ggmap@2.6.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-r-utils@2.3:", type=("build", "run"))
	depends_on("r-openssl@0.9.6:", type=("build", "run"))
