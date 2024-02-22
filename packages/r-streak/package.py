# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStreak(RPackage):
	"""Receptor Abundance Estimation using Feature Selection and Gene
Set Scoring

	Performs receptor abundance estimation for single cell RNA-sequencing data using a supervised feature selection mechanism and a thresholded gene set scoring procedure. Seurat's normalization method is described in: Hao et al., (2021) <doi:10.1016/j.cell.2021.04.048>, Stuart et al., (2019) <doi:10.1016/j.cell.2019.05.031>, Butler et al., (2018) <doi:10.1038/nbt.4096> and Satija et al., (2015) <doi:10.1038/nbt.3192>. Method for reduced rank reconstruction and rank-k selection is detailed in: Javaid et al., (2022) <doi:10.1101/2022.10.08.511197>. Gene set scoring procedure is described in: Frost et al., (2020) <doi:10.1093/nar/gkaa582>. Clustering method is outlined in: Song et al., (2020) <doi:10.1093/bioinformatics/btaa613> and Wang et al., (2011) <doi:10.32614/RJ-2011-015>.
	"""
	
	cran = "STREAK" 

	version("1.0.0", md5="e63fc004336e0aa5c99f8cf3ce5320dd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ckmeans-1d-dp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-speck", type=("build", "run"))
	depends_on("r-vam", type=("build", "run"))
