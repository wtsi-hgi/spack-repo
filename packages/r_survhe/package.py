# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvhe(RPackage):
	"""Survival Analysis in Health Economic Evaluation

	Contains a suite of functions for survival analysis in health economics.
    These can be used to run survival models under a frequentist (based on maximum likelihood)
    or a Bayesian approach (both based on Integrated Nested Laplace Approximation or Hamiltonian
    Monte Carlo). To run the Bayesian models, the user needs to install additional modules 
    (packages), i.e. 'survHEinla' and 'survHEhmc'. These can be installed using 
    'remotes::install_github' from their GitHub repositories: 
    (<https://github.com/giabaio/survHEhmc> and <https://github.com/giabaio/survHEinla/> 
    respectively). 'survHEinla' is based on the package INLA, which is available for download at
    <https://inla.r-inla-download.org/R/stable/>. The user can specify a set of parametric models 
    using a common notation and select the preferred mode of inference. The results can also be 
    post-processed to produce probabilistic sensitivity analysis and can be used to export the 
    output to an Excel file (e.g. for a Markov model, as often done by modellers and 
    practitioners). <doi:10.18637/jss.v095.i14>.
	"""
	
	homepage = "https://github.com/giabaio/survHE"
	cran = "survHE" 

	version("2.0.1", md5="1352a01ea66ee978d210b7566b03165b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
