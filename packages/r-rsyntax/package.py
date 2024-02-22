# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsyntax(RPackage):
	"""Extract Semantic Relations from Text by Querying and Reshaping
Syntax

	Various functions for querying and reshaping dependency trees, 
    as for instance created with the 'spacyr' or 'udpipe' packages.
    This enables the automatic extraction of useful semantic relations from texts,
    such as quotes (who said what) and clauses (who did what). Method proposed in 
    Van Atteveldt et al. (2017) <doi:10.1017/pan.2016.12>.
	"""
	
	cran = "rsyntax" 

	version("0.1.4", md5="9fc46fba1fca43d4a8405a0caf827833")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tokenbrowser", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
