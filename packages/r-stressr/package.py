# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStressr(RPackage):
	"""Fetch and plot financial stress index and component data

	Forms queries to submit to the Cleveland Federal Reserve Bank web
    site's financial stress index data site.  Provides query functions for both
    the composite stress index and the components data. By default the download
    includes daily time series data starting September 25, 1991.  The functions
    return a class of either type easing or cfsi which contain a list of items
    related to the query and its graphical presentation.  The list includes the
    time series data as an xts object.  The package provides four lattice time
    series plots to render the time series data in a manner similar to the
    bank's own presentation.
	"""
	
	homepage = "https://github.com/mrbcuda/stressr"
	cran = "stressr" 

	version("1.0.0", md5="84b69402539c2a6c7750a4614d2d96c2")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
