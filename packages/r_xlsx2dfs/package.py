# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXlsx2dfs(RPackage):
	"""Read and Write 'Excel' Sheets into and from List of Data Frames

	Reading and writing sheets of a single 'Excel' file into and from a list of data frames. Eases I/O of tabular data in bioinformatics while keeping them in a human readable format.
	"""
	
	cran = "xlsx2dfs" 

	version("0.1.0", md5="38a08d2c71fb8b7921ffe7bfad4c1d52")

	depends_on("r-openxlsx", type=("build", "run"))
