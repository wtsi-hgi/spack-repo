# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnfa(RPackage):
	"""Smooth Non-Parametric Frontier Analysis

	Fitting of non-parametric production frontiers for use in efficiency analysis.
    Methods are provided for both a smooth analogue of Data Envelopment Analysis (DEA) and a 
    non-parametric analogue of Stochastic Frontier Analysis (SFA). Frontiers are constructed for 
    multiple inputs and a single output using constrained kernel smoothing as in 
    Racine et al. (2009), which allow for the imposition of monotonicity and concavity constraints 
    on the estimated frontier.
	"""
	
	cran = "snfa" 

	version("0.0.1", md5="d19bc5f524f4541223ac15b70bf123db")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-abind@1.4.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-prodlim@2018.4.18:", type=("build", "run"))
	depends_on("r-quadprog@1.5.5:", type=("build", "run"))
	depends_on("r-rdpack@0.10.1:", type=("build", "run"))
	depends_on("r-rootsolve@1.7:", type=("build", "run"))
