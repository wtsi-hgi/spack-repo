# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqcnaAnnot(RPackage):
    """Annotation for the copy number analysis of deep sequencing cancer data with seqCNA

    Provides annotation on GC content, mappability and genomic features for various genomes
    """

    bioc = "seqCNA.annot"

    version("1.38.0", commit="d8179ef4ea93e1dc2d8b868c77bf105789d8e5a4")

    depends_on("r@2.10:", type=("build", "run"))
