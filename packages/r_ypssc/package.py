# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYpssc(RPackage):
	"""Yeast-Proteome Secondary-Structure Calculator

	An extension for 'NetSurfP-2.0' (Klausen et al. (2019) <doi:10.1002/prot.25674>)
    which is specifically designed to analyze the results of bottom-up-proteomics that is
    primarily analyzed with 'MaxQuant' (Cox, J., Mann, M. (2008) <doi:10.1038/nbt.1511>).
    This tool is designed to process a large number of yeast peptides that produced as a
    results of whole yeast cell-proteome digestion and provide a coherent picture of
    secondary structure of proteins.
	"""
	
	cran = "ypssc" 

	version("1.1.0", md5="b9ff21e4dcd5567167c6655c9413465d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-spelling", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-eulerr", type=("build", "run"))
	depends_on("r-peptides", type=("build", "run"))
	depends_on("r-svdialogs", type=("build", "run"))
