# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGripp(RPackage):
	"""General Inverse Problem Platform

	Set of functions designed to solve inverse problems. The direct problem is used to calculate a cost function to be minimized.
  Here are listed some papers using Inverse Problems solvers and sensitivity analysis:
  (Jader Lugon Jr.; Antonio J. Silva Neto 2011) <doi:10.1590/S1678-58782011000400003>.
  (Jader Lugon Jr.; Antonio J. Silva Neto; Pedro P.G.W. Rodrigues 2008) <doi:10.1080/17415970802082864>.
  (Jader Lugon Jr.; Antonio J. Silva Neto; Cesar C. Santana 2008) <doi:10.1080/17415970802082922>.
	"""
	
	cran = "gripp" 

	version("0.2.20", md5="0389ba9d7dd9e4b5358b3f95e691f6b1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
