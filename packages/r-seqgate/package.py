# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqgate(RPackage):
    """Filtering of Lowly Expressed Features

    Filtering of lowly expressed features (e.g. genes) is a common step before performing statistical analysis, but an arbitrary threshold is generally chosen. SeqGate implements a method that rationalize this step by the analysis of the distibution of counts in replicate samples. The gate is the threshold above which sequenced features can be considered as confidently quantified.
    """

    bioc = "SeqGate"

    version("1.18.0", commit="12c54ff78a927f2f6e8bda0d0d8096d5a1734f0f")
    version("1.12.0", commit="6332aeb3a1dfb340378fabd5023f594dacc980b8")

    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
