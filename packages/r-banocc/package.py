# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBanocc(RPackage):
    """Bayesian ANalysis Of Compositional Covariance

    BAnOCC is a package designed for compositional data, where each sample sums to one. It infers the approximate covariance of the unconstrained data using a Bayesian model coded with `rstan`. It provides as output the `stanfit` object as well as posterior median and credible interval estimates for each correlation element.
    """

    bioc = "banocc"

    version("1.32.0", commit="e7327d189d6726a914a85f2a00dc98b3ce258493")
    version("1.26.0", commit="843878f352947b6adac224988d62035102807167")

    depends_on("r@3.5.1:", type=("build", "run"))
    depends_on("r-rstan@2.17.4:", type=("build", "run"))
    depends_on("r-coda@0.18.1:", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
