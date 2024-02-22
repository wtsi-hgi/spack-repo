# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSprtt(RPackage):
	"""Sequential Probability Ratio Tests Toolbox

	It is a toolbox for Sequential Probability Ratio Tests (SPRT),  Wald (1945) <doi:10.2134/agronj1947.00021962003900070011x>.
    SPRTs are applied to the data during the sampling process, ideally after each observation.
    At any stage, the test will return a decision to either continue sampling or terminate and accept one of the specified hypotheses.
    The seq_ttest() function performs one-sample, two-sample, and paired t-tests for testing one- and two-sided hypotheses (Schnuerch & Erdfelder (2019) <doi:10.1037/met0000234>).
    The seq_anova() function allows to perform a sequential one-way fixed effects ANOVA (Steinhilber et al. (2023) <doi:10.31234/osf.io/m64ne>).
    Learn more about the package by using vignettes "browseVignettes(package = "sprtt")" or go to the website <https://meikesteinhilber.github.io/sprtt/>.
	"""
	
	homepage = "https://meikesteinhilber.github.io/sprtt/"
	cran = "sprtt" 

	version("0.2.0", md5="5af7c84595ce9ddfbcd9548936f7e77d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mbess", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
