# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepurrrsive(RPackage):
	"""Examples of Recursive Lists and Nested or Split Data Frames

	Recursive lists in the form of R objects, 'JSON', and 'XML',
    for use in teaching and examples. Examples include color palettes,
    Game of Thrones characters, 'GitHub' users and repositories, music
    collections, and entities from the Star Wars universe. Data from the
    'gapminder' package is also included, as a simple data frame and in
    nested and split forms.
	"""
	
	homepage = "https://jennybc.github.io/repurrrsive/"
	cran = "repurrrsive" 

	version("1.1.0", md5="927b886b468411847a62694741b97d2d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
