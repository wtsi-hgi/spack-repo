# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetactivitydata(RPackage):
    """Data required for getting the gene set scores with NetActivity package

    This package contains the weights from pre-trained shallow sparsely-connected autoencoders. This data is required for getting the gene set scores with NetActivity package.
    """

    bioc = "NetActivityData"

    version("1.10.0", commit="ba38acd8405aff79c82e0854d33be1d3194b4929")
    version("1.4.0", commit="6dae8519bdfe293cd7fbe74c3f789ba8a63f20ff")

    depends_on("r@4.2:", type=("build", "run"))
