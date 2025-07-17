# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqtools(RPackage):
    """Analysis of nucleotide, sequence and quality content on fastq files

    Analyze read length, phred scores and alphabet frequency and DNA k-mers on uncompressed and compressed fastq files.
    """

    bioc = "seqTools"

    version("1.42.0", commit="66c35359c1c5181406d3b757ee6f995e278f24b4")
    version("1.36.0", commit="0485f6c74a935df0a7926bb76bbe9edc06bf81a6")

    depends_on("r-zlibbioc", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
