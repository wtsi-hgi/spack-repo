# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyllogi(RPackage):
	"""Collection of Data Sets for Teaching Purposes

	Collection (syllogi in greek) of real and fictitious data sets for teaching purposes.
	     The datasets were manually entered by the author from the respective references as listed in the individual dataset documentation.
	     The fictions datasets are the creation of the author, that he has found useful for teaching statistics. 
	"""
	
	cran = "syllogi" 

	version("1.0.2", md5="4e954b8ef00711122c488bd10570aaad")

	depends_on("r@3.6:", type=("build", "run"))
