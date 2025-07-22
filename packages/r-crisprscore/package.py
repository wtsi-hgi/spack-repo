# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprscore(RPackage):
	"""On-Target and Off-Target Scoring Algorithms for CRISPR gRNAs

	Provides R wrappers of several on-target and off-target scoring methods for CRISPR guide RNAs (gRNAs). The following nucleases are supported: SpCas9, AsCas12a, enAsCas12a, and RfxCas13d (CasRx). The available on-target cutting efficiency scoring methods are RuleSet1, Azimuth, DeepHF, DeepCpf1, enPAM+GB, and CRISPRscan. Both the CFD and MIT scoring methods are available for off-target specificity prediction. The package also provides a Lindel-derived score to predict the probability of a gRNA to produce indels inducing a frameshift for the Cas9 nuclease. Note that DeepHF, DeepCpf1 and enPAM+GB are not available on Windows machines.
	"""
	
	homepage = "https://github.com/crisprVerse/crisprScore/issues"
	bioc = "crisprScore"

	version("1.12.0", commit="d0373b51dabe8c7f0bb51a79354baedebae90043")
	version("1.6.0", commit="d5de5425a7b27e39a12d3e155ab303cfbba74beb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-crisprscoredata@1.1.3:", type=("build", "run"))
	depends_on("r-basilisk@1.9.2:", type=("build", "run"))
	depends_on("r-basilisk-utils@1.9.1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
