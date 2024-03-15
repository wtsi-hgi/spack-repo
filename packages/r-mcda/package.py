# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcda(RPackage):
	"""Support for the Multicriteria Decision Aiding Process

	Support for the analyst in a Multicriteria Decision Aiding (MCDA) process with algorithms, 
    preference elicitation and data visualisation functions. Sébastien Bigaret, Richard Hodgett, Patrick Meyer, 
    Tatyana Mironova, Alexandru Olteanu (2017) Supporting the multi-criteria decision aiding process : 
    R and the MCDA package, Euro Journal On Decision Processes, Volume 5, Issue 1 - 4, 
    pages 169 - 194 <doi:10.1007/s40070-017-0064-1>.
	"""
	
	homepage = "https://github.com/paterijk/MCDA"
	cran = "MCDA" 

	version("0.1.0", md5="d7178c013c42f3c8fb253e0112604b87")

	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-glpkapi", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-triangle", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
