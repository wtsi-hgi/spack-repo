# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLazysf(RPackage):
	"""Delayed Read for 'GDAL' Vector Data Sources

	Lazy read for drawings. A 'dplyr' back end for data sources supported by 
    'GDAL' vector drivers, that allows working with local or remote sources as if they 
    are in-memory data frames. Basic features works with any drawing format ('GDAL vector 
    data source') supported by the 'sf' package. 
	"""
	
	homepage = "https://github.com/mdsumner/lazysf"
	cran = "lazysf" 

	version("0.1.0", md5="68139ee6a21d0d2ac119b6ac0550a284")

	depends_on("r-sf@0.7.0:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
