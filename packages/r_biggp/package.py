# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiggp(RPackage):
	"""Distributed Gaussian Process Calculations

	Distributes Gaussian process calculations across nodes
    in a distributed memory setting, using Rmpi. The bigGP class 
    provides high-level methods for maximum likelihood with normal data, 
    prediction, calculation of uncertainty (i.e., posterior covariance 
    calculations), and simulation of realizations. In addition, bigGP 
    provides an API for basic matrix calculations with distributed 
    covariance matrices, including Cholesky decomposition, back/forwardsolve, 
    crossproduct, and matrix multiplication.
	"""
	
	homepage = "https://doi.org/10.18637/jss.v063.i10"
	cran = "bigGP" 

	version("0.1.8", md5="32b7842f34197f03d595a1b183928e7f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rmpi@0.6.2:", type=("build", "run"))
	depends_on("openmpi", type=("build", "link", "run"))
