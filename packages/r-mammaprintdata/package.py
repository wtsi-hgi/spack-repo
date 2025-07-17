# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMammaprintdata(RPackage):
    """RGLists from the Glas and Buyse breast cancer studies

    Gene expression data for the two breast cancer cohorts published by Glas and Buyse in 2006. This cohorts were used to implement and validate the mammaPrint breast cancer test.
    """

    homepage = "http://luigimarchionni.org/breastTSP.html"
    bioc = "mammaPrintData"

    version("1.44.0", commit="46ed2ceccb5ff70db7e9024872c2e03f5e43d41e")
    version("1.38.0", commit="d0c57c48f10d3aec6e626303663e51ea6e8fdb55")

    depends_on("r@2.13:", type=("build", "run"))
