# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesknockdown(RPackage):
	"""BayesKnockdown: Posterior Probabilities for Edges from Knockdown Data

	A simple, fast Bayesian method for computing posterior probabilities for relationships between a single predictor variable and multiple potential outcome variables, incorporating prior probabilities of relationships. In the context of knockdown experiments, the predictor variable is the knocked-down gene, while the other genes are potential targets. Can also be used for differential expression/2-class data.
	"""
	
	bioc = "BayesKnockdown" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BayesKnockdown_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BayesKnockdown/BayesKnockdown_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="88869bc99b67d947642bcf38110e2ab13e65ea9965bdbb37585e34ea1e692fab")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
