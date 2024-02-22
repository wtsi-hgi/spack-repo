# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigminer(RPackage):
	"""Extract, Analyze and Visualize Mutational Signatures for Genomic
Variations

	Genomic alterations including single nucleotide substitution,
    copy number alteration, etc. are the major force for cancer
    initialization and development. Due to the specificity of molecular
    lesions caused by genomic alterations, we can generate characteristic
    alteration spectra, called 'signature' (Wang, Shixiang, et al. (2021)
    <DOI:10.1371/journal.pgen.1009557> & Alexandrov, Ludmil B., et al.
    (2020) <DOI:10.1038/s41586-020-1943-3> & Steele Christopher D., et al.
    (2022) <DOI:10.1038/s41586-022-04738-6>).  This package helps users to
    extract, analyze and visualize signatures from genomic alteration
    records, thus providing new insight into cancer study.
	"""
	
	homepage = "https://github.com/ShixiangWang/sigminer"
	cran = "sigminer" 

	version("2.3.0", md5="bebe08aa7bdf6202fdcd949704382f7b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli@2:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr@0.2:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-maftools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
