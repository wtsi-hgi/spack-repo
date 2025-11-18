# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RSeqinfo(RPackage):
    """ The Seqinfo class stores the names, lengths, circularity flags, and genomes for a particular collection of sequences. These sequences are typically the chromosomes and/or scaffolds of a specific genome assembly of a given organism. Seqinfo objects are rarely used as standalone objects. Instead, they are used as part of higher-level objects to represent their seqinfo() component. Examples of such higher-level objects are GRanges, RangedSummarizedExperiment, VCF, GAlignments, etc... defined in other Bioconductor infrastructure packages."""

    homepage = "https://bioconductor.org/packages/release/bioc/html/Seqinfo.html"
    url = "https://bioconductor.org/packages/3.22/bioc/src/contrib/Seqinfo_1.0.0.tar.gz"
    bioc = "Seqinfo"

    version("1.0.0", sha256="d72c95a5593ef0c5e343baa7d935583540abdc30c6f4d4c9178ecc8d89234d82")

    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors@0.47.6:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
