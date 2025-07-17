# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrivernet(RPackage):
    """Drivernet: uncovering somatic driver mutations modulating transcriptional networks in cancer

    DriverNet is a package to predict functional important driver genes in cancer by integrating genome data (mutation and copy number variation data) and transcriptome data (gene expression data). The different kinds of data are combined by an influence graph, which is a gene-gene interaction network deduced from pathway data. A greedy algorithm is used to find the possible driver genes, which may mutated in a larger number of patients and these mutations will push the gene expression values of the connected genes to some extreme values.
    """

    bioc = "DriverNet"

    version("1.48.0", commit="b361a0d683128e21a7b1f387b7ffb6c66a46532d")
    version("1.42.0", commit="80a010ddc4b770270945ac862ee05462c92a3951")

    depends_on("r@2.10:", type=("build", "run"))
