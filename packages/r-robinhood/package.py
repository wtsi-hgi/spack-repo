# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobinhood(RPackage):
	"""Interface for the RobinHood.com No Commission Investing Platform

	Execute API calls to the RobinHood <https://robinhood.com> investing platform. Functionality includes accessing account data and current holdings, retrieving investment statistics and quotes, placing and canceling orders, getting market trading hours, searching investments by popular tag, and interacting with watch lists.
	"""
	
	homepage = "https://github.com/JestonBlu/RobinHood"
	cran = "RobinHood" 

	version("1.7.0", md5="c62409986f1ee8d909d868d797ae92f1")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-profvis", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
