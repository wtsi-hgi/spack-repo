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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SCnorm_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SCnorm/SCnorm_1.24.0.tar.gz"]

    version("1.30.1", tag="RELEASE_3_21")
	version("1.24.0", sha256="21889d382ea33a37a615d7296748840894775f4c583dc4d40e251f9bda0337b4")

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
