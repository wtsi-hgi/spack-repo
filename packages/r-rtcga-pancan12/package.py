# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaPancan12(RPackage):
    """PanCan 12 from Genome Cancer Browser

    Package provides clinical, expression, cnv and mutation data from Genome Cancer Browser.
    """

    bioc = "RTCGA.PANCAN12"

    version("1.36.0", commit="71404f285c9281e44cae5ed25b618979bd39a41b")
    version("1.30.0", commit="2d7a1b99e0b5a27deb14ed71d3974d776f701c85")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-rtcga", type=("build", "run"))
