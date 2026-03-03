# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdibble(RPackage):
	"""Encapsulating Elements of Experimental Design

	A system to facilitate designing comparative experiments using the 
  grammar of experimental designs <https://emitanaka.org/edibble-book/>. 
  An experimental design is treated as an intermediate, mutable object that is 
  built progressively by fundamental experimental components like units, treatments, and their relation.
  The system aids in experimental planning, management and workflow.
	"""
	
	homepage = "https://edibble.emitanaka.org/"
	cran = "edibble" 

	version("1.1.0", md5="202951844bdf52d0402afd48d8e1c8da")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-nestr", type=("build", "run"))
	depends_on("r-algdesign", type=("build", "run"))
	depends_on("r-dae", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
