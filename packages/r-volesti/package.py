# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVolesti(RPackage):
	"""Volume Approximation and Sampling of Convex Polytopes

	Provides an R interface for 'volesti' C++ package. 'volesti' computes estimations of volume
             of polytopes given by (i) a set of points, (ii) linear inequalities or (iii) Minkowski sum of segments
             (a.k.a. zonotopes). There are three algorithms for volume estimation as well as algorithms
             for sampling, rounding and rotating polytopes. Moreover, 'volesti' provides algorithms for
             estimating copulas useful in computational finance. Methods implemented in 'volesti' are described
             in A. Chalkis and V. Fisikopoulos (2022) <doi:10.32614/RJ-2021-077> and references therein.
	"""
	
	cran = "volesti" 

	version("1.1.2-7", md5="34a34d6aa1a761733e84dda1c03269f3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
