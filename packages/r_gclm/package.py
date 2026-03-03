# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGclm(RPackage):
	"""Graphical Continuous Lyapunov Models

	Estimation of covariance matrices as solutions of 
             continuous time Lyapunov equations. 
             Sparse coefficient matrix and diagonal noise are estimated 
             with a proximal gradient 
             method for an l1-penalized loss minimization problem.
             Varando G, Hansen NR (2020) <arXiv:2005.10483>.
	"""
	
	homepage = "https://github.com/gherardovarando/gclm"
	cran = "gclm" 

	version("0.0.1", md5="0bad758c979aa404a90e2eef73d2acc0")

