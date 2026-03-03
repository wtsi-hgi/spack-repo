# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMojson(RPackage):
	"""A Serialization-Style Flattening and Description for JSON

	Support JSON flattening in a long data frame way, where the nesting keys will be stored in the absolute path. It also
   provides an easy way to summarize the basic description of a JSON list. The idea of 'mojson' is to transform a JSON object in an 
   absolute serialization way, which means the early key-value pairs will appear in the heading rows of the resultant data frame. 
   'mojson' also provides an alternative way of comparing two different JSON lists, returning the left/inner/right-join style results.
	"""
	
	homepage = "https://github.com/chriswweibo/mojson"
	cran = "mojson" 

	version("0.1", md5="85321e9a92fcd95d479f4d636cdc813e")

	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-comparedf", type=("build", "run"))
