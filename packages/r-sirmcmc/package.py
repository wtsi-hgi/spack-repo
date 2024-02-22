# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSirmcmc(RPackage):
	"""Compartmental Susceptible-Infectious-Recovered (SIR) Model of
Community and Household Infection

	We build an Susceptible-Infectious-Recovered (SIR) model where the rate of infection is the sum of the household rate and the community rate. We estimate the posterior distribution of the parameters using the Metropolis algorithm. Further details may be found in: F Scott Dahlgren, Ivo M Foppa, Melissa S Stockwell, Celibell Y Vargas, Philip LaRussa, Carrie Reed (2021) "Household transmission of influenza A and B within a prospective cohort during the 2013-2014 and 2014-2015 seasons" <doi:10.1002/sim.9181>.
	"""
	
	cran = "SIRmcmc" 

	version("1.1.1", md5="ee1c30e36aed0b201ddf64540b773314")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
