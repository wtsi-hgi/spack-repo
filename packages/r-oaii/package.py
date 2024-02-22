# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROaii(RPackage):
	"""'OpenAI' API R Interface

	A comprehensive set of helpers that streamline data transmission
  and processing, making it effortless to interact with the 'OpenAI' API.
	"""
	
	homepage = "https://github.com/cezarykuran/oaii"
	cran = "oaii" 

	version("0.4.0", md5="73b0760bd59043f0bb2bbe516b138779")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
