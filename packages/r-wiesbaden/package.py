# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWiesbaden(RPackage):
	"""Access Databases from the Federal Statistical Office of Germany

	Retrieve and import data from different databases of the Federal Statistical Office of Germany (DESTATIS) using their SOAP XML web service <https://www-genesis.destatis.de/>.
	"""
	
	homepage = "https://github.com/sumtxt/wiesbaden/"
	cran = "wiesbaden" 

	version("1.2.9", md5="10c68dfaf6e6a50f649736930cbb5c9c")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-xml2@1:", type=("build", "run"))
	depends_on("r-stringr@1.1:", type=("build", "run"))
	depends_on("r-stringi@1.4:", type=("build", "run"))
	depends_on("r-readr@1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-keyring@1.1:", type=("build", "run"))
