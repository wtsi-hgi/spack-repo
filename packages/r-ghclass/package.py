# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGhclass(RPackage):
	"""Tools for Managing Classes on GitHub

	Interface for the GitHub API that enables efficient 
    management of courses on GitHub. It has a functionality for 
    managing organizations, teams, repositories, and users on GitHub 
    and helps automate most of the tedious and repetitive tasks 
    around creating and distributing assignments.
	"""
	
	homepage = "https://github.com/rundel/ghclass"
	cran = "ghclass" 

	version("0.2.1", md5="4defed56e2637ebbc9467659439f7d89")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
