# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgadem(RPackage):
    """de novo motif discovery

    rGADEM is an efficient de novo motif discovery tool for large-scale genomic sequence data. It is an open-source R package, which is based on the GADEM software.
    """

    bioc = "rGADEM"

    version("2.56.0", commit="84be722eace2755f96eb646d890e6a4b0ee28d0e")
    version("2.50.0", commit="2ec7aeb3789ffa7b3b63b723c74320cad8b01837")

    depends_on("r@2.11:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-seqlogo", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
