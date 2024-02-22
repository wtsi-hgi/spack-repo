# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPetrinetr(RPackage):
	"""Building, Visualizing, Exporting and Replaying Petri Nets

	Functions for the construction of Petri Nets. Petri Nets can be replayed by firing enabled transitions.
     Silent transitions will be hidden by the execution handler. Also includes functionalities for the visualization of Petri Nets and
     export of Petri Nets to PNML (Petri Net Markup Language) files.
	"""
	
	homepage = "https://bupar.net"
	cran = "petrinetR" 

	version("0.3.0", md5="66558a32ff1627a663bd8adabff2dad3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
