# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGllvm(RPackage):
	"""Generalized Linear Latent Variable Models

	Analysis of multivariate data using generalized linear latent variable models (gllvm). 
      Estimation is performed using either Laplace approximation method or variational approximation method implemented via TMB (Kristensen et al., (2016), <doi:10.18637/jss.v070.i05>). 
      For details see Niku et al. (2019a) <doi:10.1371/journal.pone.0216129> and 
      Niku et al. (2019b) <doi:10.1111/2041-210X.13303>.
	"""
	
	homepage = "https://github.com/JenniNiku/gllvm"
	cran = "gllvm" 

	version("1.4.3", md5="e07eb19b36dcc3af0525648d6492d150")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-mvabund", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-fishmod", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
