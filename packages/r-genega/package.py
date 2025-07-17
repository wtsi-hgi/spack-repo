# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenega(RPackage):
    """Design gene based on both mRNA secondary structure and codon usage bias using Genetic algorithm

    R based Genetic algorithm for gene expression optimization by considering both mRNA secondary structure and codon usage bias, GeneGA includes the information of highly expressed genes of almost 200 genomes. Meanwhile, Vienna RNA Package is needed to ensure GeneGA to function properly.
    """

    homepage = "http://www.tbi.univie.ac.at/~ivo/RNA/"
    bioc = "GeneGA"

    version("1.58.0", commit="34aefbff0e740f8f3c5c6dd05d7f13fd438d7d34")
    version("1.52.0", commit="3a22bb798331907b30a29683138639a52dff5fd6")

    depends_on("r-seqinr", type=("build", "run"))
    depends_on("r-hash", type=("build", "run"))
