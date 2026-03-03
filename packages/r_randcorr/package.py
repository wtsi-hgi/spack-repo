# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandcorr(RPackage):
	"""Generate a Random p x p Correlation Matrix

	Implements the algorithm by Pourahmadi and Wang (2015) <doi:10.1016/j.spl.2015.06.015> for generating a random p x p correlation matrix. Briefly, the idea is to represent the correlation matrix using Cholesky factorization and p(p-1)/2 hyperspherical coordinates (i.e., angles), sample the angles from a particular distribution and then convert to the standard correlation matrix form. The angles are sampled from a distribution with pdf proportional to sin^k(theta) (0 < theta < pi, k >= 1) using the efficient sampling algorithm described in Enes Makalic and Daniel F. Schmidt (2018) <arXiv:1809.05212>.
	"""
	
	cran = "randcorr" 

	version("1.0", md5="1a54d191746b27b1893b6e8d71b3f762")

