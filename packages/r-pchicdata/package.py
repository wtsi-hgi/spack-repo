# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPchicdata(RPackage):
    """Promoter Capture Hi-C data

    Subsets of Promoter Capture Hi-C data conveniently packaged for Chicago users. Data includes interactions detected for chromosomes 20 and 21 in GM12878 cells and for chromosomes 18 and 19 in mESC.
    """

    bioc = "PCHiCdata"

    version("1.36.0", commit="169ac7b84a498ef4d57d5fe009593dfcc8d29b1d")
    version("1.30.0", commit="95d1911bf586e67a38c33c42565ac667d93cac00")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-chicago", type=("build", "run"))
