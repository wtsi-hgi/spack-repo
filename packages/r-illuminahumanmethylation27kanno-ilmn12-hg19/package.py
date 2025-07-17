# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanmethylation27kannoIlmn12Hg19(RPackage):
    """Annotation for Illumina's 27k methylation arrays

    An annotation package for Illumina's EPIC methylation arrays.
    """

    bioc = "IlluminaHumanMethylation27kanno.ilmn12.hg19"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylation27kanno.ilmn12.hg19_0.6.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/IlluminaHumanMethylation27kanno.ilmn12.hg19/IlluminaHumanMethylation27kanno.ilmn12.hg19_0.6.0.tar.gz",
    ]

    version(
        "0.6.0",
        sha256="e3ee241ef2d0c09a30f2fd3634289137093d80b2a2e0431a2086953e6c37be45",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylation27kanno.ilmn12.hg19_0.6.0.tar.gz",
    )

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-minfi@1.19.15:", type=("build", "run"))
