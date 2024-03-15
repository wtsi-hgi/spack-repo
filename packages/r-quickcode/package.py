# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuickcode(RPackage):
	"""A Compilation of Some Frequently Used R Functions

	The NOT functions and a simple compilation of various functions for easy usage. Shorthand code to save memory usage.
	"""
	
	homepage = "https://quickcode.obi.obianom.com"
	cran = "quickcode" 

	version("0.7", md5="d2100bcce5afd2c49feda92df4172c50")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-polychrome", type=("build", "run"))
