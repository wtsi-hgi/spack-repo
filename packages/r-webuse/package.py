# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebuse(RPackage):
	"""Import Stata 'webuse' Datasets

	A Stata-style `webuse()` function for importing named datasets from Stata's online collection.
	"""
	
	homepage = "https://github.com/leeper/webuse"
	cran = "webuse" 

	version("0.1.3", md5="3c1b848ee81070560d2adddcf101bb8d")

	depends_on("r-haven", type=("build", "run"))
