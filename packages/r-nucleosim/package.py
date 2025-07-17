# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNucleosim(RPackage):
    """Generate synthetic nucleosome maps

    This package can generate a synthetic map with reads covering the nucleosome regions as well as a synthetic map with forward and reverse reads emulating next-generation sequencing. The synthetic hybridization data of “Tiling Arrays” can also be generated. The user has choice between three different distributions for the read positioning: Normal, Student and Uniform. In addition, a visualization tool is provided to explore the synthetic nucleosome maps.
    """

    homepage = "https://github.com/arnauddroitlab/nucleoSim"
    bioc = "nucleoSim"

    version("1.36.0", commit="126daee3937c27b2a1b4c6525c12e7fbe31710d4")
    version("1.30.0", commit="6455637f40fdbc911fed7f285329b4ef7e835cac")

    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
