# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnisensr(RPackage):
	"""Read 'Unisens' Data

	Provides the ability to read 'Unisens' data into R. 'Unisens' is a universal data format for multi sensor data.
	"""
	
	homepage = "http://unisens.org/"
	cran = "unisensR" 

	version("0.3.3", md5="78dbf117eb1ffbb59d2d1821a7f5cdc2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-xml@1:", type=("build", "run"))
	depends_on("r-hexview", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
