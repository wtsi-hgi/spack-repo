# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlstropalr(RPackage):
	"""Support Compatibility Between 'Maelstrom' R Packages and 'Opal'
Environment

	Functions to support compatibility between 'Maelstrom' R packages 
     and 'Opal' environment. 'Opal' is the 'OBiBa' core database application for 
     biobanks. It is used to build data repositories that integrates data 
     collected from multiple sources. 'Opal Maelstrom' is a specific 
     implementation of this software. This 'Opal' client is specifically 
     designed to interact with 'Opal Maelstrom' distributions to perform 
     operations on the R server side. The user must have adequate credentials.
     Please see <https://opaldoc.obiba.org/> for complete documentation.
	"""
	
	homepage = "https://github.com/maelstrom-research/mlstrOpalr"
	cran = "mlstrOpalr" 

	version("1.0.2", md5="4062b55e2562da9da70aebbe7a9e9196")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-opalr", type=("build", "run"))
	depends_on("r-fabr@2:", type=("build", "run"))
	depends_on("r-madshapr@1.0.2:", type=("build", "run"))
