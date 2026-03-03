# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManifestor(RPackage):
	"""Access and Process Data and Documents of the Manifesto Project

	Provides access to coded election programmes from the Manifesto
    Corpus and to the Manifesto Project's Main Dataset and routines to analyse this
    data. The Manifesto Project <https://manifesto-project.wzb.eu> collects and
    analyses election programmes across time and space to measure the political
    preferences of parties. The Manifesto Corpus contains the collected and
    annotated election programmes in the Corpus format of the package 'tm' to enable
    easy use of text processing and text mining functionality. Specific functions
    for scaling of coded political texts are included.
	"""
	
	homepage = "https://github.com/ManifestoProject/manifestoR"
	cran = "manifestoR" 

	version("1.5.0", md5="3db9a84019bf15d937463c81484b39eb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-nlp@0.1.3:", type=("build", "run"))
	depends_on("r-tm@0.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.12:", type=("build", "run"))
	depends_on("r-functional@0.6:", type=("build", "run"))
	depends_on("r-zoo@1.7.11:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-htmlwidgets@0.6:", type=("build", "run"))
	depends_on("r-dt@0.2:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-readr@1.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.5:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
