# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethinheritsim(RPackage):
    """Simulating Whole-Genome Inherited Bisulphite Sequencing Data

    Simulate a multigeneration methylation case versus control experiment with inheritance relation using a real control dataset.
    """

    homepage = "https://github.com/belleau/methInheritSim"
    bioc = "methInheritSim"

    version("1.30.0", commit="8055b10bfcbea0a6023f6e3fccd40b8d51915afa")
    version("1.24.0", commit="fd8596a82dfc655cc488eca1f7ae41a7759b7ad5")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-methylkit", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-msm", type=("build", "run"))
