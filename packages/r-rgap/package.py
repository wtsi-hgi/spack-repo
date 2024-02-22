# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgap(RPackage):
	"""Production Function Output Gap Estimation

	The output gap indicates the percentage difference between the actual output of an economy and its potential. Since potential output is a latent process, the estimation of the output gap poses a challenge and numerous filtering techniques have been proposed. 'RGAP' facilitates the estimation of a Cobb-Douglas production function type output gap, as suggested by the European Commission (Havik et al. 2014) <https://ideas.repec.org/p/euf/ecopap/0535.html>. To that end, the non-accelerating wage rate of unemployment (NAWRU) and the trend of total factor productivity (TFP) can be estimated in two bivariate unobserved component models by means of Kalman filtering and smoothing. 'RGAP' features a flexible modeling framework for the appropriate state-space models and offers frequentist as well as Bayesian estimation techniques. Additional functionalities include direct access to the 'AMECO' <https://economy-finance.ec.europa.eu/economic-research-and-databases/economic-databases/ameco-database_en> database and automated model selection procedures. See the paper by Streicher (2022) <http://hdl.handle.net/20.500.11850/552089> for details. 
	"""
	
	cran = "RGAP" 

	version("0.1.1", md5="69848394819599a237512ea158be1391")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-kfas", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-dlm", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
