# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProjects(RPackage):
	"""A Project Infrastructure for Researchers

	Provides a project infrastructure with a focus on
    manuscript creation. Creates a project folder with a single command,
    containing subdirectories for specific components, templates for
    manuscripts, and so on.
	"""
	
	homepage = "https://cran.r-project.org/package=projects"
	cran = "projects" 

	version("2.1.3", md5="61050074adca89ce626bbcc5f8532f14")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-fs@1.4.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.8:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-rstudioapi@0.11:", type=("build", "run"))
	depends_on("r-sessioninfo@1.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-vctrs@0.2.4:", type=("build", "run"))
	depends_on("r-zip@2.0.4:", type=("build", "run"))
