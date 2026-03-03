# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFoolbox(RPackage):
	"""Function Manipulation Toolbox

	Provides functionality for manipulating functions and translating them
    in metaprogramming.
	"""
	
	homepage = "https://github.com/mailund/foolbox"
	cran = "foolbox" 

	version("0.1.1", md5="5b220284bfdaba6702e5e502a53c01ad")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
