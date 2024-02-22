# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadsdr(RPackage):
	"""Translate Models from System Dynamics Software into 'R'

	The goal of 'readsdr' is to bridge the design capabilities from
    specialised System Dynamics software with the powerful numerical tools 
    offered by 'R' libraries. The package accomplishes this goal by parsing 
    'XMILE' files ('Vensim' and 'Stella') models into 'R' objects to construct 
    networks (graph theory); 'ODE' functions for 'Stan'; and inputs to simulate
    via 'deSolve' as described in Duggan (2016) <doi:10.1007/978-3-319-34043-2>.
	"""
	
	cran = "readsdr" 

	version("0.2.0", md5="fb98118fd5b76bf790975b25692779c6")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
