# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcan(RPackage):
    """Phenotype Consensus ANalysis (PCAN)

    Phenotypes comparison based on a pathway consensus approach. Assess the relationship between candidate genes and a set of phenotypes based on additional genes related to the candidate (e.g. Pathways or network neighbors).
    """

    bioc = "PCAN"

    version("1.36.0", commit="4a2add9a4bf8cd96cbc7fd423286aebf5f65123a")
    version("1.30.0", commit="747982994e45008b253aad23c88affd6cd79785c")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
