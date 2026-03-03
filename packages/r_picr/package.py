# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPicr(RPackage):
	"""Predictive Information Criteria for Model Selection

	Computation of predictive information criteria (PIC) from select model object classes 
    for model selection in predictive contexts. In contrast to the more widely used Akaike 
    Information Criterion (AIC), which are derived under the assumption that target(s) of prediction 
    (i.e. validation data) are independently and identically distributed to the fitting data, the PIC
    are derived under less restrictive assumptions and thus generalize AIC to the more practically 
    relevant case of training/validation data heterogeneity. The methodology featured in this package is based on Flores (2021) <https://iro.uiowa.edu/esploro/outputs/doctoral/A-new-class-of-information-criteria/9984097169902771?institution=01IOWA_INST> "A new class of information criteria for improved prediction in the presence of training/validation data heterogeneity".
	"""
	
	homepage = "https://github.com/javenrflo/picR"
	cran = "picR" 

	version("1.0.0", md5="465260ed213f0749eb8d5b7a22c1e3b3")

