# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHalfcircle(RPackage):
	"""Plot Halfcircle Diagram

	There are growing concerns on flow data in diverse fields including trade, migration, knowledge diffusion, disease spread, and transportation. The package is an effective visual support to learn the pattern of flow which is called halfcircle diagram. The flow between two nodes placed on the center line of a circle is represented using a half circle drawn from the origin to the destination in a clockwise direction. Through changing the order of nodes, the halfcircle diagram enables users to examine the complex relationship between bidirectional flow and each potential determinants. Furthermore, the halfmeancenter function, which calculates (un) weighted mean center of half circles, makes the comparison easier.
	"""
	
	cran = "halfcircle" 

	version("0.1.0", md5="8b5cb35ddf19e3a49087370de53769de")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
