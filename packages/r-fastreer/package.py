# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastreer(RPackage):
    """Phylogenetic, Distance and Other Calculations on VCF and Fasta Files

    Calculate distances, build phylogenetic trees or perform hierarchical clustering between the samples of a VCF or FASTA file. Functions are implemented in Java and called via rJava. Parallel implementation that operates directly on the VCF or FASTA file for fast execution.
    """

    homepage = "https://github.com/gkanogiannis/fastreeR"
    bioc = "fastreeR"

    version("1.6.0", commit="776d4ceb4f5be3113532d279420d3ae088f6ba8a")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dynamictreecut", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-rjava", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("openjdk@8:", type=("build", "link", "run"))
