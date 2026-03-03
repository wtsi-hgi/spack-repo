# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJgsbook(RPackage):
	"""Package of the German Book "Statistik mit R und RStudio" by
Joerg grosse Schlarmann

	All datasets and functions used in the german book "Statistik mit R und RStudio" by grosse Schlarmann (2022) <https://www.produnis.de/R/>.
	"""
	
	cran = "jgsbook" 

	version("1.0.4", md5="696c4621cae0d7cc22a61af535db12b6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-statip", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
