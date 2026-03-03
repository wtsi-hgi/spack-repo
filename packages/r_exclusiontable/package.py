# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExclusiontable(RPackage):
	"""Creating Tables of Excluded Observations

	Instead of counting observations before and after a subset() 
    call, the ExclusionTable() function reports the number before and after 
    each subset() call together with the number of observations that have been 
    excluded. This is especially useful in observational studies for keeping 
    track how many observations have been excluded for each in-/ or 
    exclusion criteria. You just need to provide ExclusionTable() with a 
    dataset and a list of logical filter statements.
	"""
	
	homepage = "https://github.com/entjos/ExclusionTable/"
	cran = "ExclusionTable" 

	version("1.1.0", md5="1b2ea03e92e599a6cf90570892300400")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
