# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeytoenglish(RPackage):
	"""Convert Data to Memorable Phrases

	Convert keys and other values to memorable phrases. 
  Includes some methods to build lists of words.
	"""
	
	homepage = "https://github.com/mcandocia/keyToEnglish"
	cran = "keyToEnglish" 

	version("0.2.1", md5="53b516aaf5157290a1dd87423f9c26fc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
