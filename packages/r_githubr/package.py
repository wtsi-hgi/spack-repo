# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGithubr(RPackage):
	"""Easier to Use API Wrapper for 'GitHub'

	This is a 'GitHub' API wrapper for R. <https://docs.github.com/en/rest> It uses the 'gh' package but has things wrapped up for convenient use cases.
	"""
	
	homepage = "https://github.com/fhdsl/githubr"
	cran = "githubr" 

	version("0.9.1", md5="e2b742cbff1cdc151e756accb58cbf5b")

	depends_on("r-gitcreds", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
