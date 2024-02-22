# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTth(RPackage):
	"""TeX-to-HTML/MathML Translators TtH/TtM

	C source code and R wrappers for the tth/ttm TeX-to-HTML/MathML translators.
	"""
	
	cran = "tth" 

	version("4.12-0-1", md5="55a8d965adbbfd5cde2cf64d0716ac8e")

	depends_on("r@3:", type=("build", "run"))
