# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGitlink(RPackage):
	"""Add 'Git' Links to Your Web Based Assets

	Provides helpers to add 'Git' links to 'shiny'
    applications, 'rmarkdown' documents, and other 'HTML' based resources.
    This is most commonly used for 'GitHub' ribbons.
	"""
	
	homepage = "https://github.com/colearendt/gitlink"
	cran = "gitlink" 

	version("0.1.3", md5="34c93d5fe4f3d80f33308438316bdfbb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
