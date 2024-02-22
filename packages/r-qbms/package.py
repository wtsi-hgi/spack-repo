# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQbms(RPackage):
	"""Query the Breeding Management System(s)

	Linking data management systems to analytics is an important step in breeding 
    digitization. Breeders can use this R package to Query the Breeding Management 
    System(s) like 'BMS' <https://bmspro.io>, 'BreedBase' <https://breedbase.org>, and 
    'GIGWA' <https://southgreen.fr/content/gigwa> (using 'BrAPI' <https://brapi.org> calls) 
    and help them to retrieve phenotypic and genotypic data directly into their analyzing 
    pipelines.
	"""
	
	homepage = "https://icarda-git.github.io/QBMS/"
	cran = "QBMS" 

	version("0.9.1", md5="28ad24c9d9bd4dbd1835e6a3670e3afa")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rnetcdf", type=("build", "run"))
