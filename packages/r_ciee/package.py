# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCiee(RPackage):
	"""Estimating and Testing Direct Effects in Directed Acyclic Graphs
using Estimating Equations

	In many studies across different disciplines, detailed measures of the variables of interest are available. If assumptions can be made regarding the direction of effects between the assessed variables, this has to be considered in the analysis. The functions in this package implement the novel approach CIEE (causal inference using estimating equations; Konigorski et al., 2018, <DOI:10.1002/gepi.22107>) for estimating and testing the direct effect of an exposure variable on a primary outcome, while adjusting for indirect effects of the exposure on the primary outcome through a secondary intermediate outcome and potential factors influencing the secondary outcome. The underlying directed acyclic graph (DAG) of this considered model is described in the vignette. CIEE can be applied to studies in many different fields, and it is implemented here for the analysis of a continuous primary outcome and a time-to-event primary outcome subject to censoring. CIEE uses estimating equations to obtain estimates of the direct effect and robust sandwich standard error estimates. Then, a large-sample Wald-type test statistic is computed for testing the absence of the direct effect. Additionally, standard multiple regression, regression of residuals, and the structural equation modeling approach are implemented for comparison. 
	"""
	
	cran = "CIEE" 

	version("0.1.1", md5="2f7933a536ac25649193d3af4d6a9274")

	depends_on("r-survival", type=("build", "run"))
