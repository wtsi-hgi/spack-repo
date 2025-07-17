# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeastexpdata(RPackage):
    """Yeast Experimental Data

    A collection of different sets of experimental data from yeast.
    """

    bioc = "yeastExpData"

    version("0.54.0", commit="b7cdb14dff4099e4a19f3abf744e047b9fabe613")
    version("0.48.0", commit="41b3502c9c24e0be145ba323fced4b811a21680f")

    depends_on("r@2.4:", type=("build", "run"))
    depends_on("r-graph@1.9.26:", type=("build", "run"))
