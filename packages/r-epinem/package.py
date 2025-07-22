# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpinem(RPackage):
    """epiNEM

    epiNEM is an extension of the original Nested Effects Models (NEM). EpiNEM is able to take into account double knockouts and infer more complex network signalling pathways. It is tailored towards large scale double knock-out screens.
    """

    homepage = "https://github.com/cbg-ethz/epiNEM/"
    bioc = "epiNEM"

    version("1.32.0", commit="b2fc9f7e0c29d1cb966e0f0b4714422885136e35")
    version("1.26.0", commit="b9081ed78d5fadd291991308f87fce47d2b0be7c")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-boolnet", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-latticeextra", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-pcalg", type=("build", "run"))
    depends_on("r-minet", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-mnem", type=("build", "run"))
    depends_on("r-latex2exp", type=("build", "run"))
    depends_on("r-boutroslab-plotting-general", type=("build", "run"))
