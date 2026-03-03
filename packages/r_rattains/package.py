# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRattains(RPackage):
	"""Access EPA 'ATTAINS' Data

	An R interface to United States Environmental Protection Agency (EPA)  
    Assessment, Total Maximum Daily Load (TMDL) Tracking and Implementation System 
    ('ATTAINS') data. 'ATTAINS' is the EPA database used to track information 
    provided by states about water quality assessments conducted under federal 
    Clean Water Act requirements. ATTAINS information and API information is available at <https://www.epa.gov/waterdata/attains>.
	"""
	
	homepage = "https://github.com/mps9506/rATTAINS"
	cran = "rATTAINS" 

	version("1.0.0", md5="26c3d6a005adb960ae76b2fed9874ec6")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fauxpas", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-tibblify", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
