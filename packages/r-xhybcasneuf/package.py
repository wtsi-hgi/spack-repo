# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXhybcasneuf(RPackage):
    """EBI/PSB cross-hybridisation study package

    Cross-hybridisation study on the ATH1 Affymetrix GeneChip
    """

    bioc = "XhybCasneuf"

    version("1.46.0", commit="abef7e00e7b0b5cc48570d02f6eebeb026eeac5c")
    version("1.40.0", commit="f5dabde89023e3bba8704c84f59d9f87651cf10a")

    depends_on("r@2.4:", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-ath1121501cdf", type=("build", "run"))
    depends_on("r-tinesath1cdf", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
