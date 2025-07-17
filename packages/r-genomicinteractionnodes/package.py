# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicinteractionnodes(RPackage):
    """A R/Bioconductor package to detect the interaction nodes from HiC/HiChIP/HiCAR data

    The GenomicInteractionNodes package can import interactions from bedpe file and define the interaction nodes, the genomic interaction sites with multiple interaction loops. The interaction nodes is a binding platform regulates one or multiple genes. The detected interaction nodes will be annotated for downstream validation.
    """

    homepage = "https://github.com/jianhong/GenomicInteractionNodes"
    bioc = "GenomicInteractionNodes"

    version("1.12.0", commit="a109a3c3c22cc1ee925c5f430b8d5d6790ced24c")
    version("1.6.0", commit="eb1f8b056f9d3313661b980ca64b4304ba813e03")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rbgl", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
