# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReplacer(RPackage):
	"""A Value Replacement Utility

	Updates values within csv format data files using a custom, User-built
    csv format lookup file. Based on 'data.table' package.
	"""
	
	cran = "replacer" 

	version("1.0.2", md5="e1a212efbfd76a086eb43eac14f8600a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
