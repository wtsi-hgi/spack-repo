# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetwiki(RPackage):
	"""R Wrapper for Wikipedia Data

	A simple wrapper for 'Wikipedia' data. Specifically, this 
    package looks to fill a gap in retrieving text data in a tidy format that can be used for Natural Language Processing. 
	"""
	
	cran = "getwiki" 

	version("0.9.0", md5="1f6ba1272f6d4e05c21b7be3a90117f4")

	depends_on("r-jsonlite", type=("build", "run"))
