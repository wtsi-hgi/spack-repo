# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterjudge(RPackage):
    """Judging Quality of Clustering Methods using Mutual Information

    ClusterJudge implements the functions, examples and other software published as an algorithm by Gibbons, FD and Roth FP. The article is called "Judging the Quality of Gene Expression-Based Clustering Methods Using Gene Annotation" and it appeared in Genome Research, vol. 12, pp1574-1581 (2002). See package?ClusterJudge for an overview.
    """

    bioc = "ClusterJudge"

    version("1.30.0", commit="ded1f3bf06b595e7434a734be6d6f9fca6e56191")
    version("1.24.0", commit="7f8d8c940dcd685d13affb1496d361eea721a27f")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-infotheo", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-latticeextra", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
