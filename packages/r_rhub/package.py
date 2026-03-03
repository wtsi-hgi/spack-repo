# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhub(RPackage):
	"""Connect to 'R-hub'

	Run 'R CMD check' on any of the 'R-hub' (<https://builder.r-hub.io/>)
    architectures, from the command line. The current architectures include
    'Windows', 'macOS', 'Solaris' and various 'Linux' distributions.
	"""
	
	homepage = "https://github.com/r-hub/rhub"
	cran = "rhub" 

	version("1.1.2", md5="43d51e0e885cbdb0d71ad25dfe139844")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-cli@1.1:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rcmdcheck@1.2.1:", type=("build", "run"))
	depends_on("r-rematch", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-whoami", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
