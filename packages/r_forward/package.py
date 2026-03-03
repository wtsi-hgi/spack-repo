# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForward(RPackage):
	"""Robust Analysis using Forward Search

	Robust analysis using forward search in linear and
        generalized linear regression models, as described in Atkinson, A.C. and Riani, M. (2000), Robust Diagnostic Regression Analysis, First Edition. New York: Springer.
	"""
	
	cran = "forward" 

	version("1.0.6", md5="eada4df58aa843a70b226cdb672e41ce")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
