# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnordt(RPackage):
	"""Add-on to CellNOptR: Discretized time treatments

	This add-on to the package CellNOptR handles time-course data, as opposed to steady state data in CellNOptR. It scales the simulation step to allow comparison and model fitting for time-course data. Future versions will optimize delays and strengths for each edge.
	"""
	
	bioc = "CNORdt" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CNORdt_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CNORdt/CNORdt_1.44.0.tar.gz"]

	version("1.44.0", md5="74b0c2783638f7d5ce872577eb305ad3")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-cellnoptr@0.99:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
