# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoisnor(RPackage):
	"""Simultaneous Generation of Multivariate Data with Poisson and
Normal Marginals

	Generates multivariate data with count and continuous variables with a pre-specified correlation matrix. The count and continuous variables are assumed to have Poisson and normal marginals, respectively. The data generation mechanism is a combination of the normal to anything principle and a connection between Poisson and normal correlations in the mixture.
             The details of the method are explained in Yahav et al. (2012) <DOI:10.1002/asmb.901>.
	"""
	
	cran = "PoisNor" 

	version("1.3.3", md5="89087978446b82bee2404663ac3c265e")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
