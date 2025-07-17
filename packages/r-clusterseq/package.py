# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterseq(RPackage):
    """Clustering of high-throughput sequencing data by identifying co-expression patterns

    Identification of clusters of co-expressed genes based on their expression across multiple (replicated) biological samples.
    """

    bioc = "clusterSeq"

    version("1.32.0", commit="d7e95f9a4dce8e3d72ef759cd393869a5144dee7")
    version("1.26.0", commit="61fea32b5c12b26c29293efbecfa1ca8ead0a8d3")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-bayseq", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
