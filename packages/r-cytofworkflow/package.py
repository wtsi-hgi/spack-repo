# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytofworkflow(RPackage):
	"""CyTOF workflow: differential discovery in high-throughput high-dimensional cytometry datasets

	High-dimensional mass and flow cytometry (HDCyto) experiments have become a method of choice for high-throughput interrogation and characterization of cell populations. Here, we present an updated R-based pipeline for differential analyses of HDCyto data, largely based on Bioconductor packages. We computationally define cell populations using FlowSOM clustering, and facilitate an optional but reproducible strategy for manual merging of algorithm-generated clusters. Our workflow offers different analysis paths, including association of cell type abundance with a phenotype or changes in signaling markers within specific subpopulations, or differential analyses of aggregated signals. Importantly, the differential analyses we show are based on regression frameworks where the HDCyto data is the response; thus, we are able to model arbitrary experimental designs, such as those with batch effects, paired designs and so on. In particular, we apply generalized linear mixed models or linear mixed models to analyses of cell population abundance or cell-population-specific analyses of signaling markers, allowing overdispersion in cell count or aggregated signals across samples to be appropriately modeled. To support the formal statistical analyses, we encourage exploratory data analysis at every step, including quality control (e.g., multi-dimensional scaling plots), reporting of clustering results (dimensionality reduction, heatmaps with dendrograms) and differential analyses (e.g., plots of aggregated signals).
	"""
	
	homepage = "https://github.com/markrobinsonuzh/cytofWorkflow"
	bioc = "cytofWorkflow"

	version("1.32.0", commit="37be41802acddc75da5af1329ca100f74c275bcb")
	version("1.26.1", commit="a4b1c2158f26674a06651fb99be9723cd504ecf7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-catalyst", type=("build", "run"))
	depends_on("r-diffcyt", type=("build", "run"))
	depends_on("r-hdcytodata", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))

