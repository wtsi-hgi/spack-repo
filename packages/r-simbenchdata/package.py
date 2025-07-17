# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimbenchdata(RPackage):
    """SimBenchData: a collection of 35 single-cell RNA-seq data covering a wide range of data characteristics

    The SimBenchData package contains a total of 35 single-cell RNA-seq datasets covering a wide range of data characteristics, including major sequencing protocols, multiple tissue types, and both human and mouse sources.
    """

    bioc = "SimBenchData"

    version("1.16.0", commit="99619305102ea5e05d2a6cf1f68d57600b7e99c5")
    version("1.10.0", commit="42c7e7a7bd0b29579ff17da115564cebb86f5d1b")

    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
