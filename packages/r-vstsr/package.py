# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVstsr(RPackage):
	"""Access to 'Azure DevOps' API via R

	Implementation of 'Azure DevOps' <https://azure.microsoft.com/> API calls. 
    It enables the extraction of information about repositories, build and release definitions and individual releases. 
    It also helps create repositories and work items within a project without logging into 'Azure DevOps'. 
    There is the ability to use any API service with a shell for any non-predefined call.
	"""
	
	homepage = "https://github.com/ashbaldry/vstsr"
	cran = "vstsr" 

	version("1.1.0", md5="eddab03553a7a91a1d9b5ec70efd1511")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
