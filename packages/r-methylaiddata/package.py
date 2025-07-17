# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylaiddata(RPackage):
    """MethylAid-summarized data for 2800 Illumina 450k array samples and 2620 EPIC array samples

    A data package containing summarized Illumina 450k array data on 2800 samples and summarized EPIC data for 2620 samples. The data can be use as a background data set in the interactive application.
    """

    bioc = "MethylAidData"

    version("1.40.0", commit="dfcde38a787426b6ef2daa41efcef6780e3f2647")
    version("1.34.0", commit="e56febae0340bba37d870704c27052aacb0cf18e")

    depends_on("r-methylaid", type=("build", "run"))
    depends_on("r@3.2:", type=("build", "run"))
