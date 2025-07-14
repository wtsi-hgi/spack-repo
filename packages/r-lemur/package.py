# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLemur(RPackage):
	"""Latent Embedding Multivariate Regression

	Fit a latent embedding multivariate regression (LEMUR) model to multi-condition single-cell data. The model provides a parametric description of single-cell data measured with complex experimental designs. The parametric model is used to (1) align conditions, (2) predict log fold changes between conditions for all cells, and (3) identify cell neighborhoods with consistent log fold changes. For those neighborhoods, a pseudobulked differential expression test is conducted to assess which genes are significantly changed.
	"""
	
	homepage = "https://github.com/const-ae/lemur"
	bioc = "lemur" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/lemur_1.0.5.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/lemur/lemur_1.0.5.tar.gz"]

	version("1.6.1", tag="RELEASE_3_21")
	version("1.0.5", sha256="404872c1445449b5bc268054627e456a1d074f3c05f3cacf78da2572ead1e980")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-glmgampoi@1.12:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-harmony", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
