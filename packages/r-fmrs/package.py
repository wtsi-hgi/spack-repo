# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmrs(RPackage):
	"""Variable Selection in Finite Mixture of AFT Regression and FMR Models

	The package obtains parameter estimation, i.e., maximum likelihood estimators (MLE), via the Expectation-Maximization (EM) algorithm for the Finite Mixture of Regression (FMR) models with Normal distribution, and MLE for the Finite Mixture of Accelerated Failure Time Regression (FMAFTR) subject to right censoring with Log-Normal and Weibull distributions via the EM algorithm and the Newton-Raphson algorithm (for Weibull distribution). More importantly, the package obtains the maximum penalized likelihood (MPLE) for both FMR and FMAFTR models (collectively called FMRs). A component-wise tuning parameter selection based on a component-wise BIC is implemented in the package. Furthermore, this package provides Ridge Regression and Elastic Net.
	"""
	
	bioc = "fmrs"

	version("1.18.0", commit="bf959233a10993ebda490c360aa55bd0dd91bff9")
	version("1.12.0", commit="c84c5e8045e46c025b88c5949f0b602066be53c4")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
