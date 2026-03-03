# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimitation(RPackage):
	"""Simplified Simulations

	Provides tools for generating and analyzing simulation studies. Users may easily specify all terms of a simulation study, often in a single line of code. Common univariate and bivariate methods, such as t tests, proportions tests, and chi squared tests, are integrated. Multivariate studies involving linear or logistic regression may also be specified with symbolic inputs. The simulation studies generate data for n observations in each of B experiments. Analyses of each experiment are integrated, and empirical results across the experiments are also provided.
	"""
	
	cran = "simitation" 

	version("0.0.7", md5="f1045fae54793cb84113787c160d6d6c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
