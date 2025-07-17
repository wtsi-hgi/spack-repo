# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatsconvert(RPackage):
    """Import Data from Various Mass Spectrometry Signal Processing Tools to MSstats Format

    MSstatsConvert provides tools for importing reports of Mass Spectrometry data processing tools into R format suitable for statistical analysis using the MSstats and MSstatsTMT packages.
    """

    bioc = "MSstatsConvert"

    version("1.18.0", commit="1cc2fd51657c567c7b6c4843f94d1bd9174fc260")
    version("1.12.1", commit="4dabc58aff050bbe5ce794be48a06c605c6b3c6a")
    version("1.12.0", md5="1a8b79ba830db5296c2d3f589b398b7f")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-log4r", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
