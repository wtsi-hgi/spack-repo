# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnamodrData(RPackage):
    """Example data for the RNAmodR package

    RNAmodR.Data contains example data, which is used for vignettes and example workflows in the RNAmodR and dependent packages.
    """

    homepage = "https://github.com/FelixErnst/RNAmodR.Data"
    bioc = "RNAmodR.Data"

    version("1.22.0", commit="34d455ae8117a48bbff1e05d61013a0c52e4e3c0")
    version("1.16.0", commit="0703a7631421c10f58a543e0453c3af17b01af92")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-experimenthubdata@1.9.2:", type=("build", "run"))
