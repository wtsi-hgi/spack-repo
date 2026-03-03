# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsnstat(RPackage):
	"""'La Societe Nouvelle' API Access

	Tools facilitating access to the 'macro_data' service of the
    'La Societe Nouvelle' API. It ensures an easy and fully-disclosed
    access to all macro-level data used in the 'La Societe Nouvelle'
    systems and the related metadata.  Related API can be accessed from
    <https://api.lasocietenouvelle.org/>.
	"""
	
	homepage = "https://github.com/La-Societe-Nouvelle/lsnstat/"
	cran = "lsnstat" 

	version("1.0.0", md5="e9b21b4a6735dfc34170f643e069071e")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
