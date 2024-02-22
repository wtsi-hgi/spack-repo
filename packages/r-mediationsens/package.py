# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMediationsens(RPackage):
	"""Simulation-Based Sensitivity Analysis for Causal Mediation
Studies

	Simulation-based sensitivity analysis for causal mediation studies. It numerically and graphically evaluates the sensitivity of causal mediation analysis results 
 to the presence of unmeasured pretreatment confounding. The proposed method has primary advantages over existing methods. 
 First, using an unmeasured pretreatment confounder conditional associations with the treatment, mediator, and outcome as 
 sensitivity parameters, the method enables users to intuitively assess sensitivity in reference to prior knowledge about the 
 strength of a potential unmeasured pretreatment confounder. Second, the method accurately reflects the influence of unmeasured 
 pretreatment confounding on the efficiency of estimation of the causal effects. Third, the method can be implemented in 
 different causal mediation analysis approaches, including regression-based, simulation-based, and propensity score-based 
 methods. It is applicable to both randomized experiments and observational studies.
	"""
	
	cran = "mediationsens" 

	version("0.0.2", md5="f4f2c39f5b0b8870fc3daff6e17bce21")

	depends_on("r-mediation", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
