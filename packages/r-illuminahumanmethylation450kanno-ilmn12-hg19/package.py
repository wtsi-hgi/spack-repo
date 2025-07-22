# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanmethylation450kannoIlmn12Hg19(RPackage):
    """Annotation for Illumina's 450k methylation arrays.

    Manifests and annotation for Illumina's 450k array data."""

    # This package is available via bioconductor but there is no available git
    # repository.
    bioc = "IlluminaHumanMethylation450kanno.ilmn12.hg19"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylation450kanno.ilmn12.hg19_0.6.1.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/IlluminaHumanMethylation450kanno.ilmn12.hg19/IlluminaHumanMethylation450kanno.ilmn12.hg19_0.6.1.tar.gz",
    ]
    version(
        "0.6.1",
        md5="aeafc54d887b128ed265fa704a3efa42",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylation450kanno.ilmn12.hg19_0.6.1.tar.gz",
    )
    version(
        "0.6.0",
        url="https://bioconductor.org/packages/3.4/data/annotation/src/contrib/IlluminaHumanMethylation450kanno.ilmn12.hg19_0.6.0.tar.gz",
        sha256="249b8fd62add3c95b5047b597cff0868d26a98862a47cebd656edcd175a73b15",
    )

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-minfi@1.19.15:", type=("build", "run"))
