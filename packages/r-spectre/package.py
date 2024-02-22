# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectre(RPackage):
	"""Predict Regional Community Composition

	Predict regional community composition at a fine spatial 
    resolution using only sparse biological and environmental data. The package 
    is based on the DynamicFOAM algorithm described 
    in Mokany et al. (2011) <doi:10.1111/j.1461-0248.2011.01675.x>.
	"""
	
	cran = "spectre" 

	version("1.0.2", md5="4f7ad82d9759b1f4229ed61805838487")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
