# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdrtestdata(RPackage):
    """gDRtestData - R data package with testing dose reponse data

    R package with internal dose-response test data. Package provides functions to generate input testing data that can be used as the input for gDR pipeline. It also contains RDS files with MAE data processed by gDR.
    """

    bioc = "gDRtestData"

    version("1.6.0", commit="5ede591520a0946d0b9d9534eced2274b2343b37")
    version("1.0.0", commit="1ad7f0315b15a80d373a32d81362a6ef67b911d6")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
