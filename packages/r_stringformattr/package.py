# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStringformattr(RPackage):
	"""Dynamic String Formatting

	Pass named and unnamed character vectors into specified positions
    in strings. This represents an attempt to replicate some of python's string
    formatting.
	"""
	
	cran = "stringformattr" 

	version("0.1.2", md5="1b0f2a3e990780cede771485212096fa")

	depends_on("r-stringr", type=("build", "run"))
