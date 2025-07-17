# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglemoleculefootprintingdata(RPackage):
    """Data supporting the SingleMoleculeFootprinting pkg

    This Data package contains data objcets relevanat for the SingleMoleculeFootprinting package. More specifically, it contains one example of aligned sequencing data (.bam & .bai) necessary to run the SingleMoleculeFootprinting vignette. Additionally, we provide data that are essential for some functions to work correctly such as BaitCapture() and SampleCorrelation().
    """

    bioc = "SingleMoleculeFootprintingData"

    version("1.16.0", commit="8409153374d2a2dd5e10278732aaa40d56e5ae62")
    version("1.10.0", commit="9d50ed387eab62cc25d370d809a6cd2ec79e9f74")

    depends_on("r-experimenthub", type=("build", "run"))
