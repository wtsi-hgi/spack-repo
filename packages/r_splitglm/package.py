# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplitglm(RPackage):
	"""Split Generalized Linear Models

	Functions to compute split generalized linear models. The approach fits 
             generalized linear models that split the covariates into groups. The 
             optimal split of the variables into groups and the regularized estimation 
             of the coefficients are performed by minimizing an objective function 
             that encourages sparsity within each group and diversity among them.
             Example applications can be found in Christidis et al. (2021)
             <arXiv:2102.08591>.
	"""
	
	cran = "SplitGLM" 

	version("1.0.5", md5="f17fe6f1e3b5531d6208730b36056e68")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
