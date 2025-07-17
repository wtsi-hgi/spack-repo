# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabinr(RPackage):
    """Abundance and Compositional Based Binning of Metagenomes

    Provide functions for performing abundance and compositional based binning on metagenomic samples, directly from FASTA or FASTQ files. Functions are implemented in Java and called via rJava. Parallel implementation that operates directly on input FASTA/FASTQ files for fast execution.
    """

    homepage = "https://github.com/gkanogiannis/metabinR"
    bioc = "metabinR"

    version("1.10.0", commit="f3a779473565455659feeb0dee76222b0887c790")
    version("1.4.0", commit="34665b4d2c4fd681f6d2d25e38b20f7a94cd42c2")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-rjava", type=("build", "run"))
    depends_on("openjdk@8:", type=("build", "link", "run"))
