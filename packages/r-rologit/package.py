# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRologit(RPackage):
	"""Fit Rank-Ordered Logit (RO-Logit) Model

	Implements the rank-ordered logit (RO-logit) model for stratified 
    analysis of continuous outcomes introduced by 
    Tan et al. (2017) <doi:10.1177/0962280217747309>. Model diagnostics based on 
    the heuristic residuals and estimates in linear scales are available from 
    the package, and outcomes with ties are supported. 
	"""
	
	cran = "ROlogit" 

	version("0.1.2", md5="70c8402b7912c2baee7cd06b8ffb0abf")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-survival@2.41.3:", type=("build", "run"))
	depends_on("r-evd@2.3.2:", type=("build", "run"))
