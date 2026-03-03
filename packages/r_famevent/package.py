# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamevent(RPackage):
	"""Family Age-at-Onset Data Simulation and Penetrance Estimation

	Simulates age-at-onset traits associated with a segregating major gene in family data 
     obtained from population-based, clinic-based, or multi-stage designs. Appropriate ascertainment 
     correction is utilized to estimate age-dependent penetrance functions either parametrically from 
     the fitted model or nonparametrically from the data. The Expectation and Maximization algorithm 
     can infer missing genotypes and carrier probabilities estimated from family's genotype and
     phenotype information or from a fitted model. Plot functions include pedigrees of simulated 
     families and predicted penetrance curves based on specified parameter values.
     For more information see Choi, Y.-H., Briollais, L., He, W. and Kopciuk, K. (2021) FamEvent: An 
     R Package for Generating and Modeling Time-to-Event Data in Family Designs, 
     Journal of Statistical Software 97 (7), 1-30.
	"""
	
	cran = "FamEvent" 

	version("3.0", md5="1008690fd3292d3e4264f82d4df3363c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-eha", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))
