# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeTguttataUcscTaegut2(RPackage):
    """Full genome sequences for Taeniopygia guttata (UCSC version taeGut2)

    Full genome sequences for Taeniopygia guttata (Zebra finch) as provided by UCSC (taeGut2, Feb. 2013) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Tguttata.UCSC.taeGut2"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Tguttata.UCSC.taeGut2_1.4.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Tguttata.UCSC.taeGut2/BSgenome.Tguttata.UCSC.taeGut2_1.4.2.tar.gz",
    ]

    version(
        "1.4.2",
        sha256="2718f4e966618e8c496561e007e23fc2000003d12194baeaaa5fd07370696bc6",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Tguttata.UCSC.taeGut2_1.4.2.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
