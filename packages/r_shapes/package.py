# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapes(RPackage):
	"""Statistical Shape Analysis

	Routines for the statistical analysis of landmark 
  shapes, including Procrustes analysis, graphical displays, principal
  components analysis, permutation and bootstrap tests, thin-plate 
  spline transformation grids and comparing covariance matrices. 
     See Dryden, I.L. and Mardia, K.V. (2016). Statistical shape analysis, 
     with Applications in R (2nd Edition), John Wiley and Sons. 
	"""
	
	homepage = "http://www.maths.nottingham.ac.uk/~ild/shapes"
	cran = "shapes" 

	version("1.2.7", md5="1dda149ffd06f0afbce1628a12f4a900")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
