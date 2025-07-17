# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSim(RPackage):
    """Integrated Analysis on two human genomic datasets

    Finds associations between two human genomic datasets.
    """

    bioc = "SIM"

    version("1.78.0", commit="7db6f1681543932e552dffd53045dc5543fe4b6a")
    version("1.72.0", commit="33f72d9b41b1e969f35ee838e30419724c23ccf4")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-quantreg", type=("build", "run"))
    depends_on("r-globaltest", type=("build", "run"))
    depends_on("r-quantsmooth", type=("build", "run"))
