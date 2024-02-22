# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeastcostpath(RPackage):
	"""Modelling Pathways and Movement Potential Within a Landscape

	Calculates cost surfaces based on slope to be used when modelling pathways and movement potential within a landscape (Lewis, 2021) <doi:10.1007/s10816-021-09522-w>.
	"""
	
	homepage = "Available"
	cran = "leastcostpath" 

	version("2.0.12", md5="814afb6216b3dae3a6607103ba62b979")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-terra@1.5.34:", type=("build", "run"))
	depends_on("r-sf@1.0.8:", type=("build", "run"))
	depends_on("r-igraph@1.3:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-gstat@2.0.9:", type=("build", "run"))
	depends_on("r-matrix@1.4.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
