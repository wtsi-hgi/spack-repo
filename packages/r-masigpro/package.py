# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMasigpro(RPackage):
	"""Significant Gene Expression Profile Differences in Time Course Gene Expression Data

	maSigPro is a regression based approach to find genes for which there are significant gene expression profile differences between experimental groups in time course microarray and RNA-Seq experiments.
	"""
	
	bioc = "maSigPro" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/maSigPro_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/maSigPro/maSigPro_1.74.0.tar.gz"]

	version("1.80.0", tag="RELEASE_3_21")
	version("1.74.0", sha256="a867956d4948310e5ae4730901b14ac07c5e845b558d942391e893229d7d220a")

	depends_on("r@2.3.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-venn", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
