# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDart(RPackage):
    """Denoising Algorithm based on Relevance network Topology

    Denoising Algorithm based on Relevance network Topology (DART) is an algorithm designed to evaluate the consistency of prior information molecular signatures (e.g in-vitro perturbation expression signatures) in independent molecular data (e.g gene expression data sets). If consistent, a pruning network strategy is then used to infer the activation status of the molecular signature in individual samples.
    """

    bioc = "DART"

    version("1.56.0", commit="f10aa76e3d6fda995869957c9faf7122a9dd26b6")
    version("1.50.0", commit="e186a7cd98ebb891136bf9dc58293a98c69628f5")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-igraph@0.6:", type=("build", "run"))
