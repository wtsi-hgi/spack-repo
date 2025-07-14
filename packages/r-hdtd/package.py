# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdtd(RPackage):
	"""Statistical Inference about the Mean Matrix and the Covariance Matrices in High-Dimensional Transposable Data (HDTD)

	Characterization of intra-individual variability using physiologically relevant measurements provides important insights into fundamental biological questions ranging from cell type identity to tumor development. For each individual, the data measurements can be written as a matrix with the different subsamples of the individual recorded in the columns and the different phenotypic units recorded in the rows. Datasets of this type are called high-dimensional transposable data. The HDTD package provides functions for conducting statistical inference for the mean relationship between the row and column variables and for the covariance structure within and between the row and column variables.
	"""
	
	homepage = "http://github.com/AnestisTouloumis/HDTD"
	bioc = "HDTD"

	version("1.42.0", commit="eb9cf5f2a2398bc4a7b35ab452fea37aad8993f7")
	version("1.36.0", commit="d256737c58619038c8ef3dbabf1498fa1e370bd6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
