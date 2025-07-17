# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnadata(RPackage):
    """Social Networks Analysis Data Examples

    Data from Wasserman & Faust (1999) "Social Network Analysis"
    """

    bioc = "SNAData"

    version("1.54.0", commit="42d9de1932440064b20a486a11390e8724c73cc8")
    version("1.48.0", commit="20c46b8cb5535969cd902b1a624fca6f1c58fb80")

    depends_on("r@2.4:", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
