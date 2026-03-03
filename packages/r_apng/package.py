# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApng(RPackage):
	"""Convert Png Files into Animated Png

	Convert several png files into an animated png file.
  This package exports only a single function `apng'. Call the
  apng function with a vector of file names (which should be
  png files) to convert them to a single animated png file.
	"""
	
	cran = "apng" 

	version("1.1", md5="794e7b20ecd6db2feac01ebc44daa2f2")

	depends_on("r-bitops", type=("build", "run"))
