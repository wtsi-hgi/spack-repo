# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeeclickfixr(RPackage):
	"""Access Data from the SeeClickFix Web API

	Provides a wrapper to access data from the SeeClickFix
  web API for R. SeeClickFix is a central platform employed by many cities
  that allows citizens to request their city's services. This package
  creates several functions to work with all the built-in calls to the
  SeeClickFix API. Allows users to download service request data from
  numerous locations in easy-to-use dataframe format manipulable in
  standard R functions.
	"""
	
	cran = "seeclickfixr" 

	version("1.1.0", md5="df56ba9580e0561d725ff88da5373c8a")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
