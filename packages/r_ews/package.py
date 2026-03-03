# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REws(RPackage):
	"""Early Warning System

	The purpose of Early Warning Systems (EWS) is to detect accurately the occurrence of a crisis, which is represented by a binary variable which takes the value of one when the event occurs, and the value of zero otherwise. EWS are a toolbox for policymakers to prevent or attenuate the impact of economic downturns. Modern EWS are based on the econometric framework of Kauppi and Saikkonen (2008) <doi:10.1162/rest.90.4.777>. Specifically, this framework includes four dichotomous models, relying on a logit approach to model the relationship between yield spreads and future recessions, controlling for recession risk factors. These models can be estimated in a univariate or a balanced panel framework as in Candelon, Dumitrescu and Hurlin (2014) <doi:10.1016/j.ijforecast.2014.03.015>. This package provides both methods for estimating these models and a dataset covering 13 OECD countries over a period of 45 years. In addition, this package also provides methods for the analysis of the propagation mechanisms of an exogenous shock, as well as robust confidence intervals for these response functions using a block-bootstrap method as in Lajaunie (2021). This package constitutes a useful toolbox (data and functions) for scholars as well as policymakers.
	"""
	
	cran = "EWS" 

	version("0.2.0", md5="105ee1ec20bcda08af77e28f0a826f1f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
