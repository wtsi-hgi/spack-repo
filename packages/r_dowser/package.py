# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDowser(RPackage):
	"""B Cell Receptor Phylogenetics Toolkit

	Provides a set of functions for inferring, visualizing, and analyzing B cell phylogenetic trees.
    Provides methods to 1) reconstruct unmutated ancestral sequences,
    2) build B cell phylogenetic trees using multiple methods,
    3) visualize trees with metadata at the tips,
    4) reconstruct intermediate sequences,
    5) detect biased ancestor-descendant relationships among metadata types
    Workflow examples available at documentation site (see URL).
    Citations:
    Hoehn et al (2022) <doi:10.1371/journal.pcbi.1009885>,
    Hoehn et al (2021) <doi:10.1101/2021.01.06.425648>.
	"""
	
	homepage = "https://dowser.readthedocs.io"
	cran = "dowser" 

	version("2.1.0", md5="01eaa91c5aad373a12ee8e8facc311e2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-alakazam@1.1:", type=("build", "run"))
	depends_on("r-ape@5.6:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-phangorn@2.7.1:", type=("build", "run"))
	depends_on("r-phylotate", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shazam@1.1.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
