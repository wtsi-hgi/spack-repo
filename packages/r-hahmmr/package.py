# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHahmmr(RPackage):
	"""Haplotype-Aware Hidden Markov Model for RNA

	Haplotype-aware Hidden Markov Model for RNA (HaHMMR) is a method for detecting copy number variations (CNVs) from bulk RNA-seq data. Additional examples, documentations, and details on the method are available at <https://github.com/kharchenkolab/hahmmr/>.
	"""
	
	cran = "hahmmr" 

	version("1.0.0", md5="2f0c92c43adf3ad544b8b5f8949955ba")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-roptim", type=("build", "run"))
