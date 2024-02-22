# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosaic(RPackage):
	"""Project MOSAIC Statistics and Mathematics Teaching Utilities

	Data sets and utilities from Project MOSAIC (<http://www.mosaic-web.org>) used
    to teach mathematics, statistics, computation and modeling.  Funded by the
    NSF, Project MOSAIC is a community of educators working to tie together
    aspects of quantitative work that students in science, technology,
    engineering and mathematics will need in their professional lives, but
    which are usually taught in isolation, if at all.
	"""
	
	homepage = "https://github.com/ProjectMOSAIC/mosaic"
	cran = "mosaic" 

	version("1.9.0", md5="8fcedc48def8bb5f9688d4a9d84bd5b8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lattice@0.20.21:", type=("build", "run"))
	depends_on("r-ggformula", type=("build", "run"))
	depends_on("r-mosaicdata", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mosaiccore@0.7:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
