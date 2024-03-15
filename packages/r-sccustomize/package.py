# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSccustomize(RPackage):
	"""Custom Visualizations & Functions for Streamlined Analyses of
Single Cell Sequencing

	Collection of functions created and/or curated to aid in the visualization and analysis of single-cell data using 'R'.  'scCustomize' aims to provide 1) Customized visualizations for aid in ease of use and to create more aesthetic and functional visuals. 2) Improve speed/reproducibility of common tasks/pieces of code in scRNA-seq analysis with a single or group of functions.  For citation please use: Marsh SE (2021) "Custom Visualizations & Functions for Streamlined Analyses of Single Cell Sequencing" <doi:10.5281/zenodo.5706430> RRID:SCR_024675.
	"""
	
	homepage = "https://github.com/samuel-marsh/scCustomize"
	cran = "scCustomize" 

	version("2.1.2", md5="5409a8b8f7f5c6a3d215d1100ca6d406")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-seurat@4.3.0.1:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-cli@3.2:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggprism", type=("build", "run"))
	depends_on("r-ggrastr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix@1.5:", type=("build", "run"))
	depends_on("r-paletteer", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.1.3:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-scattermore@1.2:", type=("build", "run"))
	depends_on("r-seuratobject@5:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
