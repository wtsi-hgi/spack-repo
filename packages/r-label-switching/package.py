# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabelSwitching(RPackage):
	"""Relabelling MCMC Outputs of Mixture Models

	The Bayesian estimation of mixture models (and more general hidden Markov models) suffers from the label switching phenomenon, making the MCMC output non-identifiable. This package can be used in order to deal with this problem using various relabelling algorithms.
	"""
	
	cran = "label.switching" 

	version("1.8", md5="9e6ec536d4e51c0c8d01179f5aaabf4f")

	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
