# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrornaome(RPackage):
    """SummarizedExperiment for the microRNAome project

    This package provides a SummarizedExperiment object of read counts for microRNAs across tissues, cell-types, and cancer cell-lines. The read count matrix was prepared and provided by the author of the study: Towards the human cellular microRNAome.
    """

    bioc = "microRNAome"

    version("1.30.0", commit="ac499dd38d870537982cd02743870be3ba3e37d0")
    version("1.24.0", commit="0d9653cc70f87ce24f7466de3572f29ff713a654")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
