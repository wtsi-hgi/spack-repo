# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaggle(RPackage):
    """Broadcast data between R and Gaggle

    This package contains functions enabling data exchange between R and Gaggle enabled bioinformatics software, including Cytoscape, Firegoose and Gaggle Genome Browser.
    """

    homepage = "http://gaggle.systemsbiology.net/docs/geese/r/"
    bioc = "gaggle"

    version("1.70.0", commit="ea1b1b6524e66af2c595556b9b1f5998b2bf56cf")

    depends_on("r@2.3:", type=("build", "run"))
    depends_on("r-rjava@0.4:", type=("build", "run"))
    depends_on("r-graph@1.10.2:", type=("build", "run"))
    depends_on("r-runit@0.4.17:", type=("build", "run"))
