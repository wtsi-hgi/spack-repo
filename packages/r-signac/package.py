# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignac(RPackage):
	"""Analysis of Single-Cell Chromatin Data.

	A framework for the analysis and exploration of single-cell chromatin data.
	The 'Signac' package contains functions for quantifying single-cell
	chromatin data, computing per-cell quality control metrics, dimension
	reduction and normalization, visualization, and DNA sequence motif
	analysis. Reference: Stuart et al. (2021)
	<doi:10.1038/s41592-021-01282-5>."""

	cran = "Signac"

	version("1.12.0", md5="3248e7c85395070471afa4279d6a0faf")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.29.3:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-seuratobject@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("zlib", type=("build", "zlib", "run"))
