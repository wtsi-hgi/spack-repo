# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsynth(RPackage):
	"""Generalized Synthetic Control Method

	Provides causal inference with interactive fixed-effect models. It imputes counterfactuals for each treated unit using control group information based on a linear interactive fixed effects model that incorporates unit-specific intercepts interacted with time-varying coefficients. This method generalizes the synthetic control method to the case of multiple treated units and variable treatment periods, and improves efficiency and interpretability. This version supports unbalanced panels and implements the matrix completion method. 
	"""
	
	homepage = "https://yiqingxu.org/packages/gsynth/gsynth_examples.html"
	cran = "gsynth" 

	version("1.2.1", md5="492dc7d0a986698968dd44187c91c321")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-ggally@1.0.1:", type=("build", "run"))
	depends_on("r-future@1.21:", type=("build", "run"))
	depends_on("r-dorng@1.8.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-abind@1.4.0:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.6:", type=("build", "run"))
	depends_on("r-mass@7.3.47:", type=("build", "run"))
	depends_on("r-lfe@1.0.0:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
