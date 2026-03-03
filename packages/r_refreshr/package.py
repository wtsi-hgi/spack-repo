# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefreshr(RPackage):
	"""Work with Refreshable Datasets that Update their Data
Automatically

	Connects dataframes/tables with a remote data source. Raw data downloaded
  from the data source can be further processed and transformed using data preparation 
  code that is also baked into the dataframe/table. Refreshable dataframes can 
  be shared easily (e.g. as R data files). Their users do not need to care about
  the inner workings of the data update mechanisms.
	"""
	
	homepage = "https://github.com/jsugarelli/refreshr/"
	cran = "refreshr" 

	version("0.1.0", md5="c20e52a10fb8e2f19a324510281f8531")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
