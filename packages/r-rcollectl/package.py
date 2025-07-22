# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcollectl(RPackage):
    """Help use collectl with R in Linux, to measure resource consumption in R processes

    Provide functions to obtain instrumentation data on processes in a unix environment.  Parse output of a collectl run.  Vizualize aspects of system usage over time, with annotation.
    """

    homepage = "https://github.com/vjcitn/Rcollectl"
    bioc = "Rcollectl"

    version("1.8.0", commit="1b03bdce5279227193bb733a5b3427c1afdce96a")
    version("1.2.0", commit="5a64468353ababf782302ad003607be0ca7449f3")

    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-lubridate", type=("build", "run"))
    depends_on("r-processx", type=("build", "run"))
