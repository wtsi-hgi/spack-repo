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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scPCA_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scPCA/scPCA_1.16.0.tar.gz"]

	version("1.16.0", sha256="c27df5020915ff86c23b0faa81782b65c5eaff1285b66e17405004e469d37c1b")

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
