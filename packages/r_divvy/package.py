# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDivvy(RPackage):
	"""Spatial Subsampling of Biodiversity Occurrence Data

	Divide taxonomic occurrence data into geographic regions of fair
    comparison, with three customisable methods to standardise area and extent.
    Calculate common biodiversity and range-size metrics on subsampled data.
    Background theory and practical considerations for the methods are described
    in Antell and others (2023) <doi:10.31223/X5997Z>.
	"""
	
	homepage = "https://gawainantell.github.io/divvy/"
	cran = "divvy" 

	version("1.0.0", md5="6adef846cdf7d0cc13d113343b9cd3b3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-inext@3:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
