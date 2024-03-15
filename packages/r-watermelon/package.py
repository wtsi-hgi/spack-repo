# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWatermelon(RPackage):
	"""Illumina 450 methylation array normalization and metrics.

	15 flavours of betas and three performance metrics, with methods for
	objects produced by methylumi and minfi packages."""

	bioc = "wateRmelon"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/wateRmelon_2.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/wateRmelon/wateRmelon_2.8.0.tar.gz"]

	version("2.8.0", md5="dd08402958a5cc50170669a5f17e44f6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-methylumi", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))
	depends_on("r-roc", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))
