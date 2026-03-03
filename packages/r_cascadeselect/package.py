# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCascadeselect(RPackage):
	"""A Cascade Select Input for 'Shiny'

	Provides a cascade select widget for usage in 'Shiny'
    applications. This is useful for selection of hierarchical choices
    (e.g. continent, country, city). It is taken from the 'JavaScript'
    library 'PrimeReact'.
	"""
	
	homepage = "https://github.com/stla/cascadeSelect"
	cran = "cascadeSelect" 

	version("1.1.0", md5="e339c9701ae07d9955b7a8b3cf0fe17c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fontawesome", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
