# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRblt(RPackage):
	"""Bio-Logging Toolbox

	An R-shiny application to visualize bio-loggers time series at a microsecond precision as Acceleration, Temperature, Pressure, Light intensity. It is possible to link behavioral labels extracted
  from 'BORIS' software <http://www.boris.unito.it> or manually written in a csv file.
	"""
	
	homepage = "https://github.com/sg4r/rblt"
	cran = "rblt" 

	version("0.2.4.7", md5="3ded2e09fdb0cee5eb63cc13c369d134")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-hdf5r@1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("hdf5@1.8.12:", type=("build", "link", "run"))
