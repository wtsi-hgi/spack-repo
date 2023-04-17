# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsample(RPackage):
    """General Resampling Infrastructure.

    Classes and functions to create and summarize different types
    of resampling objects (e.g. bootstrap, cross-validation)."""

    cran = "rsample"

    version("1.1.1", sha256="90d2ae86d27a397ba9d8d010e7dea5c7b86fecbec7e9af273db0c2e8c374b8ba")

    depends_on ("r-dplyr", type=("build", "run"))
    depends_on ("r-furrr", type=("build", "run"))
    depends_on ("r-generics", type=("build", "run"))
    depends_on ("r-glue", type=("build", "run"))
    depends_on ("r-pillar", type=("build", "run"))
    depends_on ("r-purrr", type=("build", "run"))
    depends_on ("r-rlang", type=("build", "run"))
    depends_on ("r-slider", type=("build", "run"))
    depends_on ("r-tibble", type=("build", "run"))
    depends_on ("r-tidyr", type=("build", "run"))
    depends_on ("r-tidyselect", type=("build", "run"))
    depends_on ("r-vctrs", type=("build", "run"))
