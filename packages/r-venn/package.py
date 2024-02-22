# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVenn(RPackage):
	"""Draw Venn Diagrams

	A close to zero dependency package to draw and display Venn 
    diagrams up to 7 sets, and any Boolean union of set intersections.
	"""
	
	homepage = "https://github.com/dusadrian/venn"
	cran = "venn" 

	version("1.12", md5="29b0e3dd951c8626b126705d88f8303a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-admisc@0.33:", type=("build", "run"))
