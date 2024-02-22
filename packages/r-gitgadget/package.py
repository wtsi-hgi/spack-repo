# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGitgadget(RPackage):
	"""'Rstudio' Addin for Version Control and Assignment Management
using Git

	An 'Rstudio' addin for version control that allows users to clone
    repositories, create and delete branches, and sync forks on GitHub, GitLab, etc.
    Furthermore, the addin uses the GitLab API to allow instructors to create
    forks and merge requests for all students/teams with one click of a button.
	"""
	
	homepage = "URL:"
	cran = "gitgadget" 

	version("0.8.1", md5="61f6e6ff3c43e28fe99e63e0e07d4076")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-miniui@0.1.1.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
	depends_on("r-curl@3.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-shinyfiles@0.7.5:", type=("build", "run"))
	depends_on("r-callr@2.0.4:", type=("build", "run"))
	depends_on("r-usethis@1.5.1:", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
