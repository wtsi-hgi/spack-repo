# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFibroeset(RPackage):
    """exprSet for Karaman et al. (2003) fibroblasts data

    exprSet for Karaman et al. (2003) human, bonobo and gorilla fibroblasts data
    """

    bioc = "fibroEset"

    version("1.50.0", commit="f60d51e31c147049d38de665348da2735f1696cb")
    version("1.44.0", commit="1ebe9653cb77365e7ffee2b904cbab032908ed21")

    depends_on("r-biobase@2.5.5:", type=("build", "run"))
