# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReffectivepred(RPackage):
	"""Pandemic Prediction Model in an SIRS Framework

	A suite of methods to fit and predict case count data using 
    a compartmental SIRS (Susceptible – Infectious – Recovered – Susceptible) 
    model, based on an assumed specification of the effective reproduction 
    number. The significance of this approach is that it relates epidemic 
    progression to the average number of contacts of infected individuals, 
    which decays as a function of the total susceptible fraction remaining 
    in the population. The main functions are pred.curve(), which computes 
    the epidemic curve for a set of parameters, and estimate.mle(), which 
    finds the best fitting curve to observed data. The easiest way to pass 
    arguments to the functions is via a config file, which contains input 
    settings required for prediction, and the package offers two methods, 
    navigate_to_config()  which points the user to the configuration file, 
    and re_predict() for starting the fit-predict process.
    Razvan G. Romanescu et al. (2023) <doi:10.1016/j.epidem.2023.100708>.
	"""
	
	cran = "REffectivePred" 

	version("1.0.0", md5="e4d4843d2240f05ee045df9a3a2f7ed9")

	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
