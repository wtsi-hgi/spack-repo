# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBend(RPackage):
	"""Bayesian Estimation of Nonlinear Data (BEND)

	Provides a set of models to estimate nonlinear longitudinal data using Bayesian estimation methods. These models include the: 1) Bayesian Piecewise Random Effects Model (Bayes_PREM()) which estimates a piecewise random effects (mixture) model for a given number of latent classes and a latent number of possible changepoints in each class, and can incorporate class and outcome predictive covariates (see Lamm (2022) <https://hdl.handle.net/11299/252533> and Lock et al., (2018) <doi:10.1007/s11336-017-9594-5>), 2) Bayesian Crossed Random Effects Model (Bayes_CREM()) which estimates a linear, quadratic, exponential, or piecewise crossed random effects models where individuals are changing groups over time (e.g., students and schools; see Rohloff et al., (2024) <doi:10.1111/bmsp.12334>), and 3) Bayesian Bivariate Piecewise Random Effects Model (Bayes_BPREM()) which estimates a bivariate piecewise random effects model to jointly model two related outcomes (e.g., reading and math achievement; see Peralta et al., (2022) <doi:10.1037/met0000358>). 
	"""
	
	homepage = "https://github.com/crohlo/BEND"
	cran = "BEND" 

	version("1.0", md5="5d046f69786493a1d9547e336dfa7ffa")

	depends_on("r@3.6.3:", type=("build", "run"))
	depends_on("r-coda@0.19.4:", type=("build", "run"))
	depends_on("r-label-switching@1.8:", type=("build", "run"))
	depends_on("r-rjags@4.14:", type=("build", "run"))
