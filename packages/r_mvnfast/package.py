# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvnfast(RPackage):
	"""Fast Multivariate Normal and Student's t Methods

	Provides computationally efficient tools related to the
    multivariate normal and Student's t distributions. The main functionalities
    are: simulating multivariate random vectors, evaluating multivariate normal or
    Student's t densities and Mahalanobis distances. These tools are very efficient
    thanks to the use of C++ code and of the OpenMP API.
	"""
	
	homepage = "https://github.com/mfasiolo/mvnfast/"
	cran = "mvnfast" 

	version("0.2.8", md5="7f86b01f428f34145a2fd143b441e9bf")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
