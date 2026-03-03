# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKaryotapr(RPackage):
	"""DNA Copy Number Analysis for Genome-Wide Tapestri Panels

	Analysis of DNA copy number in single cells using 
    custom genome-wide targeted DNA sequencing panels for the Mission Bio 
    Tapestri platform. Users can easily parse, manipulate, and visualize 
    datasets produced from the automated 'Tapestri Pipeline', with support for 
    normalization, clustering, and copy number calling. Functions are also 
    available to deconvolute multiplexed samples by genotype and parsing 
    barcoded reads from exogenous lentiviral constructs.
	"""
	
	homepage = "https://github.com/joeymays/karyotapR"
	cran = "karyotapR" 

	version("1.0.1", md5="5f9e82f919046d7f6323d767db1645ab")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
