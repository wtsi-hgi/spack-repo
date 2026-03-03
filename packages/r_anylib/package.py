# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnylib(RPackage):
	"""Install and Load Any Package from CRAN, Bioconductor or Github

	Made to make your life simpler with packages, by
    installing and loading a list of packages, whether they are on CRAN,
    Bioconductor or github. For github, if you do not have the full path, with 
    the maintainer name in it (e.g. "achateigner/topReviGO"), it will be able to
    load it but not to install it.
	"""
	
	cran = "anyLib" 

	version("1.0.5", md5="1a16fd35ec640ccc8b5fa54b9ce64d5e")

	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
