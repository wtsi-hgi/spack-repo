# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScpca(RPackage):
	"""Sparse Contrastive Principal Component Analysis

	A toolbox for sparse contrastive principal component analysis (scPCA) of high-dimensional biological data. scPCA combines the stability and interpretability of sparse PCA with contrastive PCA's ability to disentangle biological signal from unwanted variation through the use of control data. Also implements and extends cPCA.
	"""
	
	homepage = "https://github.com/PhilBoileau/scPCA"
	bioc = "scPCA"

	version("1.22.0", commit="d0f461c3a68227c788d1561a82b2e5c6f0593eaa")
	version("1.16.0", commit="5f06cd0fb8e46b9a2193a6debb92e47c754087a4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
	depends_on("r-sparsepca", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-origami", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-coop", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-scaledmatrix", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
