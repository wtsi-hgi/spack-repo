# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmvconnect(RPackage):
	"""Connect to the 'jamovi' Statistical Spreadsheet

	Methods to access data sets from the 'jamovi' statistical
  spreadsheet (see <https://www.jamovi.org> for more information) from R.
	"""
	
	cran = "jmvconnect" 

	version("2.3.13", md5="e08cb58ad2c295066fe5f253b28f8f45")

	depends_on("r-jmvcore@2.3.12:", type=("build", "run"))
	depends_on("r-evaluate", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
