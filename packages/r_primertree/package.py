# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrimertree(RPackage):
	"""Visually Assessing the Specificity and Informativeness of Primer
Pairs

	Identifies potential target sequences for a given
    set of primers and generates phylogenetic trees annotated with the
    taxonomies of the predicted amplification products.
	"""
	
	cran = "primerTree" 

	version("1.0.6", md5="36856e8c2266c968413c5b91bba3aa03")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-directlabels", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
