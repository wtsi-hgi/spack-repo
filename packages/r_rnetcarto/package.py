# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnetcarto(RPackage):
	"""Fast Network Modularity and Roles Computation by Simulated
Annealing (Rgraph C Library Wrapper for R)

	Provides functions to compute the modularity and modularity-related roles in networks. It is a wrapper around the rgraph library (Guimera & Amaral, 2005, <doi:10.1038/nature03288>).
	"""
	
	cran = "rnetcarto" 

	version("0.2.6", md5="614874f21fd3faf0024dafd4bd0c75bf")

	depends_on("gsl", type=("build", "link", "run"))
