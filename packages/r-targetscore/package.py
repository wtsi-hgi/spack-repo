# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTargetscore(RPackage):
	"""TargetScore: Infer microRNA targets using microRNA-overexpression data and sequence information

	Infer the posterior distributions of microRNA targets by probabilistically modelling the likelihood microRNA-overexpression fold-changes and sequence-based scores. Variaitonal Bayesian Gaussian mixture model (VB-GMM) is applied to log fold-changes and sequence scores to obtain the posteriors of latent variable being the miRNA targets. The final targetScore is computed as the sigmoid-transformed fold-change weighted by the averaged posteriors of target components over all of the features.
	"""
	
	homepage = "http://www.cs.utoronto.ca/~yueli/software.html"
	bioc = "TargetScore"

	version("1.46.0", commit="6120512ecd47ef66154038e6b0f8aacd5c696b4b")
	version("1.40.0", commit="9b7c06b49ac7d032c900804e4973a4065aa46676")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
