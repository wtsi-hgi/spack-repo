# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBccp(RPackage):
	"""Bias Correction under Censoring Plan

	Developed for the following tasks. Simulating, computing maximum likelihood 
             estimator, computing the Fisher information matrix, computing goodness-of-fit measures,
             and correcting bias of the ML estimator for a wide range of distributions fitted to units
             placed on progressive type-I interval censoring and progressive type-II censoring plans.  
             The methods of Cox and Snell (1968) <doi:10.1111/j.2517-6161.1968.tb00724.x> and
             bootstrap method for computing the bias-corrected maximum likelihood estimator.
	"""
	
	cran = "bccp" 

	version("0.5.0", md5="3efba6efb428a52d169aa40bbe57c6c4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
