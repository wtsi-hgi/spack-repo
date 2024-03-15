# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlfr(RPackage):
	"""Connectivity to 'Alfresco' Content Management Repositories

	Allows you to connect to an 'Alfresco' content management repository and interact
  with its contents using simple and intuitive functions.  You will be able to establish a connection session to the 'Alfresco' repository,
  read and upload content and manage folder hierarchies.  For more details on the 'Alfresco' content management repository
  see <https://www.alfresco.com/ecm-software/document-management>.
	"""
	
	homepage = "https://github.com/rwetherall/alfr"
	cran = "alfr"

	version("1.2.1", md5="1bb5dd329519d4f4d4c391248740d8f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
