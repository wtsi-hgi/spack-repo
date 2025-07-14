# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScnorm(RPackage):
	"""Normalization of single cell RNA-seq data

	This package implements SCnorm — a method to normalize single-cell RNA-seq data.
	"""
	
	homepage = "https://github.com/rhondabacher/SCnorm"
	bioc = "SCnorm"

	version("1.30.1", commit="c8694b88b2919005caad7ed1eea85c143c970d47")
	version("1.24.0", commit="a500413ee9ba73880d062c01057e67ea11514c54")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
