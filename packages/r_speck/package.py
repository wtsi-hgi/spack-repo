# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpeck(RPackage):
	"""Receptor Abundance Estimation using Reduced Rank Reconstruction
and Clustered Thresholding

	Surface Protein abundance Estimation using CKmeans-based clustered thresholding ('SPECK') is an unsupervised learning-based method that performs receptor abundance estimation for single cell RNA-sequencing data based on reduced rank reconstruction (RRR) and a clustered thresholding mechanism. Seurat's normalization method is described in: Hao et al., (2021) <doi:10.1016/j.cell.2021.04.048>, Stuart et al., (2019) <doi:10.1016/j.cell.2019.05.031>, Butler et al., (2018) <doi:10.1038/nbt.4096> and Satija et al., (2015) <doi:10.1038/nbt.3192>. Method for the RRR is further detailed in: Erichson et al., (2019) <doi:10.18637/jss.v089.i11> and Halko et al., (2009) <arXiv:0909.4061>. Clustering method is outlined in: Song et al., (2020) <doi:10.1093/bioinformatics/btaa613> and Wang et al., (2011) <doi:10.32614/RJ-2011-015>.
	"""
	
	cran = "SPECK" 

	version("1.0.0", md5="4650bc6aba7d67ddd06f099acfd1129c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ckmeans-1d-dp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix@1.6.1.1:", type=("build", "run"))
	depends_on("r-rsvd", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
