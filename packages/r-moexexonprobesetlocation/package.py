# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoexexonprobesetlocation(RPackage):
    """Probe sequence data for microarrays of type MoEx

    This package was automatically created by package AnnotationForge version 1.7.17. The exon-level probeset genome location was retrieved from Netaffx using AffyCompatible.
    """

    bioc = "MoExExonProbesetLocation"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/MoExExonProbesetLocation_1.15.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/MoExExonProbesetLocation/MoExExonProbesetLocation_1.15.0.tar.gz",
    ]

    version(
        "1.15.0",
        sha256="876a93b68241eb4e2b77190c9f6b5bb15d8f55b0a72cf265af9c2f12e51a722f",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.7.17:", type=("build", "run"))
