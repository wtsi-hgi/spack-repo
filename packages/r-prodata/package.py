# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProdata(RPackage):
    """SELDI-TOF data of Breast cancer samples

    A data package of SELDI-TOF protein mass spectrometry data of 167 breast cancer and normal samples.
    """

    bioc = "ProData"

    version("1.46.0", commit="3c08517a9ba54b980c2d0af8e1ca3299675b417a")
    version("1.40.0", commit="dd11baccd72d50671f546efdc3597f621b32ad49")

    depends_on("r@2.4:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
