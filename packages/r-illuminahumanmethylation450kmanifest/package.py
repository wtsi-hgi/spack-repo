# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanmethylation450kmanifest(RPackage):
    """Annotation for Illumina's 450k methylation arrays."""

    bioc = "IlluminaHumanMethylation450kmanifest"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylation450kmanifest_0.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/IlluminaHumanMethylation450kmanifest/IlluminaHumanMethylation450kmanifest_0.4.0.tar.gz",
    ]

    version(
        "0.4.0",
        sha256="41b2e54bac3feafc7646fe40bce3aa2b92c10871b0a13657c5736517792fa763",
    )

    depends_on("r@2.13:", type=("build", "run"))
    depends_on("r-minfi", type=("build", "run"))
