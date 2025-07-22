# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeAmelliferaUcscApimel2(RPackage):
    """Full genome sequences for Apis mellifera (UCSC version apiMel2)

    Full genome sequences for Apis mellifera (Honey Bee) as provided by UCSC (apiMel2, Jan. 2005) and stored in Biostrings objects.
    """

    bioc = "BSgenome.Amellifera.UCSC.apiMel2"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Amellifera.UCSC.apiMel2_1.4.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Amellifera.UCSC.apiMel2/BSgenome.Amellifera.UCSC.apiMel2_1.4.0.tar.gz",
    ]

    version(
        "1.4.0",
        sha256="8f9c667de4f6043997cf71922cffd84abf3d453859e533a76f1e1f4fd5e1c7a4",
        url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Amellifera.UCSC.apiMel2_1.4.0.tar.gz",
    )

    depends_on("r-bsgenome", type=("build", "run"))
