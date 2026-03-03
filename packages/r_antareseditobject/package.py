# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAntareseditobject(RPackage):
	"""Edit an 'Antares' Simulation

	Edit an 'Antares' simulation before running it : create new areas, links, thermal
    clusters or binding constraints or edit existing ones. Update 'Antares' general & optimization settings.
    'Antares' is an open source power system generator, more information available here : <https://antares-simulator.org/>.
	"""
	
	homepage = "https://github.com/rte-antares-rpackage/antaresEditObject"
	cran = "antaresEditObject" 

	version("0.6.1", md5="03ebc94f895dc9e2521acc5ecea33ddf")

	depends_on("r-antaresread@2.4.2:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-memuse", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
