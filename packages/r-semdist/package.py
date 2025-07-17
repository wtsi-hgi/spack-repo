# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemdist(RPackage):
    """Information Accretion-based Function Predictor Evaluation

    This package implements methods to calculate information accretion for a given version of the gene ontology and uses this data to calculate remaining uncertainty, misinformation, and semantic similarity for given sets of predicted annotations and true annotations from a protein function predictor.
    """

    homepage = "http://github.com/iangonzalez/SemDist"
    bioc = "SemDist"

    version("1.42.0", commit="97a85b0d1d5fcb331a32b663fb08abf46652126d")
    version("1.36.0", commit="bf8559da3fbb57afdfe3bcecbd1ddfac354e2466")

    depends_on("r@3.1:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-annotate", type=("build", "run"))
