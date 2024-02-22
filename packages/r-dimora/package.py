# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDimora(RPackage):
	"""Diffusion Models R Analysis

	The implemented methods are: Standard Bass model, Generalized Bass model (with rectangular shock, exponential shock, and mixed shock. You can choose to add from 1 to 3 shocks), Guseo-Guidolin model and Variable Potential Market model, and UCRCD model. The Bass model consists of a simple differential equation that describes the process of how new products get adopted in a population, the Generalized Bass model is a generalization of the Bass model in which there is a "carrier" function x(t) that allows to change the speed of time sliding. In some real processes the reachable potential of the resource available in a temporal instant may appear to be not constant over time, because of this we use Variable Potential Market model, in which the Guseo-Guidolin has a particular specification for the market function. The UCRCD model (Unbalanced Competition and Regime Change Diachronic) is a diffusion model used to capture the dynamics of the competitive or collaborative transition.
	"""
	
	cran = "DIMORA" 

	version("0.3.6", md5="a9d1d1f3cc24235a17e294d8591c5760")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
