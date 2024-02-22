# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetnet(RPackage):
	"""Inferring metabolic networks from untargeted high-resolution mass spectrometry data

	MetNet contains functionality to infer metabolic network topologies from quantitative data and high-resolution mass/charge information. Using statistical models (including correlation, mutual information, regression and Bayes statistics) and quantitative data (intensity values of features) adjacency matrices are inferred that can be combined to a consensus matrix. Mass differences calculated between mass/charge values of features will be matched against a data frame of supplied mass/charge differences referring to transformations of enzymatic activities. In a third step, the two levels of information are combined to form a adjacency matrix inferred from both quantitative and structure information.
	"""
	
	bioc = "MetNet" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MetNet_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MetNet/MetNet_1.20.0.tar.gz"]

	version("1.20.0", md5="0e03ec28e1272f094758907923a0226f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-s4vectors@0.28.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.20:", type=("build", "run"))
	depends_on("r-bnlearn@4.3:", type=("build", "run"))
	depends_on("r-biocparallel@1.12:", type=("build", "run"))
	depends_on("r-corpcor@1.6.10:", type=("build", "run"))
	depends_on("r-dplyr@1.0.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-genenet@1.2.15:", type=("build", "run"))
	depends_on("r-genie3@1.7:", type=("build", "run"))
	depends_on("r-parmigene@1.0.2:", type=("build", "run"))
	depends_on("r-psych@2.1.6:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-stabs@0.6:", type=("build", "run"))
	depends_on("r-tibble@3.0.5:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
