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

	version("1.80.0", commit="8b80c73508a9e3ef047d6230482a4cb1d900eacb")
	version("1.74.0", commit="55ea81cc9b3f9efafbc8e597aec7d9c783db8a21")

	depends_on("r@2.3.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-venn", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
