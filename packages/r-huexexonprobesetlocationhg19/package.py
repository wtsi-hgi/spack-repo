# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuexexonprobesetlocationhg19(RPackage):
    """Exon-level probeset chromosome location for microarrays of type HuEx

    This package was automatically created by package AnnotationDbi version 1.11.8. The exon-level probeset genome location was retrieved from Netaffx using AffyCompatible. The exon-level probeset genome location was retrieved from Netaffx using AffyCompatible. Genome release hg19.
    """

    bioc = "HuExExonProbesetLocationHg19"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/HuExExonProbesetLocationHg19_0.0.3.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/HuExExonProbesetLocationHg19/HuExExonProbesetLocationHg19_0.0.3.tar.gz",
    ]

    version(
        "0.0.3",
        sha256="b0fb35096890bfd8020b3c085457421c024614bcdd68de57198909c6c5064440",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/HuExExonProbesetLocationHg19_0.0.3.tar.gz",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.8:", type=("build", "run"))
