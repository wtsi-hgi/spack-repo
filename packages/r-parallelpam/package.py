# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParallelpam(RPackage):
	"""Parallel Partitioning-Around-Medoids (PAM) for Big Sets of Data

	Application of the Partitioning-Around-Medoids (PAM) clustering algorithm described in Schubert, E. and Rousseeuw, P.J.:
        "Fast and eager k-medoids clustering: O(k) runtime improvement of the PAM, CLARA, and CLARANS algorithms." Information Systems,
        vol. 101, p. 101804, (2021). <doi:10.1016/j.is.2021.101804>.
	It uses a binary format for storing and retrieval of matrices developed for the 'jmatrix' package but the functionality of 'jmatrix'
	is included here, so you do not need to install it. Also, it is used by package 'scellpam', so if you have installed it, you do not need
	to install this package.
	PAM can be applied to sets of data whose dissimilarity matrix can be very big. It has been tested with up to 100.000 points.
	It does this with the help of the code developed for other package, 'jmatrix', which allows the matrix not to be loaded in 'R' memory (which
	would force it to be of double type) but it gets from disk, which allows using float (or even smaller data types). Moreover, the
	dissimilarity matrix is calculated in parallel if the computer has several cores so it can open many threads. The initial part
	of the PAM algorithm can be done with the BUILD or LAB algorithms; the BUILD algorithm has been implemented in parallel. The optimization
	phase implements the FastPAM1 algorithm, also in parallel. Finally, calculation of silhouette is available and also implemented in parallel.
	"""
	
	cran = "parallelpam" 

	version("1.4", md5="126d76346d0571153c2681d5dc80c281")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-memuse@4.2.1:", type=("build", "run"))
