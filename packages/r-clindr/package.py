# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClindr(RPackage):
	"""Simulation and Analysis Tools for Clinical Dose Response
Modeling

	Bayesian and ML Emax model fitting, graphics and simulation for clinical dose
    response.  The summary data from the dose response meta-analyses in  
    Thomas, Sweeney, and Somayaji (2014) <doi:10.1080/19466315.2014.924876> and
    Thomas and Roy (2016) <doi:10.1080/19466315.2016.1256229> 
    Wu, Banerjee, Jin, Menon, Martin, and Heatherington(2017) <doi:10.1177/0962280216684528> 
    are included 
    in the package.  The prior distributions for the Bayesian analyses default to
    the posterior predictive distributions derived from these references.
	"""
	
	cran = "clinDR" 

	version("2.4.1", md5="f7f4e8d59676a4a4c7ed0a29a486f13e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rstan@2.17.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dosefinding", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
