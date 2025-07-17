# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmiccircos(RPackage):
    """High-quality circular visualization of omics data

    OmicCircos is an R application and package for generating high-quality circular plots for omics data.
    """

    bioc = "OmicCircos"

    version("1.46.0", commit="2e20fe3b6b0159138288862af7ebc462e8e5e3dc")
    version("1.40.0", commit="9e358a5c8c0c54828830a3e66fafc9d60facea30")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
