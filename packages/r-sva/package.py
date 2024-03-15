# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSva(RPackage):
	"""Surrogate Variable Analysis.

	The sva package contains functions for removing batch effects and other
	unwanted variation in high-throughput experiment. Specifically, the sva
	package contains functions for the identifying and building surrogate
	variables for high-dimensional data sets. Surrogate variables are
	covariates constructed directly from high-dimensional data (like gene
	expression/RNA sequencing/methylation/brain imaging data) that can be
	used in subsequent analyses to adjust for unknown, unmodeled, or latent
	sources of noise. The sva package can be used to remove artifacts in
	three ways: (1) identifying and estimating surrogate variables for
	unknown sources of variation in high-throughput experiments (Leek and
	Storey 2007 PLoS Genetics,2008 PNAS), (2) directly removing known batch
	effects using ComBat (Johnson et al. 2007 Biostatistics) and (3)
	removing batch effects with known control probes (Leek 2014 biorXiv).
	Removing batch effects and using surrogate variables in differential
	expression analysis have been shown to reduce dependence, stabilize
	error rate estimates, and improve reproducibility, see (Leek and Storey
	2007 PLoS Genetics, 2008 PNAS or Leek et al. 2011 Nat. Reviews
	Genetics)."""

	bioc = "sva"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sva_3.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sva/sva_3.50.0.tar.gz"]

	version("3.50.0", md5="8c42cd3e23be4d24f072d98394931552")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
