# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpia(RPackage):
    """Signaling Pathway Impact Analysis (SPIA) using combined evidence of pathway over-representation and unusual signaling perturbations

    This package implements the Signaling Pathway Impact Analysis (SPIA) which uses the information form a list of differentially expressed genes and their log fold changes together with signaling pathways topology, in order to identify the pathways most relevant to the condition under the study.
    """

    homepage = "http://bioinformatics.oxfordjournals.org/cgi/reprint/btn577v1"
    bioc = "SPIA"

    version("2.60.0", commit="6378a74a4174124b17e7ea32d844b9b807bfd2b0")
    version("2.54.0", commit="aa77d2538780141a2c9c068fd483a562a384d10f")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-kegggraph", type=("build", "run"))
