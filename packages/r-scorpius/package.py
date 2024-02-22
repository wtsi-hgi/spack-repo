# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScorpius(RPackage):
	"""Inferring Developmental Chronologies from Single-Cell RNA
Sequencing Data

	An accurate and easy tool for performing linear trajectory inference on
  single cells using single-cell RNA sequencing data. In addition, 'SCORPIUS'
  provides functions for discovering the most important genes with respect to
  the reconstructed trajectory, as well as nice visualisation tools.
  Cannoodt et al. (2016) <doi:10.1101/079509>.
	"""
	
	homepage = "https://github.com/rcannood/SCORPIUS"
	cran = "SCORPIUS" 

	version("1.0.9", md5="ad32ff4e2c2fa5315080ea4952400080")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dynutils@1.0.3:", type=("build", "run"))
	depends_on("r-dynwrap", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-lmds", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-princurve@2.1.4:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
