# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicstate(RPackage):
    """Build and access GenomicState objects for use with derfinder tools from sources like Gencode

    This package contains functions for building GenomicState objects from different annotation sources such as Gencode. It also provides access to these files at JHPCE.
    """

    homepage = "https://github.com/LieberInstitute/GenomicState"
    bioc = "GenomicState"

    version("0.99.16", commit="9682b17d2cd14d8603830c189d02cde17c62c5a0")
    version("0.99.15", commit="e13845af3046a6442c538d098659904f6b54d897")

    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-bumphunter", type=("build", "run"))
    depends_on("r-derfinder@1.21.7:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
