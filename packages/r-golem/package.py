# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGolem(RPackage):
	"""A Framework for Robust Shiny Applications

	An opinionated framework for building a production-ready
    'Shiny' application. This package contains a series of tools for
    building a robust 'Shiny' application from start to finish.
	"""
	
	homepage = "https://github.com/ThinkR-open/golem"
	cran = "golem" 

	version("0.4.1", md5="759f1070cd4edac4092ad96a4a407a55")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-attempt@0.3:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
