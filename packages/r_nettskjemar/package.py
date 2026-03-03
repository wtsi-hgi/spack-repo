# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNettskjemar(RPackage):
	"""Connect to the 'nettskjema.no' API of the University of Oslo

	Enables users to retrieve data, meta-data, and codebooks 
    from <https://nettskjema.no/>. The data from the API is richer than from the
    online data portal. Mowinckel (2021) <doi:10.5281/zenodo.4745481>.
	"""
	
	homepage = "https://github.com/LCBC-UiO/nettskjemar"
	cran = "nettskjemar" 

	version("0.1.4", md5="3fc2cf0fd620206bc15c94709675ebf4")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
