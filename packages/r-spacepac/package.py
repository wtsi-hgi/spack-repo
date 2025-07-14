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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SpacePAC_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SpacePAC/SpacePAC_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="a251d26c5f48982a1f719df261c8ed4fc03682a572188bf0692c812cc3be2f2d")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-ipac", type=("build", "run"))
