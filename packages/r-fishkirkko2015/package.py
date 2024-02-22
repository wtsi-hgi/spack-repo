# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFishkirkko2015(RPackage):
	"""Dataset of Measurements of Fish Species at Kirkkojarvi Lake,
Finland

	Dataset of 302 measurements of 11 fish species to accompany the
    manuscript "Length-weight relationships of six freshwater fish species
    from lake Kirkkojarvi, Finland".
	"""
	
	cran = "fishkirkko2015" 

	version("1.0.0", md5="e291da089d6452be6297d16fd2e4f8e3", url="https://cran.r-project.org/src/contrib/fishkirkko2015_1.0.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
