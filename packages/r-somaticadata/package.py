# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomaticadata(RPackage):
    """An example cancer whole genome sequencing data for the SomatiCA package

    An example cancer whole genome sequencing data for the SomatiCA package
    """

    bioc = "SomatiCAData"

    version("1.46.0", commit="0af5e9f26178eb837ffc4ab701043ef697a32cd6")
    version("1.40.0", commit="cee61d4a415202dcf7fc6c3e222c37d2dbe8f23b")

    depends_on("r@2.14:", type=("build", "run"))
