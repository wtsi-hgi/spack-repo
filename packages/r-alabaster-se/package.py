# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterSe(RPackage):
    """Load and Save SummarizedExperiments from File

    Save SummarizedExperiments into file artifacts, and load them back into memory. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
    """

    bioc = "alabaster.se"

    version("1.8.0", commit="504580a05bbbad7de8678dd64dd293aa18c4a2b7")
    version("1.2.0", commit="d1222d4bf0de42896832424f1e476478716c3e3f")

    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-alabaster-base", type=("build", "run"))
    depends_on("r-alabaster-ranges", type=("build", "run"))
    depends_on("r-alabaster-matrix", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
