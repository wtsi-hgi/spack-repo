# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactormodel(RPackage):
	"""Factor Model Estimation Using Proxy Variables

	Functions to estimate a factor model using discrete and continuous proxy variables. The function 'dproxyme' estimates a factor model of discrete proxy variables using an EM algorithm (Dempster, Laird, Rubin (1977) <doi:10.1111/j.2517-6161.1977.tb01600.x>; Hu (2008) <doi:10.1016/j.jeconom.2007.12.001>; Hu(2017) <doi:10.1016/j.jeconom.2017.06.002> ). The function 'cproxyme' estimates a linear factor model (Cunha, Heckman, and Schennach (2010) <doi:10.3982/ECTA6551>).
	"""
	
	cran = "factormodel" 

	version("1.0", md5="38b7ffded02f3891aa152753baae1ebb")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
