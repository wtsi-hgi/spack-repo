# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDta(RPackage):
    """Dynamic Transcriptome Analysis

    Dynamic Transcriptome Analysis (DTA) can monitor the cellular response to perturbations with higher sensitivity and temporal resolution than standard transcriptomics. The package implements the underlying kinetic modeling approach capable of the precise determination of synthesis- and decay rates from individual microarray or RNAseq measurements.
    """

    bioc = "DTA"

    version("2.54.0", commit="ab36f85a099b6a5eeea5ad98822a729eacf98457")
    version("2.48.0", commit="5830440af154567015e5b9b14f937564b28e10f2")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-lsd", type=("build", "run"))
    depends_on("r-scatterplot3d", type=("build", "run"))
