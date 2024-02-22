# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModmarg(RPackage):
	"""Calculating Marginal Effects and Levels with Errors

	Calculate predicted levels and marginal effects,
    using the delta method to calculate standard errors. This is an R-based
    version of the 'margins' command from Stata.
	"""
	
	homepage = "https://github.com/anniejw6/modmarg"
	cran = "modmarg" 

	version("0.9.6", md5="3b6aff93998005ccae67c380b29196d7")

	depends_on("r@3.5:", type=("build", "run"))
