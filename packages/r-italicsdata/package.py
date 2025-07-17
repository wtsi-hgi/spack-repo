# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItalicsdata(RPackage):
    """ITALICSData

    Data needed to use the ITALICS package
    """

    homepage = "http://bioinfo.curie.fr"
    bioc = "ITALICSData"

    version("2.46.0", commit="c440a8231510e5d9eb8fa76d51846fef00ff6e35")
    version("2.40.0", commit="90cbb17d8641cf788ee183f919827ec6cbba0168")

    depends_on("r@2:", type=("build", "run"))
