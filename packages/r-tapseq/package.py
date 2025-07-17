# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTapseq(RPackage):
    """Targeted scRNA-seq primer design for TAP-seq

    Design primers for targeted single-cell RNA-seq used by TAP-seq. Create sequence templates for target gene panels and design gene-specific primers using Primer3. Potential off-targets can be estimated with BLAST. Requires working installations of Primer3 and BLASTn.
    """

    homepage = "https://github.com/argschwind/TAPseq"
    bioc = "TAPseq"

    version("1.20.0", commit="a6a1f4363ecb75b086a32fc7906517b47145563a")
    version("1.14.1", commit="bc862df8ae415442f86b138c365e69d7e0f23743")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors@0.20.1:", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("primer3@2.5.0:", type=("build", "link", "run"))
    depends_on("blast-plus@2.6.0:", type=("build", "link", "run"))
