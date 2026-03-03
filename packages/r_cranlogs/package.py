# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCranlogs(RPackage):
	"""Download Logs from the 'RStudio' 'CRAN' Mirror

	'API' to the database of 'CRAN' package downloads from the
    'RStudio' 'CRAN mirror'. The database itself is at <http://cranlogs.r-pkg.org>,
    see <https://github.com/r-hub/cranlogs.app> for the raw 'API'.
	"""
	
	homepage = "https://github.com/r-hub/cranlogs"
	cran = "cranlogs" 

	version("2.1.1", md5="a8ce990b5a78265ad8b905e2be8ee98a")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
