# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDerfinderhelper(RPackage):
    """derfinder helper package

    Helper package for speeding up the derfinder package when using multiple cores. This package is particularly useful when using BiocParallel and it helps reduce the time spent loading the full derfinder package when running the F-statistics calculation in parallel.
    """

    homepage = "https://github.com/leekgroup/derfinderHelper"
    bioc = "derfinderHelper"

    version("1.42.0", commit="98041a98070bbae9bc5dd4b5c38f4b54545ea6d4")
    version("1.36.0", commit="dc605200345b7ed67a2bddc3591dfc23f116795f")

    depends_on("r@3.2.2:", type=("build", "run"))
    depends_on("r-iranges@1.99.27:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-s4vectors@0.2.2:", type=("build", "run"))
