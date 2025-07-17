# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcoil(RPackage):
    """Prediction of Oligomerization of Coiled Coil Proteins

    The package allows for predicting whether a coiled coil sequence (amino acid sequence plus heptad register) is more likely to form a dimer or more likely to form a trimer. Additionally to the prediction itself, a prediction profile is computed which allows for determining the strengths to which the individual residues are indicative for either class. Prediction profiles can also be visualized as curves or heatmaps.
    """

    homepage = "http://www.bioinf.jku.at/software/procoil/"
    bioc = "procoil"

    version("2.36.0", commit="b467c3a3a7b622bb50957bed4439592c3323adb0")
    version("2.30.0", commit="304b01d3299fb1d06eaa262275eb168ea1b55d4c")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-kebabs", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
