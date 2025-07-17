# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicade4(RPackage):
    """Multiple co-inertia analysis of omics datasets

    This package performes multiple co-inertia analysis of omics datasets.
    """

    bioc = "omicade4"

    version("1.48.0", commit="1677af8d101b9ebb649879476f8583c0452f1d7d")
    version("1.42.0", commit="53ca069cda60845888830431aab065cfcc1e8e6c")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-ade4", type=("build", "run"))
    depends_on("r-made4", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
