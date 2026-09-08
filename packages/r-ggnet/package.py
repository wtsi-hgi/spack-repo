# Copyright 2013-2026 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgnet(RPackage):
    """Plot networks as ggplot2 objects.

    Provides the ggnet and ggnet2 functions for plotting network objects with
    ggplot2. ggnet2 offers extensive control over node and edge aesthetics.
    """

    homepage = "https://github.com/briatte/ggnet"
    git = "https://github.com/briatte/ggnet.git"

    license("GPL-3.0-only")

    version("20160129", commit="da9a7cf2fac24a37ef626e6143ee376eebbdf2d8")

    depends_on("r", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("r-ggplot2")
        depends_on("r-network")
        depends_on("r-scales")
        depends_on("r-sna")
