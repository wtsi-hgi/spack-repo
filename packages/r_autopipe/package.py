# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutopipe(RPackage):
	"""Automated Transcriptome Classifier Pipeline: Comprehensive
Transcriptome Analysis

	An unsupervised fully-automated pipeline for transcriptome analysis or a supervised option to identify characteristic genes from predefined subclasses.
              We rely on the 'pamr' <http://www.bioconductor.org/packages//2.7/bioc/html/pamr.html> clustering algorithm to cluster the Data and then draw a heatmap of the clusters with the most significant genes and the 
              least significant genes according to the 'pamr' algorithm. This way we get easy to grasp heatmaps that show us for each cluster which are the clusters most defining genes.
	"""
	
	cran = "AutoPipe" 

	version("0.1.6", md5="d085d425db3464db8f16f34e79806960")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-pamr", type=("build", "run"))
	depends_on("r-siggenes", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-consensusclusterplus", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-msigdbr", type=("build", "run"))
