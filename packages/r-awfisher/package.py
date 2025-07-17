# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwfisher(RPackage):
    """An R package for fast computing for adaptively weighted fisher's method

    Implementation of the adaptively weighted fisher's method, including fast p-value computing, variability index, and meta-pattern.
    """

    bioc = "AWFisher"

    version("1.22.0", commit="adfe7c90910b989dd9107f718fa7c1063d8b3c6d")
    version("1.16.0", commit="76256c87697e81a5d62b5e26b7d4dda0310d1e62")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
