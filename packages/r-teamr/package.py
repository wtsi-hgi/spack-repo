# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTeamr(RPackage):
	"""Send Formatted Messages, Images and Objects to Microsoft 'Teams'

	Package of wrapper functions using R6 class to send requests to 
  Microsoft 'Teams' <https://products.office.com/en-us/microsoft-teams/group-chat-software> through webhooks.
  When you need to share information or data from R to 'Teams', rather than copying/pasting, you
  can use this package to send well-formatted output from multiple R objects.
	"""
	
	homepage = "https://github.com/wwwjk366/teamr"
	cran = "teamr" 

	version("0.0.1", md5="051ba3987ee0b5bf93ee79bd1191ec4d")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
