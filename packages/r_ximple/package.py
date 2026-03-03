# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXimple(RPackage):
	"""A Simple XML Tree Parser and Generator

	Provides a simple XML tree parser/generator. It includes functions to read XML files into R objects, get information out of and into nodes, and write R objects back
                    to XML code. It's not as powerful as the 'XML' package and doesn't aim to be, but for simple XML handling it could be useful. It was originally developed for
                    the R GUI and IDE 'RKWard' <https://rkward.kde.org>, to make plugin development easier.
	"""
	
	homepage = "https://reaktanz.de/?c=hacking&s=XiMpLe"
	cran = "XiMpLe" 

	version("0.11-2", md5="80f798c670f3423b338cbf754d0c5c4c")

	depends_on("r@3.5:", type=("build", "run"))
