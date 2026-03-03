# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpdir(RPackage):
	"""Boxplots for Directional Data

	Functions for drawing boxplots for data on (the boundary of) a unit circle (i.e., circular and axial data), from Buttarazzi D., Pandolfo G., Porzio G.C. (2018) <doi:10.1111/biom.12889>.
	"""
	
	cran = "bpDir" 

	version("0.1.2", md5="80eb2e72b2c41f72ed2cf7c9eeaeec0e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
