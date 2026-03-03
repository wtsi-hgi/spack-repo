# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetaclust(RPackage):
	"""A Family of Beta Mixture Models for Clustering Beta-Valued DNA
Methylation Data

	A family of novel beta mixture models (BMMs) has been developed by Majumdar et al. (2022) <arXiv:2211.01938v1> to appositely model the beta-valued cytosine-guanine dinucleotide (CpG) sites, to objectively identify methylation state thresholds and to identify the differentially methylated CpG (DMC) sites using a model-based clustering approach. The family of beta mixture models employs different parameter constraints applicable to different study settings. The EM algorithm is used for parameter estimation, with a novel approximation during the M-step providing tractability and ensuring computational feasibility.
	"""
	
	cran = "betaclust" 

	version("1.0.3", md5="0b8b4a088d300c78fd74562e78adc8bd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
