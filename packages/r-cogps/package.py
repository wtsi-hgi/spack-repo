# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCogps(RPackage):
    """cancer outlier Gene Profile Sets

    Gene Set Enrichment Analysis of P-value based statistics for outlier gene detection in dataset merged from multiple studies
    """

    bioc = "coGPS"

    version("1.52.0", commit="52bacfab891e4b003e194ba2678d81d08553bafe")
    version("1.46.0", commit="d38d342310f857fd01549fc4dd7c21cffd4506fb")

    depends_on("r@2.13:", type=("build", "run"))
