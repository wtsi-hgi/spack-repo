# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynetnlaresistance(RPackage):
	"""Resisting Neighbor Label Attack in a Dynamic Network

	An anonymization algorithm to resist neighbor label attack in a dynamic network.
	"""
	
	cran = "dynetNLAResistance" 

	version("0.1.0", md5="c3cb1da8e2d21eb9ef7178f4f047f793")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
