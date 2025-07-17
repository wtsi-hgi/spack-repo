# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133abarcodevecs(RPackage):
    """hgu133a data for barcode

    Data used by the barcode package for microarrays of type hgu133a.
    """

    bioc = "hgu133abarcodevecs"

    version("1.46.0", commit="d52f041ff9072d85502e01580ceb33e7c7daaf92")
    version("1.40.0", commit="37008009dd28243187a369572ac94c3fbea5d2b8")

    depends_on("r@2.10:", type=("build", "run"))
