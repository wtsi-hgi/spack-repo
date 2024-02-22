# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlakazam(RPackage):
	"""Immunoglobulin Clonal Lineage and Diversity Analysis

	Provides methods for high-throughput adaptive immune 
    receptor repertoire sequencing (AIRR-Seq; Rep-Seq) analysis. In 
    particular, immunoglobulin (Ig) sequence lineage reconstruction, 
    lineage topology analysis, diversity profiling, amino acid property 
    analysis and gene usage.
    Citations: 
    Gupta and Vander Heiden, et al (2017) <doi:10.1093/bioinformatics/btv359>,
    Stern, Yaari and Vander Heiden, et al (2014) <doi:10.1126/scitranslmed.3008879>.
	"""
	
	homepage = "https://alakazam.readthedocs.io/"
	cran = "alakazam" 

	version("1.3.0", md5="aef6659ef46836fe6b03da34625261b2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-airr@1.4.1:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-igraph@1.5:", type=("build", "run"))
	depends_on("r-matrix@1.3.0:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-biostrings@2.56:", type=("build", "run"))
	depends_on("r-genomicalignments@1.24:", type=("build", "run"))
	depends_on("r-iranges@2.22.2:", type=("build", "run"))
