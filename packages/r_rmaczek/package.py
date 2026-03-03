# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmaczek(RPackage):
	"""Czekanowski's Diagrams

	Allows for production of Czekanowski's Diagrams. See K. Bartoszek, A. Vasterlund (2020) <doi:10.2478/bile-2020-0008>.
	"""
	
	cran = "RMaCzek" 

	version("1.5.1", md5="cfee03eb7d7888ff046dc8daac5b77d0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ga@3.2:", type=("build", "run"))
	depends_on("r-seriation@1.3.4:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ecp", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
