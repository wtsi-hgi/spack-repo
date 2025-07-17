# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgen(RPackage):
    """An R package for analysis of case-control studies in genetic epidemiology

    This is a package for analysis of case-control data in genetic epidemiology. It provides a set of statistical methods for evaluating gene-environment (or gene-genes) interactions under multiplicative and additive risk models, with or without assuming gene-environment (or gene-gene) independence in the underlying population.
    """

    bioc = "CGEN"

    version("3.44.0", commit="941049d1cecac6168056235eb41897a1eba72579")
    version("3.38.0", commit="f9588ed20eb4a6f2d559ea5ca37d8463803cff9e")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
