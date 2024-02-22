# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactsetProtobufStachextensions(RPackage):
	"""'FactSet' 'STACH' Extensions Package

	Allow clients to convert 'FactSet' 'STACH' formatted data to simpler 
    tabular formats in the form of data frames. This package also provides helper
    methods to extract the meta data from 'FactSet' 'STACH' formatted
    data. See documentation on the 'GitHub' repository for more information.
	"""
	
	homepage = "https://github.com/factset/stach-extensions"
	cran = "factset.protobuf.stachextensions" 

	version("1.0.4", md5="07a54b01fdeb240404a5cf1196c68c2f")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("protobuf", type=("build", "link", "run"))
