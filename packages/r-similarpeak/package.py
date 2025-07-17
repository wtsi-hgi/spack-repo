# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimilarpeak(RPackage):
    """Metrics to estimate a level of similarity between two ChIP-Seq profiles

    This package calculates metrics which quantify the level of similarity between ChIP-Seq profiles. More specifically, the package implements six pseudometrics specialized in pattern similarity detection in ChIP-Seq profiles.
    """

    homepage = "https://github.com/adeschen/similaRpeak"
    bioc = "similaRpeak"

    version("1.40.0", commit="136d0a7316ccb90eb980f2fa37f2d9fbabce7623")
    version("1.34.0", commit="f4a9a4fed2a7b64d0b05eae06ef04a4570c9cf00")

    depends_on("r-r6@2:", type=("build", "run"))
