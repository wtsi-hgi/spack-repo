# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListeretalbsseq(RPackage):
    """BS-seq data of H1 and IMR90 cell line excerpted from Lister et al. 2009

    Base resolution bisulfite sequencing data of Human DNA methylomes
    """

    bioc = "ListerEtAlBSseq"

    version("1.40.0", commit="8456644b0a6d6b2b8e4ecfa18ca4255e72fb1914")
    version("1.34.0", commit="136e9526b8b15d3ef5c7224f2ed823645a337fdb")

    depends_on("r@3.1.1:", type=("build", "run"))
    depends_on("r-methylpipe", type=("build", "run"))
