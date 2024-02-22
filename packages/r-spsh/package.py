# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpsh(RPackage):
	"""Estimation and Prediction of Parameters of Various Soil
Hydraulic Property Models

	Estimates model parameters of soil hydraulic property functions by inverting measured data. A wide range of hydraulic models, weighting schemes,
    global optimization algorithms, Markov chain Monte Carlo samplers, and extended statistical analyses of results are provided.
	Prediction of soil hydraulic property model parameters and common soil properties using pedotransfer functions is facilitated. 
	Parameter estimation is based on identically and independentally distributed (weighted) model residuals, and simple model selection criteria (Hoege, M., Woehling, T., and Nowak, W. (2018) <doi:10.1002/2017WR021902>) can be calculated.
	The included models are the van Genuchten-Mualem in its unimodal, bimodal and trimodal form, the the Kosugi 2 parametric-Mualem model, and the Fredlund-Xing model.
	All models can be extended to account for non-capillary water storage and conductivity (Weber, T.K.D., Durner, W., Streck, T. and Diamantopoulos, E. (2019) <doi:10.1029/2018WR024584>. 
	The isothermal vapour conductivity (Saito, H., Simunek, J. and Mohanty, B.P. (2006) <doi:10.2136/vzj2006.0007>) is calculated based on 
	volumetric air space and a selection of different tortuosity models: 
	(Grable, A.R., Siemer, E.G. (1968) <doi:10.2136/sssaj1968.03615995003200020011x>, Lai, S.H., Tiedje J.M., Erickson, E. (1976) <doi:10.2136/sssaj1976.03615995004000010006x>,
	Moldrup, P., Olesen, T., Rolston, D.E., and Yamaguchi, T. (1997) <doi:10.1097/00010694-199709000-00004>, Moldrup, P., Olesen, T., Yoshikawa, S., Komatsu, T., and Rolston, D.E. (2004) <doi:10.2136/sssaj2004.7500>, 
	Moldrup, P., Olesen, T., Yoshikawa, S., Komatsu, T., and Rolston, D.E. (2005) <doi:10.1097/01.ss.0000196768.44165.1f>, Millington, R.J., Quirk, J.P. (1961) <doi:10.1039/TF9615701200>,
	Penman, H.L. (1940) <doi:10.1017/S0021859600048164>, and Xu, X, Nieber, J.L. Gupta, S.C. (1992) <doi:10.2136/sssaj1992.03615995005600060014x>). 	
	"""
	
	cran = "spsh" 

	version("1.1.0", md5="6fe1fd7825d20801e6a8b769162d1f43")

	depends_on("r-deoptim@2.2.4:", type=("build", "run"))
	depends_on("r-lhs@0.16:", type=("build", "run"))
	depends_on("r-pracma@2.1.4:", type=("build", "run"))
	depends_on("r-fme@1.3.5:", type=("build", "run"))
	depends_on("r-hypergeo@1.2.13:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
