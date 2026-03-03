# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtable(RPackage):
	"""Easy Table

	Creates simple to highly customized tables for a wide selection of descriptive statistics, with or without weighting the data.
	"""
	
	cran = "etable" 

	version("1.3.1", md5="4442915b5008d135d39c42ba63de7fa5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
