# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesctdesign(RPackage):
	"""Two Arm Bayesian Clinical Trial Design with and Without
Historical Control Data

	A set of functions to help clinical trial researchers calculate power and sample size for two-arm Bayesian randomized clinical trials that do or do not incorporate historical control data.  At some point during the design process, a clinical trial researcher who is designing a basic two-arm Bayesian randomized clinical trial needs to make decisions about power and sample size within the context of hypothesized treatment effects.  Through simulation, the simple_sim() function will estimate power and other user specified clinical trial characteristics at user specified sample sizes given user defined scenarios about treatment effect,control group characteristics, and outcome.  If the clinical trial researcher has access to historical control data, then the researcher can design a two-arm Bayesian randomized clinical trial that incorporates the historical data.  In such a case, the researcher needs to work through the potential consequences of historical and randomized control differences on trial characteristics, in addition to working through issues regarding power in the context of sample size, treatment effect size, and outcome.  If a researcher designs a clinical trial that will incorporate historical control data, the researcher needs the randomized controls to be from the same population as the historical controls.  What if this is not the case when the designed trial is implemented?  During the design phase, the researcher needs to investigate the negative effects of possible historic/randomized control differences on power, type one error, and other trial characteristics.  Using this information, the researcher should design the trial to mitigate these negative effects.  Through simulation, the historic_sim() function will estimate power and other user specified clinical trial characteristics at user specified sample sizes given user defined scenarios about historical and randomized control differences as well as treatment effects and outcomes.  The results from historic_sim() and simple_sim() can be printed with print_table() and graphed with plot_table() methods.  Outcomes considered are Gaussian, Poisson, Bernoulli, Lognormal, Weibull, and Piecewise Exponential.  The methods are described in Eggleston et al. (2021) <doi:10.18637/jss.v100.i21>.  
	"""
	
	homepage = "https://github.com/begglest/BayesCTDesign"
	cran = "BayesCTDesign" 

	version("0.6.1", md5="06a2ffc6feb97c5d43d57705d43043d3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-eha@2.9:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-survival@2.41.3:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
