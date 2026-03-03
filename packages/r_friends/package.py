# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFriends(RPackage):
	"""The Entire Transcript from Friends in Tidy Format

	The complete scripts from the American sitcom Friends in tibble 
    format. Use this package to practice data wrangling, text analysis and 
    network analysis.
	"""
	
	homepage = "https://github.com/EmilHvitfeldt/friends"
	cran = "friends" 

	version("0.1.0", md5="3903cb91b295c761406db210c83fb711")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
