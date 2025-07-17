# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeadsortedSalivaEpic(RPackage):
    """Illumina EPIC data on BeadSorted child saliva cells

    Raw data objects used to estimate saliva cell proportion estimates in ewastools. The FlowSorted.Saliva.EPIC object is constructed from samples assayed by Lauren Middleton et. al. (2021).
    """

    bioc = "BeadSorted.Saliva.EPIC"

    version("1.16.0", commit="82df32a47337b73c40ee786683f92f146b1d7b64")
    version("1.10.0", commit="e2bfe0c65365fa9507ff400b4514581ebd5e66ce")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-minfi@1.36:", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
