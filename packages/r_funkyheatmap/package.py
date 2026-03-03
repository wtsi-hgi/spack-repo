# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunkyheatmap(RPackage):
	"""Generating Funky Heatmaps for Data Frames

	Allows generating heatmap-like visualisations for benchmark data 
  frames. Funky heatmaps can be fine-tuned by providing annotations of the 
  columns and rows, which allows assigning multiple palettes or geometries
  or grouping rows and columns together in categories.
  Saelens et al. (2019) <doi:10.1038/s41587-019-0071-9>.
	"""
	
	homepage = "https://funkyheatmap.github.io/funkyheatmap/"
	cran = "funkyheatmap" 

	version("0.5.0", md5="8d6e547168b799ef7ca1b7974910afa2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
