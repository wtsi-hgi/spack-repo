# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBintools(RPackage):
	"""Bayesian BIN (Bias, Information, Noise) Model of Forecasting

	A recently proposed Bayesian BIN model disentangles the underlying processes 
    that enable forecasters and forecasting methods to improve, decomposing forecasting accuracy into 
    three components: bias, partial information, and noise. By describing the differences between two 
    groups of forecasters, the model allows the user to carry out useful inference, such as calculating 
    the posterior probabilities of the treatment reducing bias, diminishing noise, or increasing information.
    It also provides insight into how much tamping down bias and noise in judgment or enhancing the efficient 
    extraction of valid information from the environment improves forecasting accuracy. This package provides 
    easy access to the BIN model. For further information refer to the paper Ville A. Satopää, Marat Salikhov,
    Philip E. Tetlock, and Barbara Mellers (2021) "Bias, Information, Noise: The BIN 
    Model of Forecasting" <doi:10.1287/mnsc.2020.3882>. 
	"""
	
	cran = "BINtools" 

	version("0.2.0", md5="7950f34c44026da88060e3708765cac9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-tibble@3.0.3:", type=("build", "run"))
	depends_on("r-stringi@1.4.6:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.1:", type=("build", "run"))
	depends_on("r-combinat@0.0.8:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
