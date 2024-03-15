# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimmodel(RPackage):
	"""Perform Nonlinear Regression Using 'optim' as the Optimization
Engine

	A wrapper for 'optim' for nonlinear regression problems; see Nocedal J and Write S (2006, ISBN: 978-0387-30303-1).  Performs ordinary least squares (OLS), iterative re-weighted least squares (IRWLS), and maximum likelihood (MLE). Also includes the robust outlier detection (ROUT) algorithm; see Motulsky, H and Brown, R (2006)<doi:10.1186/1471-2105-7-123>.
	"""
	
	cran = "OptimModel" 

	version("2.0-1", md5="cf9e2c16b6194f3e0777e30c1106561f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
