# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RC2z(RPackage):
	"""A Reference Manager

	'Cristin' to 'Zotero' ('c2z') aims at obtaining total
    dominion over 'Cristin' ('Current Research Information SysTem in
    Norway') and 'Zotero'. The package enables manipulating 'Zotero'
    libraries using 'R'.  Import references from 'Cristin', 'Regjeringen',
    'CRAN', 'ISBN' ('Alma', 'LoC'), and 'DOI' ('CrossRef', 'DataCite') to
    a 'Zotero' library. Add, edit, copy, or delete items, including
    attachments and collections, and export references to 'BibLaTeX' (and
    other formats).
	"""
	
	homepage = "https://github.com/oeysan/c2z/"
	cran = "c2z" 

	version("0.2.0", md5="fd28a6b2cfaefd4919b96d5d34a1820f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
