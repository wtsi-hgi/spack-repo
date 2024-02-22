# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbw(RPackage):
	"""Stable Balancing Weights for Causal Inference and Missing Data

	Implements the Stable Balancing Weights by Zubizarreta (2015) <DOI:10.1080/01621459.2015.1023805>. These are the weights of minimum variance that approximately balance the empirical distribution of the observed covariates. For an overview, see Chattopadhyay, Hase and Zubizarreta (2020) <DOI:10.1002/(ISSN)1097-0258>. To solve the optimization problem in 'sbw', the default solver is 'quadprog', which is readily available through CRAN. The solver 'osqp' is also posted on CRAN. To enhance the performance of 'sbw', users are encouraged to install other solvers such as 'gurobi' and 'Rmosek', which require special installation. For the installation of gurobi and pogs, please follow the instructions at <https://www.gurobi.com/documentation/9.1/quickstart_mac/r_ins_the_r_package.html> and <http://foges.github.io/pogs/stp/r>.
	"""
	
	cran = "sbw" 

	version("1.1.5", md5="5f0ac8202478c34ffdfad5684b462149")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
