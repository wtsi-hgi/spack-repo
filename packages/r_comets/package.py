# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComets(RPackage):
	"""Covariance Measure Tests for Conditional Independence

	Covariance measure tests for conditional independence testing 
    against conditional covariance and nonlinear conditional mean alternatives.
    Contains versions of the generalised covariance measure test 
    (Shah and Peters, 2020, <doi:10.1214/19-aos1857>) and projected covariance 
    measure test (Lundborg et al., 2023, <doi:10.48550/arXiv.2211.02039>). 
    Applications can be found in 
    Kook and Lundborg (2024, <doi:10.48550/arXiv.2402.14416>).
	"""
	
	cran = "comets" 

	version("0.0-1", md5="6a1f19e1b5ed2d28283590a796cfde89")

	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
