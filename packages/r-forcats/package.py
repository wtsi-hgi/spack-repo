# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForcats(RPackage):
    """Tools for Working with Categorical Variables (Factors).

    Helpers for reordering factor levels (including moving specified levels to
    front, ordering by first appearance, frequency, or a supplied vector), and
    tools for modifying factor levels (including collapsing rare levels into an
    'other' level). Part of the tidyverse.
    """

    cran = "forcats"

    # Versions fetched via: spack checksum -b r-forcats
    version("1.0.0", sha256="c5bb157909d92e1e1a427c0dc5cb358ea00a43a14918a9088fa4f6630962254e")
    version("0.5.2", sha256="14a60a43183f82da0fbf42633cee446d21dcbb98a8c37361b5c8061a4da86141")
    version("0.5.1", sha256="c4fb96e874e2bedaa8a1aa32ea22abdee7906d93b5c5c7b42c0894c0c5b6a289")
    version("0.5.0", sha256="8f960e789333ec597ddf2d653a64e330f03b86f465e9b71f6779f227355d90c4")
    version("0.4.0", sha256="7c83cb576aa6fe1379d7506dcc332f7560068b2025f9e3ab5cd0a5f28780d2b2")
    version("0.3.0", sha256="95814610ec18b8a8830eba63751954387f9d21400d6ab40394ed0ff22c0cb657")
    version("0.2.0", sha256="b5bce370422d4c0ec9509249ae645373949bfbe9217cdf50dce2bfbdad9f7cd7")
    version("0.1.1", sha256="814663e5203ec203040ee22209c7b208d39b67d618c5a448f1a357c07e16b600")
    version("0.1.0", sha256="28d12d7b6ca6b5696ec4fb3102e0e7b5af65f9b69dae0ae2d1b21183767a03ea")

    # Dependencies (align with tidyverse conventions; versions chosen to be reasonable)
    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
    depends_on("r-rlang@1:", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
