# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpip(RPackage):
    """Host-Pathogen Interaction Prediction

    HPiP (Host-Pathogen Interaction Prediction) uses an ensemble learning algorithm for prediction of host-pathogen protein-protein interactions (HP-PPIs) using structural and physicochemical descriptors computed from amino acid-composition of host and pathogen proteins.The proposed package can effectively address data shortages and data unavailability for HP-PPI network reconstructions. Moreover, establishing computational frameworks in that regard will reveal mechanistic insights into infectious diseases and suggest potential HP-PPI targets, thus narrowing down the range of possible candidates for subsequent wet-lab experimental validations.
    """

    homepage = "https://github.com/mrbakhsh/HPiP"
    bioc = "HPiP"

    version("1.14.0", commit="e2435b77fcf3b01ba08ede8e3c374c20350696ba")
    version("1.8.0", commit="677208a56902bf6502e45d524c8814f06eb64468")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-dplyr@1.0.6:", type=("build", "run"))
    depends_on("r-httr@1.4.2:", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-caret", type=("build", "run"))
    depends_on("r-corrplot", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-proc", type=("build", "run"))
    depends_on("r-prroc", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-protr", type=("build", "run"))
    depends_on("r-mcl", type=("build", "run"))
