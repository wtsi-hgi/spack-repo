# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPortfolioanalytics(RPackage):
	"""Portfolio Analysis, Including Numerical Methods for Optimization
of Portfolios

	Portfolio optimization and analysis routines and graphics.
	"""
	
	homepage = "https://github.com/braverock/PortfolioAnalytics"
	cran = "PortfolioAnalytics" 

	version("1.1.0", md5="60446f72cd88029cc798cfb4cb7ca274")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts@0.10.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-performanceanalytics@1.5.1:", type=("build", "run"))
