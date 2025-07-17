# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTernarynet(RPackage):
    """Ternary Network Estimation

    Gene-regulatory network (GRN) modeling seeks to infer dependencies between genes and thereby provide insight into the regulatory relationships that exist within a cell. This package provides a computational Bayesian approach to GRN estimation from perturbation experiments using a ternary network model, in which gene expression is discretized into one of 3 states: up, unchanged, or down). The ternarynet package includes a parallel implementation of the replica exchange Monte Carlo algorithm for fitting network models, using MPI.
    """

    bioc = "ternarynet"

    version("1.52.0", commit="dc372eea4e0a8b37845c14791da556e2945ceb46")
    version("1.46.0", commit="8dd30d9d9324da2f0e19230cbb4d6ed44798cf97")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
