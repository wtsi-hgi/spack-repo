# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT
# file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmptydropsmultiome(RPackage):
    """Sensitive and specific selection of nuclei-containing droplets in
    multiome datasets."""

    homepage = "https://github.com/MarioniLab/EmptyDropsMultiome"
    git = "https://github.com/MarioniLab/EmptyDropsMultiome.git"

    license = "GPL-3.0-or-later"

    version("20240603", commit="5fd8e2f154e03f15a719ea8852b320f4310554e8")

    depends_on("r", type=("build", "run"))
    depends_on("r-dropletutils", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-mixtools", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
