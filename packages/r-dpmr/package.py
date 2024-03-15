# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDpmr(RPackage):
	"""Data Package Manager for R

	Create, install, and summarise data packages that follow
    the Open Knowledge Foundation's Data Package Protocol.
	"""
	
	homepage = "http://cran.r-project.org/package=dpmr"
	cran = "dpmr" 

	version("0.1.9", md5="f8f762fb70d1618f3f79e2a41acbb4f2")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
