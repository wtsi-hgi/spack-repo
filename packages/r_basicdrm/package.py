# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasicdrm(RPackage):
	"""Fit Hill Dose Response Models

	Evaluate, fit, and analyze Hill dose response models (Goutelle et 
    al., 2008 <doi:10.1111/j.1472-8206.2008.00633.x>), also sometimes referred
    to as four-parameter log-logistic models.  Includes tools to invert Hill 
    models,  select models based on the Akaike information criterion
    (Akaike, 1974 <doi:10.1109/TAC.1974.1100705>) or Bayesian information 
    criterion (Schwarz, 1978 <https://www.jstor.org/stable/2958889>), and 
    construct bootstrapped confidence intervals both
    on the Hill model parameters and values derived from the Hill model
    parameters.
	"""
	
	cran = "basicdrm" 

	version("0.1.0", md5="1fbbd7dc0a0222d4d55ccc1d630aaab6")

	depends_on("r@2.10:", type=("build", "run"))
