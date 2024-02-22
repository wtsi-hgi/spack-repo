# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeemod(RPackage):
	"""Markov Models for Health Economic Evaluations

	An implementation of the modelling and reporting features described 
    in reference textbook and guidelines (Briggs, Andrew, et al. Decision 
    Modelling for Health Economic Evaluation. Oxford Univ. Press, 2011;
    Siebert, U. et al. State-Transition Modeling. Medical Decision Making 
    32, 690-700 (2012).): deterministic and probabilistic sensitivity analysis, 
    heterogeneity analysis, time dependency on state-time and model-time 
    (semi-Markov and non-homogeneous Markov models), etc.
	"""
	
	homepage = "https://aphp.github.io/heemod/"
	cran = "heemod" 

	version("1.0.1", md5="ba3eb0ca49a04906de35bc04e81cb88c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-memoise@2:", type=("build", "run"))
	depends_on("r-mvnfast@0.2.5:", type=("build", "run"))
	depends_on("r-tibble@3.2:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-glue@1.6:", type=("build", "run"))
	depends_on("r-lifecycle@1:", type=("build", "run"))
	depends_on("r-vctrs@0.6:", type=("build", "run"))
