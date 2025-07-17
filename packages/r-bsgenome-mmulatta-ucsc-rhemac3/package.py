# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmulattaUcscRhemac3(RPackage):
    """Full genome sequences for Macaca mulatta (UCSC version rheMac3)

    Full genome sequences for Macaca mulatta (Rhesus) as provided by UCSC (rheMac3, Oct. 2010) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Mmulatta.UCSC.rheMac3"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmulatta.UCSC.rheMac3_1.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mmulatta.UCSC.rheMac3/BSgenome.Mmulatta.UCSC.rheMac3_1.4.0.tar.gz",
    ]

    version(
        "1.4.0",
        sha256="b1caf21a049aacb6224588c881707ecec556eff9ed9f88f967ace763ca257b64",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmulatta.UCSC.rheMac3_1.4.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
