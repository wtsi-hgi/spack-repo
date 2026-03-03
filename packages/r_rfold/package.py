# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfold(RPackage):
	"""Working with many R Folders Within an R Package

	
    Allows developers to work with many R folders inside a package. It offers functionalities to transfer R scripts (saved outside the R folder) into 
    the R folder while making additional checks.
	"""
	
	homepage = "https://github.com/feddelegrand7/rfold"
	cran = "rfold" 

	version("0.2.0", md5="268c6ff61f6bf4c7658f62fe5396645d")

	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-fs@1.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-here@1.0.1:", type=("build", "run"))
	depends_on("r-usethis@2.0.1:", type=("build", "run"))
