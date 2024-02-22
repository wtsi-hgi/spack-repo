# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPermpath(RPackage):
	"""Permutation Based Gene Expression Pathway Analysis

	Can be used to carry out permutation based gene expression pathway analysis. This work was supported by a National Institute of Allergy and Infectious Disease/National Institutes of Health contract (No. HHSN272200900059C). 
	"""
	
	cran = "permPATH" 

	version("1.3", md5="4463d16a30cfceda37be995d49968029")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-r2html@2.3.2:", type=("build", "run"))
	depends_on("r-xtable@1.8.2:", type=("build", "run"))
