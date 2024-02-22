# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTangramPipe(RPackage):
	"""Row-by-Row Table Building

	Builds tables with customizable rows. Users can specify the type
             of data to use for each row, as well as how to handle missing
             data and the types of comparison tests to run on the table
             columns.
	"""
	
	homepage = "https://github.com/thomasgstewart/tangram.pipe"
	cran = "tangram.pipe" 

	version("1.1.2", md5="0649c33f9796226060b762d318cbfd18")

	depends_on("r-dplyr", type=("build", "run"))
