# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSetools(RPackage):
    """SEtools: tools for working with SummarizedExperiment

    This includes a set of convenience functions for working with the SummarizedExperiment class. Note that plotting functions historically in this package have been moved to the sechm package (see vignette for details).
    """

    bioc = "SEtools"

    version("1.22.0", commit="eaa5616d7b56c880d18e6485f6219846a3eda76e")
    version("1.16.0", commit="e4c14651b9682b55de4e64cb6afebec63fa94cda")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-sechm", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-openxlsx", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-sva", type=("build", "run"))
