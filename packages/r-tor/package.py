# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTor(RPackage):
	"""Import Multiple Files From a Single Directory at Once

	The goal of tor (to-R) is to help you to import
    multiple files from a single directory at once, and to do so as
    quickly, flexibly, and simply as possible.
	"""
	
	homepage = "https://github.com/maurolepore/tor"
	cran = "tor" 

	version("1.1.2", md5="89f93459b0edf6e4318df5ad19d501e7")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
