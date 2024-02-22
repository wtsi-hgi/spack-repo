# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraits(RPackage):
	"""Species Trait Data from Around the Web

	Species trait data from many different sources, including
    sequence data from 'NCBI' (<https://www.ncbi.nlm.nih.gov/>),
    plant trait data from 'BETYdb', data from 'EOL' 'Traitbank',
    'Birdlife' International, and more.
	"""
	
	homepage = "https://docs.ropensci.org/traits/"
	cran = "traits" 

	version("0.5.0", md5="a766479518ffdb06b8887617a74f4fad")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.19:", type=("build", "run"))
	depends_on("r-httr@1.1:", type=("build", "run"))
	depends_on("r-crul@0.6:", type=("build", "run"))
	depends_on("r-tibble@1.3.4:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-taxize@0.7.4:", type=("build", "run"))
	depends_on("r-xml2@0.1.2:", type=("build", "run"))
	depends_on("r-rvest@0.3.1:", type=("build", "run"))
	depends_on("r-hoardr", type=("build", "run"))
