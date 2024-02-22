# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMadrat(RPackage):
	"""May All Data be Reproducible and Transparent (MADRaT) *

	Provides a framework which should improve reproducibility and
    transparency in data processing. It provides functionality such as
    automatic meta data creation and management, rudimentary quality
    management, data caching, work-flow management and data aggregation.
    * The title is a wish not a promise. By no means we expect this
    package to deliver everything what is needed to achieve full
    reproducibility and transparency, but we believe that it supports
    efforts in this direction.
	"""
	
	homepage = "https://github.com/pik-piam/madrat"
	cran = "madrat" 

	version("3.6.4", md5="24d6969bb889fe6e2b2de70af991b7ab")

	depends_on("r-magclass@5.7:", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pkgload", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
