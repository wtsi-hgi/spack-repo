# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTnbcCms(RPackage):
	"""TNBC.CMS: Prediction of TNBC Consensus Molecular Subtypes

	This package implements a machine learning-based classifier for the assignment of consensus molecular subtypes to TNBC samples. It also provides functions to summarize genomic and clinical characteristics.
	"""
	
	bioc = "TNBC.CMS"

	version("1.18.0", commit="7ce7eb8a112f957b4a3b24bb7873414e12c2613a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-gsva@1.26:", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
