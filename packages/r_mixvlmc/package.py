# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixvlmc(RPackage):
	"""Variable Length Markov Chains with Covariates

	Estimates Variable Length Markov Chains (VLMC) models and VLMC with
    covariates models from discrete sequences. Supports model selection via
    information criteria and simulation of new sequences from an estimated
    model. See Bühlmann, P. and Wyner, A. J. (1999) <doi:10.1214/aos/1018031204>
    for VLMC and Zanin Zambom, A., Kim, S. and Lopes Garcia, N. (2022)
    <doi:10.1111/jtsa.12615> for VLMC with covariates.
	"""
	
	homepage = "https://github.com/fabrice-rossi/mixvlmc"
	cran = "mixvlmc" 

	version("0.2.1", md5="5567b476ae6a99883a02f1e3da75a834")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-butcher", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
