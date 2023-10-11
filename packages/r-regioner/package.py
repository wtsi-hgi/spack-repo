# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RRegioner(RPackage):
    """regioneR offers a statistical framework based on customizable permutation tests to assess the association between genomic region sets and other genomic features."""

    homepage = "https://bioconductor.org/packages/release/bioc/html/regioneR.html"
    url = "https://bioconductor.org/packages/release/bioc/src/contrib/regioneR_1.32.0.tar.gz"
    bioc = "regioneR"

    version("1.32.0", sha256="e16bbe258a05850edd8b270181ef1415445e0ca5cd1d446882ac9a96d4c3343f")

    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-memoise", type=("build", "run"))
