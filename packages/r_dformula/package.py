# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDformula(RPackage):
	"""Data Manipulation using Formula

	A tool for manipulating data using the generic formula. A single formula allows to easily add, replace and remove variables before running the analysis. 
	"""
	
	homepage = "https://github.com/serafinialessio/dformula"
	cran = "dformula" 

	version("1.0", md5="3aa9ebab6e96036cec5f467eb9bbdf6d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-formula-tools@1.7.1:", type=("build", "run"))
