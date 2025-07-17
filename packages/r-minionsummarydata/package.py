# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinionsummarydata(RPackage):
    """Summarised MinION sequencing data published by Ashton et al. 2015

    Summarised MinION sequencing data for Salmonella Typhi published by Ashton et al. in 2015. Three replicate runs are each provided as Fast5Summary objects.
    """

    bioc = "minionSummaryData"

    version("1.38.0", commit="01f179b8f51fad196254ecfb1580fb35b9e60300")
    version("1.32.0", commit="c5efcc288603153f51d2bdb15073cb8cfd205302")

    depends_on("r@3.2:", type=("build", "run"))
