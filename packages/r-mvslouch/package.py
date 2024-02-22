# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvslouch(RPackage):
	"""Multivariate Stochastic Linear Ornstein-Uhlenbeck Models for
Phylogenetic Comparative Hypotheses

	Fits multivariate Ornstein-Uhlenbeck types of models to continues trait data from species related by a common evolutionary history. See K. Bartoszek, J, Pienaar, P. Mostad, S. Andersson, T. F. Hansen (2012) <doi:10.1016/j.jtbi.2012.08.005>. The suggested PCMBaseCpp package (which significantly speeds up the likelihood calculations) can be obtained from <https://github.com/venelin/PCMBaseCpp/>.
	"""
	
	cran = "mvSLOUCH" 

	version("2.7.6", md5="90e6571c7bff6e4de74a98e5d764d0c7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-ape@5.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ouch", type=("build", "run"))
	depends_on("r-pcmbase@1.2.10:", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
