# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUklr(RPackage):
	"""Client to United Kingdom Land Registry

	Access data from Land Registry Open Data
    <http://landregistry.data.gov.uk/> through 'SPARQL' queries. 'uklr'
    supports the house price index, transaction and price paid data.
	"""
	
	homepage = "https://kvasilopoulos.github.io/uklr/"
	cran = "uklr" 

	version("1.0.2", md5="7b00066a573133260b8c0ef2c2a47996")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
