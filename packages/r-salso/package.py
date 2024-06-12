# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSalso(RPackage):
    """Search Algorithms and Loss Functions for Bayesian Clustering

    The SALSO algorithm is an efficient randomized greedy search method to find a point estimate for a random partition based on a loss function and posterior Monte Carlo samples. The algorithm is implemented for many loss functions, including the Binder loss and a generalization of the variation of information loss, both of which allow for unequal weights on the two types of clustering mistakes. Efficient implementations are also provided for Monte Carlo estimation of the posterior expected loss of a given clustering estimate. See Dahl, Johnson, Müller (2022) <doi:10.1080/10618600.2022.2069779>.
    """

    homepage = "https://github.com/dbdahl/salso"
    cran = "salso"

    version("0.3.35", md5="a7940b7411cf1f357927ba0c1c12a4e7")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("rust", type=("build", "link", "run"))

    def patch(self):
        filter_file(
            'version <- strsplit(output, " ", fixed = TRUE)[[1]][2]',
            'version <- strsplit(output, " ", fixed = TRUE)[[1]][2]\nversion <- sub("-nightly$", "", version)',
            "tools/cargo_run.R",
            string=True,
        )
