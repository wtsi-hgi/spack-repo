# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataone(RPackage):
	"""R Interface to the DataONE REST API

	Provides read and write access to data and metadata from
    the DataONE network <https://www.dataone.org> of data repositories.  
    Each DataONE repository implements a consistent repository application 
    programming interface. Users call methods in R to access these remote 
    repository functions, such as methods to query the metadata catalog, get 
    access to metadata for particular data packages, and read the data objects 
    from the data repository. Users can also insert and update data objects on 
    repositories that support these methods.
	"""
	
	homepage = "https://github.com/DataONEorg/rdataone"
	cran = "dataone" 

	version("2.2.2", md5="8eb47f237de350522598cbeaabac883b")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-xml@3.95.0.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-datapack@1.4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
