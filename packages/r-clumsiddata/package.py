# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClumsiddata(RPackage):
    """Data for the CluMSID package

    This package contains various LC-MS/MS and GC-MS data that is used in vignettes and examples in the CluMSID package.
    """

    bioc = "CluMSIDdata"

    version("1.24.0", commit="0ce1ec45230d04a0cde60066ad18f314a3b9ca26")
    version("1.18.0", commit="d77fe253b8baa46d0d2c56423915c2709fbe28f8")

    depends_on("r@3.6:", type=("build", "run"))
