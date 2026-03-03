# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuardianapi(RPackage):
	"""Access 'The Guardian' Newspaper Open Data API

	Access to 'The Guardian' newspaper's open API
  <https://open-platform.theguardian.com/>, containing all articles published 
  in 'The Guardian' from 1999 to the present, including article text, metadata,
  tags and contributor information. An API key and registration is required.
	"""
	
	homepage = "https://docs.evanodell.com/guardianapi"
	cran = "guardianapi" 

	version("0.1.1", md5="fa763b332abbef642bcefe329ef81ac3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
