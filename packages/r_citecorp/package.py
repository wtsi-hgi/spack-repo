# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCitecorp(RPackage):
	"""Client for the Open Citations Corpus

	Client for the Open Citations Corpus (<http://opencitations.net/>).
    Includes a set of functions for getting one identifier type from another,
    as well as getting references and citations for a given identifier.
	"""
	
	homepage = "https://github.com/ropenscilabs/citecorp"
	cran = "citecorp" 

	version("0.3.0", md5="bc92e1e30a71a0ef1de034dca189c33b")

	depends_on("r-crul@0.7:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fauxpas@0.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
