# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactsetProtobufStachV2(RPackage):
	"""'FactSet' 'STACH V2' Library

	Generates 'RProtobuf' classes for 'FactSet' 'STACH V2' tabular 
    format which represents complex multi-dimensional array of data. These 
    classes help in the 'serialization' and 'deserialization' of 'STACH V2' 
    formatted data. See 'GitHub' repository documentation for more 
    information.
	"""
	
	homepage = "https://github.com/factset/stachschema-sdks"
	cran = "factset.protobuf.stach.v2" 

	version("1.0.6", md5="a847efaeff6d55d24a97ff13f45cec4e", url="https://cran.r-project.org/src/contrib/factset.protobuf.stach.v2_1.0.6.tar.gz")

	depends_on("r-rprotobuf", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("protobuf", type=("build", "link", "run"))
