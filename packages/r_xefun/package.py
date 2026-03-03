# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXefun(RPackage):
	"""X-Engineering or Supporting Functions

	Miscellaneous functions used for x-engineering (feature engineering) or 
  for supporting in other packages maintained by 'Shichen Xie'.
	"""
	
	homepage = "https://github.com/ShichenXie/xefun"
	cran = "xefun" 

	version("0.1.5", md5="d0302909c19666784cb616bb35cf130e")

	depends_on("r-data-table", type=("build", "run"))
