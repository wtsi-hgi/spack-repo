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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TargetScore_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TargetScore/TargetScore_1.40.0.tar.gz"]

	version("1.40.0", md5="92d3b6ca138c6c3081262a758ec63766")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
