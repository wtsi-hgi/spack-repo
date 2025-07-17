# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHomoSapiens(RPackage):
    """Annotation package for the Homo.sapiens object

    Contains the Homo.sapiens object to access data from several related annotation packages.
    """

    bioc = "Homo.sapiens"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Homo.sapiens_1.3.1.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/Homo.sapiens/Homo.sapiens_1.3.1.tar.gz",
    ]

    version(
        "1.3.1",
        sha256="014809fc6ef6410be8dc1094c9cb083719f20d999065ae4bf388855be0913b94",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-organismdbi@1.11.39:", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
