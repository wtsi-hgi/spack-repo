# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChristmas(RPackage):
	"""Generation of Different Animated Christmas Cards

	Generation of different Christmas cards, most of them being
    animated. Most of the cards can be generated in three languages (English,
    Catalan and Spanish). The collection started in 2009.
	"""
	
	homepage = "https://sites.google.com/view/josebarrera/"
	cran = "christmas" 

	version("1.3.0", md5="51788e7ca185d512062e75fade4772fe")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-animation@2.6:", type=("build", "run"))
