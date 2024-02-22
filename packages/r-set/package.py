# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSet(RPackage):
	"""Set Operation

	More easy to get intersection, union or complementary set and 
    combinations.
	"""
	
	homepage = "https://github.com/yikeshu0611/set"
	cran = "set" 

	version("1.2", md5="b879f377719bf455e1eb1d6fa9999d8d")

	depends_on("r-do", type=("build", "run"))
