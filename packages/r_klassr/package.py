# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKlassr(RPackage):
	"""Classifications and Codelists for Statistics Norway

	Functions to search, retrieve and apply classifications 
  and codelists using Statistics Norway's API <https://www.ssb.no/klass> 
  from the system 'KLASS'. Retrieves classifications by date with options 
  to choose language, hierarchical level and formatting.
	"""
	
	homepage = "https://statisticsnorway.github.io/klassR/"
	cran = "klassR" 

	version("0.2.3", md5="6b2b3da3bb162a488c23072a43189c71")

	depends_on("r-tm", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
