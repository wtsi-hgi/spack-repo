# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLucidus(RPackage):
	"""LUCID with Multiple Omics Data

	An implementation of estimating the Latent Unknown Clusters By Integrating Multi-omics Data (LUCID) model (Peng (2019) <doi:10.1093/bioinformatics/btz667>). LUCID conducts integrated clustering using exposures, omics data (and outcome as an option). This is a major update from the last version while conserving all the previous features. This package implements three different integration strategies for multiple omics data analysis within the LUCID framework: LUCID early integration (the original LUCID model), LUCID in parallel (intermediate), and LUCID in serial (late). Automated model selection for each LUCID model is available to obtain the optimal number of latent clusters, and an integrated imputation approach is implemented to handle sporadic and list-wise missing multiple omics data.
	"""
	
	cran = "LUCIDus" 

	version("3.0.1", md5="34e6dad515298d68074880b4cd936b29")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
