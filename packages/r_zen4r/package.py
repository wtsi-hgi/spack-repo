# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZen4r(RPackage):
	"""Interface to 'Zenodo' REST API

	Provides an Interface to 'Zenodo' (<https://zenodo.org>) REST API, 
  including management of depositions, attribution of DOIs by 'Zenodo' and 
  upload and download of files.
	"""
	
	homepage = "https://github.com/eblondel/zen4R"
	cran = "zen4R" 

	version("0.9", md5="83c459e52894798d761a4e08529bb70c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-atom4r", type=("build", "run"))
	depends_on("r-utf8", type=("build", "run"))
