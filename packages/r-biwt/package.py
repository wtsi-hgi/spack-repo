# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiwt(RPackage):
	"""Compute the Biweight Mean Vector and Covariance & Correlation
Matrice

	Compute multivariate location, scale, and correlation
        estimates based on Tukey's biweight M-estimator.
	"""
	
	cran = "biwt" 

	version("1.0.1", md5="8b0223107af338cb1f38f2bcdf461d32")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
