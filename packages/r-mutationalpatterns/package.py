# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMutationalpatterns(RPackage):
	"""Comprehensive genome-wide analysis of mutational processes

	Mutational processes leave characteristic footprints in genomic DNA. This package provides a comprehensive set of flexible functions that allows researchers to easily evaluate and visualize a multitude of mutational patterns in base substitution catalogues of e.g. healthy samples, tumour samples, or DNA-repair deficient cells. The package covers a wide range of patterns including: mutational signatures, transcriptional and replicative strand bias, lesion segregation, genomic distribution and association with genomic features, which are collectively meaningful for studying the activity of mutational processes. The package works with single nucleotide variants (SNVs), insertions and deletions (Indels), double base substitutions (DBSs) and larger multi base substitutions (MBSs). The package provides functionalities for both extracting mutational signatures de novo and determining the contribution of previously identified mutational signatures on a single sample level. MutationalPatterns integrates with common R genomic analysis workflows and allows easy association with (publicly available) annotation data.
	"""
	
	homepage = "https://doi.org/doi:10.1186/s12864-022-08357-3"
	bioc = "MutationalPatterns" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MutationalPatterns_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MutationalPatterns/MutationalPatterns_3.12.0.tar.gz"]

	version("3.12.0", sha256="242b28877a9dab664cada4fc96107cbd25c56fa22804601b3ce2a86bba22caa7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-genomicranges@1.24:", type=("build", "run"))
	depends_on("r-nmf@0.20.6:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics@0.18:", type=("build", "run"))
	depends_on("r-bsgenome@1.40:", type=("build", "run"))
	depends_on("r-variantannotation@1.18.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-pracma@1.8.8:", type=("build", "run"))
	depends_on("r-iranges@2.6:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.12:", type=("build", "run"))
	depends_on("r-biostrings@2.40:", type=("build", "run"))
	depends_on("r-ggdendro@0.1.20:", type=("build", "run"))
	depends_on("r-cowplot@0.9.2:", type=("build", "run"))
	depends_on("r-ggalluvial@0.12.2:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
