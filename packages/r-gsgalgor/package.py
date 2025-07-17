# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsgalgor(RPackage):
    """An Evolutionary Framework for the Identification and Study of Prognostic Gene Expression Signatures in Cancer

    A multi-objective optimization algorithm for disease sub-type discovery based on a non-dominated sorting genetic algorithm. The 'Galgo' framework combines the advantages of clustering algorithms for grouping heterogeneous 'omics' data and the searching properties of genetic algorithms for feature selection. The algorithm search for the optimal number of clusters determination considering the features that maximize the survival difference between sub-types while keeping cluster consistency high.
    """

    homepage = "https://github.com/harpomaxx/GSgalgoR"
    bioc = "GSgalgoR"

    version("1.18.0", commit="326c6fcf22931232ff0a6d3e61a736d913cf9de0")
    version("1.12.0", commit="b3a122751610f1b7dbce5476845b7ecaf676e27a")

    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-matchingr", type=("build", "run"))
    depends_on("r-nsga2r", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-proxy", type=("build", "run"))
