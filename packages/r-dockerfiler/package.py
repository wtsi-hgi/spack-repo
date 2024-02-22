# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDockerfiler(RPackage):
	"""Easy Dockerfile Creation from R

	Build a Dockerfile straight from your R session.
    'dockerfiler' allows you to create step by step a Dockerfile, and
    provide convenient tools to wrap R code inside this Dockerfile.
	"""
	
	homepage = "https://github.com/ThinkR-open/dockerfiler"
	cran = "dockerfiler" 

	version("0.2.2", md5="036c7fa0312dc7282d019e6cdd9d1d41")

	depends_on("r-attempt@0.3.1:", type=("build", "run"))
	depends_on("r-cli@2.3:", type=("build", "run"))
	depends_on("r-desc@1.2:", type=("build", "run"))
	depends_on("r-fs@1.5:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-pak@0.2:", type=("build", "run"))
	depends_on("r-pkgbuild@1.2:", type=("build", "run"))
	depends_on("r-r6@2.5:", type=("build", "run"))
	depends_on("r-remotes@2.2:", type=("build", "run"))
	depends_on("r-usethis@2.0.1:", type=("build", "run"))
