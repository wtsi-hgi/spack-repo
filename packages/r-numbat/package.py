# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNumbat(RPackage):
	"""Haplotype-Aware CNV Analysis from scRNA-Seq

	A computational method that infers copy number variations (CNVs) in cancer scRNA-seq data and reconstructs the tumor phylogeny. 'numbat' integrates signals from gene expression, allelic ratio, and population haplotype structures to accurately infer allele-specific CNVs in single cells and reconstruct their lineage relationship. 'numbat' can be used to: 1. detect allele-specific copy number variations from single-cells; 2. differentiate tumor versus normal cells in the tumor microenvironment; 3. infer the clonal architecture and evolutionary history of profiled tumors. 'numbat' does not require tumor/normal-paired DNA or genotype data, but operates solely on the donor scRNA-data data (for example, 10x Cell Ranger output). Additional examples and documentations are available at <https://kharchenkolab.github.io/numbat/>. For details on the method please see Gao et al. Nature Biotechnology (2022) <doi:10.1038/s41587-022-01468-y>.
	"""
	
	homepage = "https://github.com/kharchenkolab/numbat/"
	cran = "numbat" 

	version("1.3.2-1", md5="3c780d001b05c7e00ff4927fb04ef7ee")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-optparse", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-scistreer@1.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vcfr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-roptim", type=("build", "run"))
