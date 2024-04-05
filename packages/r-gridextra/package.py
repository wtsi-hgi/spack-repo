# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RGridextra(RPackage):
    """Provides a number of user-level functions to work with "grid" graphics, notably to arrange multiple grid-based plots on a page, and draw tables."""

    cran = "gridExtra"

    version("2.3", sha256="81b60ce6f237ec308555471ae0119158b115463df696d2eca9b177ded8988e3b")
    version("2.2.1", sha256="44fe455a5bcdf48a4ece7a542f83e7749cf251dc1df6ae7634470240398c6818")
    version("2.2.0", sha256="87a4f78cd1875b1a43be118953ef555d0436076791d51b5dacc6ec9be6934450")
    version("2.0.0", sha256="27dc76f75eb08f99a4ab0f629a016250722368528ca6b515edb0b0339acbdea7")
    version("0.9.1", sha256="1d0e7f10b2b35716d38dd71113ed247599f910922906f0097fc865ca0b2ff296")
    version("0.9", sha256="eaeaa36ae8007e9e2ba6f01484bc474a1e19f4b820f9cc25c69010e7fcf3190e")
    version("0.8.5", sha256="68cc8568ed4308c6778330a4cd9a2e4e3e9d72a399145e4ee96f44b65e4597ce")
    version("0.8", sha256="431d7120420de5147becac2f6212cac62a174e043cd09f7f33cfa4eeb43905a2")
    version("0.7", sha256="50ff1c2eafcf5b4065704ba223f1e34f597c9317dd61f22d91f437f72bb70a16")
    version("0.6.5", sha256="f877a80fd85a53075f51e45910ccecd39989dabfc239f5a9244cc78e8cd0e7d5")
    version("0.6", sha256="c3f6d7f7b54dc4eea674929025b0ebf2127ac4634fe78a0c53cdc9a1cd98bb70")

    depends_on("r-gtable", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
