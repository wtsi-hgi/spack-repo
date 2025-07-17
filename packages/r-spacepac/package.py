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

    version("1.46.0", commit="f418831d959c5041dfc75bc180e31798819763af")
    version("1.40.0", commit="82b1cf93edd1d3d106854f51530a59f5c932916f")

    depends_on("r@2.15:", type=("build", "run"))
    depends_on("r-ipac", type=("build", "run"))
