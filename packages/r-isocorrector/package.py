# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsocorrector(RPackage):
    """Correction for natural isotope abundance and tracer purity in MS and MS/MS data from stable isotope labeling experiments

    IsoCorrectoR performs the correction of mass spectrometry data from stable isotope labeling/tracing metabolomics experiments with regard to natural isotope abundance and tracer impurity. Data from both MS and MS/MS measurements can be corrected (with any tracer isotope: 13C, 15N, 18O...), as well as ultra-high resolution MS data from multiple-tracer experiments (e.g. 13C and 15N used simultaneously). See the Bioconductor package IsoCorrectoRGUI for a graphical user interface to IsoCorrectoR. NOTE: With R version 4.0.0, writing correction results to Excel files may currently not work on Windows. However, writing results to csv works as before.
    """

    homepage = "https://genomics.ur.de/files/IsoCorrectoR/"
    bioc = "IsoCorrectoR"

    version("1.26.0", commit="96af901c292ee8819185394ddff0d788ffc30a67")
    version("1.20.0", commit="3178d35c93c7c00a4b0c3d104d0c8e09b7160a91")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-quadprog", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-readxl", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-pracma", type=("build", "run"))
    depends_on("r-writexls", type=("build", "run"))
