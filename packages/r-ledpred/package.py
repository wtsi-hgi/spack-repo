# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLedpred(RPackage):
	"""Learning from DNA to Predict Enhancers

	This package aims at creating a predictive model of regulatory sequences used to score unknown sequences based on the content of DNA motifs, next-generation sequencing (NGS) peaks and signals and other numerical scores of the sequences using supervised classification. The package contains a workflow based on the support vector machine (SVM) algorithm that maps features to sequences, optimize SVM parameters and feature number and creates a model that can be stored and used to score the regulatory potential of unknown sequences.
	"""
	
	bioc = "LedPred"

	version("1.42.0", commit="c59cf73387fc9597436940f28c1b4e84de56d063")
	version("1.36.0", commit="a4864fef7cee0fe1d10876bcb3c0c7f564c20b5a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-e1071@1.6:", type=("build", "run"))
	depends_on("r-akima", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-irr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
