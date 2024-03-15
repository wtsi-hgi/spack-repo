# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnassisjavalibs(RPackage):
	"""OnassisJavaLibs, java libraries to run conceptmapper and semantic similarity

	A package that contains java libraries to call conceptmapper and compute semnatic similarity from R
	"""
	
	bioc = "OnassisJavaLibs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/OnassisJavaLibs_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/OnassisJavaLibs/OnassisJavaLibs_1.24.0.tar.gz"]

	version("1.24.0", md5="88d86bc7e7d339146ba7ea689c2d8080")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))

	# experiment