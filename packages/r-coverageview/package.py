# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoverageview(RPackage):
    """Coverage visualization package for R

    This package provides a framework for the visualization of genome coverage profiles. It can be used for ChIP-seq experiments, but it can be also used for genome-wide nucleosome positioning experiments or other experiment types where it is important to have a framework in order to inspect how the coverage distributed across the genome
    """

    bioc = "CoverageView"

    version("1.46.0", commit="df0eab68eca991227600e380eb5a7dae7c160136")
    version("1.40.0", commit="68638abde811029c16b9ec109a4ef23b30e8301e")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-rsamtools@1.19.17:", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-s4vectors@0.7.21:", type=("build", "run"))
    depends_on("r-iranges@2.3.23:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
