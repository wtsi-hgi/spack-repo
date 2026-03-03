# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyEmptystate(RPackage):
	"""Empty State Components for 'Shiny'

	
    Offers a comprehensive solution for managing 'empty states' in 'Shiny' applications.
    It provides tools to create both default and customizable components for scenarios where
    data is absent or doesn't match user-defined filters. The package prioritizes user experience,
    ensuring clarity and consistency even when data is not available to display.
	"""
	
	homepage = "https://appsilon.github.io/shiny.emptystate/"
	cran = "shiny.emptystate" 

	version("0.1.0", md5="3845c387dad44750c144bdc077ce479a")

	depends_on("r-fontawesome", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
