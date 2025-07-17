# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedisparam(RPackage):
    """Provide a 'redis' back-end for BiocParallel

    This package provides a Redis-based back-end for BiocParallel, enabling an alternative mechanism for distributed computation. The The 'manager' distributes tasks to a 'worker' pool through a central Redis server, rather than directly to workers as with other BiocParallel implementations. This means that the worker pool can change dynamically during job evaluation. All features of BiocParallel are supported, including reproducible random number streams, logging to the manager, and alternative 'load balancing' task distributions.
    """

    bioc = "RedisParam"

    version("1.10.0", commit="2ef834fca488758fe0c3b1f8b2a43f9067aebfe0")
    version("1.4.0", commit="2d32ea847832b0125c25f12f6e4b6208877585fd")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-biocparallel@1.29.12:", type=("build", "run"))
    depends_on("r-redux", type=("build", "run"))
    depends_on("r-withr", type=("build", "run"))
    depends_on("r-futile-logger", type=("build", "run"))
    depends_on("hiredis", type=("build", "link", "run"))
