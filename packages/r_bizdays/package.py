# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBizdays(RPackage):
	"""Business Days Calculations and Utilities

	Business days calculations based on a list of holidays and
    nonworking weekdays. Quite useful for fixed income and derivatives pricing.
	"""
	
	homepage = "https://github.com/wilsonfreitas/R-bizdays"
	cran = "bizdays" 

	version("1.0.16", md5="2512180e77f360ef5a23f05e80dbf577")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
