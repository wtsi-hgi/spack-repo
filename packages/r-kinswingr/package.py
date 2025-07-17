# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKinswingr(RPackage):
    """KinSwingR: network-based kinase activity prediction

    KinSwingR integrates phosphosite data derived from mass-spectrometry data and kinase-substrate predictions to predict kinase activity. Several functions allow the user to build PWM models of kinase-subtrates, statistically infer PWM:substrate matches, and integrate these data to infer kinase activity.
    """

    bioc = "KinSwingR"

    version("1.26.0", commit="fa892c8e3cf66ee1a24180e07f2ffdee0c54e746")
    version("1.20.0", commit="1f21d34538803a31d4a75170544913efb130dd60")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-sqldf", type=("build", "run"))
