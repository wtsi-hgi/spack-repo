# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvmf(RPackage):
	"""Fast Generation of von Mises-Fisher Distributed Pseudo-Random
Vectors

	Generates pseudo-random vectors that follow an arbitrary von Mises-Fisher distribution on a sphere. This method is fast and efficient when generating a large number of pseudo-random vectors. Functions to generate random variates and compute density for the distribution of an inner product between von Mises-Fisher random vector and its mean direction are also provided. Details are in Kang and Oh (2024) <doi:10.1007/s11222-024-10419-3>.
	"""
	
	homepage = "https://github.com/seungwoo-stat/rvMF"
	cran = "rvMF" 

	version("0.1.0", md5="3f21ddacb9c3c8391674a134e8bacc28")
	version("0.0.8", md5="2e089a1b07ecbf6efb859de05ab5adc9")

	depends_on("r-bessel@0.6.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rfast@2.0.6:", type=("build", "run"))
	depends_on("r-scmodels@1.0.4:", type=("build", "run"))
