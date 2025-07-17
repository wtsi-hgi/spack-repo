# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcistargetHg19MotifdbsCisbponly500bp(RPackage):
    """RcisTarget motif databases for human (hg19) - Subset of 4.6k motifs

    RcisTarget databases: Gene-based motif rankings and annotation to transcription factors. This package contains a subset of 4.6k motifs (cisbp motifs), scored only within 500bp upstream and the TSS. See RcisTarget tutorial to download the full databases, containing 20k motifs and search space up to 10kbp around the TSS.
    """

    homepage = "http://scenic.aertslab.org"
    bioc = "RcisTarget.hg19.motifDBs.cisbpOnly.500bp"

    version("1.28.0", commit="6030af7438e5defced8abf1b8d5cfdfb56685f06")
    version("1.22.0", commit="524a41d9f53c033668274e7cb1d6730c0febc234")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
