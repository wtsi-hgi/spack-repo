# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdinalrr(RPackage):
	"""Analysis of Repeatability and Reproducibility Studies with
Ordinal Measurements

	Implements Bayesian data analyses of balanced repeatability and reproducibility studies with ordinal measurements. Model fitting is based on MCMC posterior sampling with 'rjags'. Function ordinalRR() directly carries out the model fitting, and this function has the flexibility to allow the user to specify key aspects of the model, e.g., fixed versus random effects. Functions for preprocessing data and for the numerical and graphical display of a fitted model are also provided. There are also functions for displaying the model at fixed (user-specified) parameters and for simulating a hypothetical data set at a fixed (user-specified) set of parameters for a random-effects rater population. For additional technical details, refer to Culp, Ryan, Chen, and Hamada (2018) and cite this Technometrics paper when referencing any aspect of this work. The demo of this package reproduces results from the Technometrics paper.
	"""
	
	cran = "ordinalRR" 

	version("1.1", md5="61149f0b87a17430af8400563a96da5d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
