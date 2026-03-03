# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotbfs(RPackage):
	"""Learning Hybrid Bayesian Networks using Mixtures of Truncated
Basis Functions

	Learning, manipulation and  evaluation of mixtures of  truncated basis  functions 
  (MoTBFs),  which include mixtures of  polynomials (MOPs) and  mixtures of truncated 
  exponentials (MTEs). MoTBFs are a flexible framework for modelling hybrid Bayesian
  networks (I. Pérez-Bernabé, A. Salmerón, H. Langseth (2015) <doi:10.1007/978-3-319-20807-7_36>; H. Langseth, T.D. Nielsen, I. Pérez-Bernabé, A. Salmerón (2014) <doi:10.1016/j.ijar.2013.09.012>; I. Pérez-Bernabé, A. Fernández, R. Rumí, A. Salmerón (2016) <doi:10.1007/s10618-015-0429-7>). The  package provides  functionality for learning  univariate, multivariate and
  conditional  densities, with the  possibility of incorporating prior  knowledge. Structural
  learning of hybrid Bayesian  networks is also provided. A set of useful tools is provided,
  including  plotting, printing  and likelihood  evaluation. This  package  makes use of  S3 
  objects, with two new classes called 'motbf' and 'jointmotbf'.
	"""
	
	cran = "MoTBFs" 

	version("1.4.1", md5="4fe03364afcced0e504834a29d50cc39")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-ggm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
