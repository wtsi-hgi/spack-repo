# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNamedropr(RPackage):
	"""Create Visual Citations for Presentations and Posters

	Provides 'visual citations' containing the metadata of a
    scientific paper and a 'QR' code.  A 'visual citation' is a banner
    containing title, authors, journal and year of a publication.  This
    package can create such banners based on 'BibTeX' and 'BibLaTeX'
    references or call the reference metadata from 'Crossref'-API. The
    banners include a QR code pointing to the 'DOI'.  The resulting HTML
    object or PNG image can be included in a presentation to point the
    audience to good resources for further reading.  Styling is possible
    via predefined designs or via custom 'CSS'.  This package is not
    intended as replacement for proper reference manager packages, but a
    tool to enrich scientific presentation slides and conference posters.
	"""
	
	homepage = "https://github.com/nucleic-acid/namedropR"
	cran = "namedropR" 

	version("2.4.1", md5="40959456a0f91015e3299cc7ee332ce2")

	depends_on("r-bib2df", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-qrcode@0.1.4:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
