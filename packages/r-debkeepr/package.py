# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDebkeepr(RPackage):
	"""Analysis of Non-Decimal Currencies and Double-Entry Bookkeeping

	Analysis of historical non-decimal currencies and value
    systems that use tripartite or tetrapartite systems such as pounds,
    shillings, and pence. It introduces new vector classes to represent
    non-decimal currencies, making them compatible with numeric classes,
    and provides functions to work with these classes in data frames in
    the context of double-entry bookkeeping.
	"""
	
	homepage = "https://github.com/jessesadler/debkeepr"
	cran = "debkeepr" 

	version("0.1.1", md5="b093bb7d29ebc55e02f1732ba6bde141")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-vctrs@0.5.2:", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
