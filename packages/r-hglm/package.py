# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHglm(RPackage):
	"""Hierarchical Generalized Linear Models

	Implemented here are procedures for fitting hierarchical generalized linear models (HGLM). It can be used for linear mixed models and generalized linear mixed models with random effects for a variety of links and a variety of distributions for both the outcomes and the random effects. Fixed effects can also be fitted in the dispersion part of the mean model. As statistical models, HGLMs were initially developed by Lee and Nelder (1996) <https://www.jstor.org/stable/2346105?seq=1>. We provide an implementation (Ronnegard, Alam and Shen 2010) <https://journal.r-project.org/archive/2010-2/RJournal_2010-2_Roennegaard~et~al.pdf> following Lee, Nelder and Pawitan (2006) <ISBN: 9781420011340> with algorithms extended for spatial modeling (Alam, Ronnegard and Shen 2015) <https://journal.r-project.org/archive/2015/RJ-2015-017/RJ-2015-017.pdf>. 
	"""
	
	cran = "hglm" 

	version("2.2-1", md5="6ff7a982455b1e4470388ee49405095e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-hglm-data", type=("build", "run"))
