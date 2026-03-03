# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRabhit(RPackage):
	"""Inference Tool for Antibody Haplotype

	Infers V-D-J haplotypes and gene deletions from AIRR-seq data for Ig and TR chains, 
    based on J, D, or V genes as anchor, by adapting a Bayesian framework.
    It also calculates a Bayes factor, a number that indicates the certainty level of the inference, for each haplotyped gene.
    Citation:
    Gidoni, et al (2019) <doi:10.1038/s41467-019-08489-3>.
    Peres and Gidoni, et al (2019) <doi:10.1093/bioinformatics/btz481>.
	"""
	
	homepage = "https://yaarilab.bitbucket.io/RAbHIT/"
	cran = "rabhit" 

	version("0.2.5", md5="cb5a30533d3aa80d33657c9e5abfc85e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-plotly@4.7.1:", type=("build", "run"))
	depends_on("r-gtools@3.5:", type=("build", "run"))
	depends_on("r-cowplot@0.9.1:", type=("build", "run"))
	depends_on("r-readr@2.1.1:", type=("build", "run"))
	depends_on("r-dendextend@1.9:", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.5:", type=("build", "run"))
	depends_on("r-ggdendro@0.1.20:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-alakazam@1:", type=("build", "run"))
	depends_on("r-tigger@1:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.3:", type=("build", "run"))
	depends_on("r-gtable@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-stringi@1.4.3:", type=("build", "run"))
	depends_on("r-splitstackshape@1.4.8:", type=("build", "run"))
	depends_on("r-fastmatch@1.1:", type=("build", "run"))
