# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RL1pack(RPackage):
	"""Routines for L1 Estimation

	L1 estimation for linear regression using Barrodale and Roberts' method
    <doi:10.1145/355616.361024> and the EM algorithm <doi:10.1023/A:1020759012226>,
    density, distribution function, quantile function and random number generation
    for univariate and multivariate Laplace distribution <doi:10.1080/03610929808832115>.
	"""
	
	homepage = "http://l1pack.mat.utfsm.cl/"
	cran = "L1pack" 

	version("0.41-24", md5="5671a62f55371b4c949f2d745c026dee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fastmatrix", type=("build", "run"))
