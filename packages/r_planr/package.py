# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlanr(RPackage):
	"""Tools for Supply Chain Management, Demand and Supply Planning

	Perform flexible and quick calculations for Demand and Supply Planning, such as projected inventories and coverages, as well as replenishment plan. For any time bucket, daily, weekly or monthly, and any granularity level, product or group of products.
	"""
	
	homepage = "https://github.com/nguyennico/planr"
	cran = "planr" 

	version("0.3.0", md5="a36a447eed0acd5005ceb5a651d20534")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
