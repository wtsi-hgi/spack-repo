# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiomvcclass(RPackage):
    """Model-View-Controller (MVC) Classes That Use Biobase

    Creates classes used in model-view-controller (MVC) design
    """

    bioc = "BioMVCClass"

    version("1.76.0", commit="3435d53142b84e0eef4ee67f8d9df444b2a883ae")
    version("1.70.0", commit="a96216b3ca5e5479ee27c253c9fbd5cb1b27b856")

    depends_on("r@2.1:", type=("build", "run"))
    depends_on("r-mvcclass", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
