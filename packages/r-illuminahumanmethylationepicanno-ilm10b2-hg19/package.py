# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanmethylationepicannoIlm10b2Hg19(RPackage):
    """Annotation for Illumina's EPIC methylation arrays

    An annotation package for Illumina's EPIC methylation arrays.
    """

    homepage = "https://bitbucket.com/kasperdanielhansen/Illumina_EPIC"
    bioc = "IlluminaHumanMethylationEPICanno.ilm10b2.hg19"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylationEPICanno.ilm10b2.hg19_0.6.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/IlluminaHumanMethylationEPICanno.ilm10b2.hg19/IlluminaHumanMethylationEPICanno.ilm10b2.hg19_0.6.0.tar.gz",
    ]

    version(
        "0.6.0",
        sha256="4decdbc78a6a8d02bf8aecb0d6e1d81134ae9dbc2375add52574f07829e8cd69",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylationEPICanno.ilm10b2.hg19_0.6.0.tar.gz",
    )

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-minfi@1.19.15:", type=("build", "run"))
