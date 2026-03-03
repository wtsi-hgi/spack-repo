# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepresentr(RPackage):
	"""Create Representative Records After Entity Resolution

	An implementation of Kaplan, Betancourt, Steorts (2022) <doi:10.1080/00031305.2022.2041482> that creates representative records for use in downstream tasks after entity resolution is performed. Multiple methods for creating the representative records (data sets) are provided. 
	"""
	
	cran = "representr" 

	version("0.1.5", md5="20ed172e1e669b9f9af739bbb93fb0e6")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
