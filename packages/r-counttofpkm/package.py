# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCounttofpkm(RPackage):
	"""Convert Counts to Fragments per Kilobase of Transcript per
Million (FPKM)

	Implements the algorithm described in Trapnell,C. et al. (2010) <doi: 10.1038/nbt.1621>. This function takes read counts matrix of RNA-Seq data, feature lengths which can be retrieved using 'biomaRt' package, and the mean fragment lengths which can be calculated using the 'CollectInsertSizeMetrics(Picard)' tool. It then returns a matrix of FPKM normalised data by library size and feature effective length. It also provides the user with a quick and reliable function to generate FPKM heatmap plot of the highly variable features in RNA-Seq dataset.
	"""
	
	homepage = "https://github.com/AAlhendi1707/countToFPKM"
	cran = "countToFPKM" 

	version("1.0", md5="11448a314fcedd53a4a9c7dd2c930ce4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
