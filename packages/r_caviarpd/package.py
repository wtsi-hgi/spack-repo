# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaviarpd(RPackage):
    """Cluster Analysis via Random Partition Distributions

    Cluster analysis is performed using pairwise distance information and a random partition distribution. The method is
    implemented for two random partition distributions. It draws samples and then obtains and plots clustering estimates.
    An implementation of a selection algorithm is provided for the mass parameter of the partition distribution. Since
    pairwise distances are the principal input to this procedure, it is most comparable to the hierarchical and k-medoids
    clustering methods. The method is Dahl, Andros, Carter (2022+) <doi:10.1002/sam.11602>.
    """

    homepage = "https://github.com/dbdahl/caviarpd"
    cran = "caviarpd"

    version("0.3.9", md5="87de50b6a68b1a1fa16671e6f8e9c457")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("rust", type=("build", "link", "run"))

    def patch(self):
        filter_file(
            'version <- strsplit(output, " ", fixed = TRUE)[[1]][2]',
            'version <- strsplit(output, " ", fixed = TRUE)[[1]][2]\nversion <- sub("-nightly$", "", version)',
            "tools/cargo_run.R",
            string=True,
        )
