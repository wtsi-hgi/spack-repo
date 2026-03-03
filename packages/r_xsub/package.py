# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXsub(RPackage):
	"""Cross-National Data on Sub-National Violence

	Tools to download and merge data files on sub-national conflict, violence and protests from <http://www.x-sub.org>.
	"""
	
	homepage = "https://github.com/zhukovyuri/xSub"
	cran = "xSub" 

	version("3.0.2", md5="942686f511cd8626c11e798fd43ebf52")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
