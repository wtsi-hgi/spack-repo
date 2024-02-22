# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpacepac(RPackage):
	"""Identification of Mutational Clusters in 3D Protein Space via Simulation.

	Identifies clustering of somatic mutations in proteins via a simulation approach while considering the protein's tertiary structure.
	"""
	
	bioc = "SpacePAC" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SpacePAC_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SpacePAC/SpacePAC_1.40.0.tar.gz"]

	version("1.40.0", md5="aa35450e9ef0b3cd7ca3d90262d36ddf")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-ipac", type=("build", "run"))
