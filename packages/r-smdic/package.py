# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmdic(RPackage):
	"""Identification of Somatic Mutation-Driven Immune Cells

	A computing tool is developed to automated identify somatic mutation-driven immune cells. The operation modes including: i) inferring the relative abundance matrix of tumor-infiltrating immune cells and integrating it with a particular gene mutation status, ii) detecting differential immune cells with respect to the gene mutation status and converting the abundance matrix of significant differential immune cell into two binary matrices (one for up-regulated and one for down-regulated), iii) identifying somatic mutation-driven immune cells by comparing the gene mutation status with each immune cell in the binary matrices across all samples, and iv) visualization of immune cell abundance of samples in different mutation status..
	"""
	
	cran = "SMDIC" 

	version("0.1.5", md5="08eb8977fb8567bfb34d855edf10486c")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-samr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-maftools", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
