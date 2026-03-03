# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootf2(RPackage):
	"""Simulation and Comparison of Dissolution Profiles

	Compare dissolution profiles with confidence interval of similarity
  factor f2 using bootstrap methodology as described in the literature, such as 
  Efron and Tibshirani (1993, ISBN:9780412042317), Davison and Hinkley (1997,
  ISBN:9780521573917), and Shah et al. (1998) <doi:10.1023/A:1011976615750>. 
  The package can also be used to simulate dissolution profiles based on 
  mathematical modelling and multivariate normal distribution.
	"""
	
	homepage = "https://github.com/zhengguoxu/bootf2"
	cran = "bootf2" 

	version("0.4.1", md5="f03498fda64dd9256d106d83e07f7973", url="https://cran.r-project.org/src/contrib/bootf2_0.4.1.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
