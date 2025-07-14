# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnits(RPackage):
	"""R Normalization and Inference of Time Series data

	R/Bioconductor package for normalization, curve registration and inference in time course gene expression data.
	"""
	
	bioc = "Rnits"

	version("1.42.0", commit="cdb1317bc9d3450bbc576f491462a70b239d0c2a")
	version("1.36.0", commit="f7e2d12c89f0e4f58f758eafecec39412028822d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
