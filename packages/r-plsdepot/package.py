# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlsdepot(RPackage):
	"""Partial Least Squares (PLS) Data Analysis Methods

	Different methods for PLS analysis of
        one or two data tables such as Tucker's Inter-Battery, NIPALS,
        SIMPLS, SIMPLS-CA, PLS Regression, and PLS Canonical Analysis.
        The main reference for this software is the awesome book (in
        French) 'La Regression PLS: Theorie et Pratique' by Michel
        Tenenhaus.
	"""
	
	cran = "plsdepot" 

	version("0.2.0", md5="d6b593f58e2c43536541d76fbc763e41")

	depends_on("r@2.15.1:", type=("build", "run"))
