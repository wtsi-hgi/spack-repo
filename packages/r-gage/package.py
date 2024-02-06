# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGage(RPackage):
    """GAGE is a widely used method for gene set (enrichment or GSEA) or pathway analysis. """

    homepage = "https://github.com/datapplab/gage"
    git = "https://github.com/datapplab/gage"

    version("2.47.1", commit="d99df9a")

    depends_on("R@4:", type=("build", "run"))
    depends_on("r-keggrest", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))

