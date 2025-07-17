# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIclusterplus(RPackage):
    """Integrative clustering of multi-type genomic data

    Integrative clustering of multiple genomic data using a joint latent variable model.
    """

    bioc = "iClusterPlus"

    version("1.44.0", commit="a1db2358f2bd7d3d014192abc2f97925813c80f6")
    version("1.38.0", commit="600249ea684b661d7db68272a65344ae873a31f1")

    depends_on("r@4.1:", type=("build", "run"))
