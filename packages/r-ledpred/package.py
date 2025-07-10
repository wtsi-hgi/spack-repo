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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/LedPred_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/LedPred/LedPred_1.36.0.tar.gz"]

	version("1.36.0", sha256="b522d611a451da2707dbdc50ae6d83a3082416968d11874d84ccab3ec0c7dad9")

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
