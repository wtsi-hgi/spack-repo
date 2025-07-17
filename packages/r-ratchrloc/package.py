# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRatchrloc(RPackage):
    """A data package containing annotation data for ratCHRLOC

    Annotation data file for ratCHRLOC assembled using data from public data repositories
    """

    bioc = "ratCHRLOC"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ratCHRLOC_2.1.6.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ratCHRLOC/ratCHRLOC_2.1.6.tar.gz",
    ]

    version(
        "2.1.6",
        sha256="4b5b0cc170320c97565ef5191f53c79b74ebacc101874ca0fc92b7bd3935f355",
    )

    depends_on("r@2.7:", type=("build", "run"))
