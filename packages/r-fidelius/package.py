# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFidelius(RPackage):
	"""Browser-Side Password-Protected HTML Documents

	Create secure, encrypted, and password-protected static HTML 
  documents that include the machinery for secure in-browser authentication 
  and decryption.
	"""
	
	homepage = "https://mattwarkentin.github.io/fidelius/"
	cran = "fidelius" 

	version("0.0.2", md5="f16fe15673171d6099429fdc13e55fb5")

	depends_on("r-askpass", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-sodium", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
