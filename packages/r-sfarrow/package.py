# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfarrow(RPackage):
	"""Read/Write Simple Feature Objects ('sf') with 'Apache' 'Arrow'

	Support for reading/writing simple feature ('sf') spatial objects from/to 'Parquet' files. 'Parquet' files are an open-source, column-oriented data storage format from Apache (<https://parquet.apache.org/>), now popular across programming languages. This implementation converts simple feature list geometries into well-known binary format for use by 'arrow', and coordinate reference system information is maintained in a standard metadata format.
	"""
	
	homepage = "https://github.com/wcjochem/sfarrow"
	cran = "sfarrow" 

	version("0.4.1", md5="a2e14236864928f98ae8c27590b7c3be")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
