# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmgampoi(RPackage):
	"""Fit a Gamma-Poisson Generalized Linear Model.

	Fit linear models to overdispersed count data.  The package can estimate
	the overdispersion and fit repeated models for matrix input. It is designed
	to handle large input datasets as they typically occur in single cell
	RNA-seq experiments."""

	bioc = "glmGamPoi"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/glmGamPoi_1.14.3.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/glmGamPoi/glmGamPoi_1.14.3.tar.gz"]

	version("1.14.3", md5="a713a5c0adddd2e5f4d30e02af38d309")
	version("1.6.0", sha256="55e292e994ff4e51062e2eb63b3e9c79cb0c03440fcb4fc5e78a81903cfbcef9", url="https://bioconductor.org/packages/3.14/bioc/src/contrib/glmGamPoi_1.6.0.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
