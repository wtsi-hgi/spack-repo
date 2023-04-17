# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFurrr(RPackage):
    """Apply Mapping Functions in Parallel using Futures.

    Implementations of the family of map() functions from 'purrr'
    that can be resolved using any 'future'-supported backend, e.g.
    parallel on the local machine or distributed on a compute cluster."""

    cran = "furrr"

    version("0.3.1", sha256="0d91735e2e9be759b1ab148d115c2c7429b79740514778828e5dab631dc0e48b")

    depends_on("r@3.4.0:", type=("build", "run"))
    depends_on("r-future@1.25.0:", type=("build", "run"))
    depends_on("r-globals@0.14.0:", type=("build", "run"))
    depends_on("r-lifecycle@1.0.1:", type=("build", "run"))
    depends_on("r-purrr@0.3.4:", type=("build", "run"))
    depends_on("r-rlang@1.0.2:", type=("build", "run"))
    depends_on("r-vctrs@0.4.1:", type=("build", "run"))
