# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtlr(RPackage):
	"""Print Right-to-Left Languages Correctly

	Convenience functions to make some common tasks with right-to-left string
    printing easier, more convenient and with no need to remember long Unicode
    characters. Specifically helpful for right-to-left languages such as Arabic,
    Persian and Hebrew.
	"""
	
	homepage = "https://github.com/matanhakim/rtlr"
	cran = "rtlr" 

	version("0.1.0", md5="9ccc035570572cce294066b13a439099")

	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
