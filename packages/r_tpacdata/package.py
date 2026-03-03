# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpacdata(RPackage):
	"""Human Protein Atlas Data for Tissue-Adjusted Pathway Analysis of
Cancer (TPAC)

	Contains summary data on gene expression in normal human tissues from the Human Protein Atlas for use with the 
  Tissue-Adjusted Pathway Analysis of cancer (TPAC) method.
  Frost, H. Robert (2023) "Tissue-adjusted pathway analysis of cancer (TPAC)" <doi:10.1101/2022.03.17.484779>.
	"""
	
	cran = "TPACData" 

	version("0.1.0", md5="cb6e30ca0e226ebb0b9a4c72687215e2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
