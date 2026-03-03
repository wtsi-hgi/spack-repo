# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrnni(RPackage):
	"""Manipulate with RNNI Tree Space

	Calculate RNNI distance between and manipulate with ranked trees. RNNI stands for Ranked Nearest Neighbour Interchange and is an extension of the classical NNI space (space of trees created by the NNI moves) to ranked trees, where internal nodes are ordered according to their heights (usually assumed to be times). The RNNI distance takes the tree topology into account, as standard NNI does, but also penalizes changes in the order of internal nodes, i.e. changes in the order of times of evolutionary events. For more information about the RNNI space see: Gavryushkin et al. (2018) <doi:10.1007/s00285-017-1167-9>, Collienne & Gavryushkin (2021) <doi:10.1007/s00285-021-01567-5>, Collienne et al. (2021) <doi:10.1007/s00285-021-01685-0>, and Collienne (2021) <http://hdl.handle.net/10523/12606>.
	"""
	
	homepage = "https://rrnni.biods.org/"
	cran = "rrnni" 

	version("0.1.1", md5="79269b8a1b1f9130ea3d24f97743e76b")

	depends_on("r-ape", type=("build", "run"))
