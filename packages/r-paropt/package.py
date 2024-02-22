# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParopt(RPackage):
	"""Parameter Optimizing of ODE-Systems

	Enable optimization of parameters of ordinary differential equations.
             Therefore, using 'SUNDIALS' to solve the ODE-System (see Hindmarsh, Alan C., Peter N. Brown, Keith E. Grant, Steven L. Lee, Radu Serban, Dan E. Shumaker, and Carol S. Woodward. (2005) <doi:10.1145/1089014.1089020>).
             Furthermore, for optimization the particle swarm algorithm is used (see: Akman, Devin, Olcay Akman, and Elsa Schaefer. (2018) <doi:10.1155/2018/9160793> and Sengupta, Saptarshi, Sanchita Basak, and Richard Peters. (2018) <doi:10.3390/make1010010>). 
	"""
	
	cran = "paropt" 

	version("0.3.3", md5="261fca5c345273cd92a3f0da471a598d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ast2ast", type=("build", "run"))
	depends_on("r-dfdr", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
