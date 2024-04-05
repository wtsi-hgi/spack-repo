# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHubeau(RPackage):
	"""Get Data from the French National Database on Water 'Hub'Eau'

	Collection of functions to help retrieving data from
    'Hub'Eau' the free and public French National APIs on water
    <https://hubeau.eaufrance.fr/>.
	"""
	
	homepage = "https://inrae.github.io/hubeau/"
	cran = "hubeau" 

	version("0.5.0", md5="67dc4fb306163afbe7aa5bb93fc6f5f2")
	version("0.4.1", md5="84fab7a5d34e356fd062037808f50ae1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
