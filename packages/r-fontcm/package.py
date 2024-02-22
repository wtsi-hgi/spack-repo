# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFontcm(RPackage):
	"""Computer Modern font for use with extrafont package

	Computer Modern font for use with extrafont package
	"""
	
	homepage = "https://github.com/wch/fontcm"
	cran = "fontcm" 

	version("1.1", md5="524cbcbe4f297e7aacb5dd093e4541bf")

	depends_on("r@2.14:", type=("build", "run"))
