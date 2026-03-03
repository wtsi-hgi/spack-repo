# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRngforgpd(RPackage):
	"""Random Number Generation for Generalized Poisson Distribution

	Generation of univariate and multivariate data that follow the generalized 
  Poisson distribution. The details of the univariate part are explained in 
  Demirtas (2017) <doi: 10.1080/03610918.2014.968725>, and the multivariate part is 
  an extension of the correlated Poisson data generation routine that was introduced in 
  Yahav and Shmueli (2012) <doi: 10.1002/asmb.901>. 
	"""
	
	cran = "RNGforGPD" 

	version("1.1.0", md5="c44fbcd058abe34c3b9eb7db6743480e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
