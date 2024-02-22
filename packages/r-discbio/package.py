# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscbio(RPackage):
	"""A User-Friendly Pipeline for Biomarker Discovery in Single-Cell
Transcriptomics

	An open, multi-algorithmic pipeline for easy, fast and efficient
  analysis of cellular sub-populations and the molecular signatures that
  characterize them. The pipeline consists of four successive steps: data
  pre-processing, cellular clustering with pseudo-temporal ordering, defining
  differential expressed genes and biomarker identification. More details on
  Ghannoum et. al. (2021) <doi:10.3390/ijms22031399>. This package implements
  extensions of the work published by Ghannoum et. al. (2019)
  <doi:10.1101/700989>.
	"""
	
	homepage = "https://github.com/ocbe-uio/DIscBIO"
	cran = "DIscBIO" 

	version("1.2.2", md5="32fdda52d227d60e65cc4db8170a9c40")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-tscan", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rweka", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-netindices", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-tsne", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
