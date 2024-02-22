# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpeedytax(RPackage):
	"""Rapidly Import Classifier Results into 'phyloseq'

	Import classification results from the 'RDP Classifier' (Ribosomal Database Project),' 'USEARCH sintax,' 'vsearch sintax' and the 'QIIME2' (Quantitative Insights into Microbial Ecology) classifiers into 'phyloseq' tax_table objects.
	"""
	
	cran = "speedytax" 

	version("1.0.3", md5="5653fc0cd76e58b7b6cadbfe427983b0")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
