# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmlr(RPackage):
	"""Fitting Markov-Modulated Linear Regression Models

	A set of tools for fitting Markov-modulated linear regression, where responses Y(t) are time-additive, and model operates in the external environment, which is described as a continuous time Markov chain with finite state space.    
    Model is proposed by Alexander Andronov (2012) <arXiv:1901.09600v1> and algorithm of parameters estimation is based on eigenvalues and eigenvectors decomposition.
    Markov-switching regression models have the same idea of varying the regression parameters randomly in accordance with external environment. The difference is that for Markov-modulated linear regression model the external environment is described as a continuous-time homogeneous irreducible Markov chain with known parameters while switching models consider Markov chain as unobserved and estimation procedure involves estimation of transition matrix.
    These models have significant differences in terms of the analytical approach.
    Also, package provides a set of data simulation tools for Markov-modulated linear regression (for academical/research purposes).
    Research project No. 1.1.1.2/VIAA/1/16/075.
	"""
	
	cran = "MMLR" 

	version("0.2.0", md5="081cee49f305aa720a1429a346c99a6f")

	depends_on("r-pracma", type=("build", "run"))
