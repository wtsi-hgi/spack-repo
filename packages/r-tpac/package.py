# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpac(RPackage):
	"""Tissue-Adjusted Pathway Analysis of Cancer (TPAC)

	Contains logic for single sample gene set testing of cancer transcriptomic data with adjustment for normal tissue-specificity.
  Frost, H. Robert (2023) "Tissue-adjusted pathway analysis of cancer (TPAC)" <doi:10.1101/2022.03.17.484779>.
	"""
	
	cran = "TPAC" 

	version("0.2.0", md5="5b490784df6cb8080d1982ea894e825a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tpacdata", type=("build", "run"))
