# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RJaneaustenr(RPackage):
    """Full texts for Jane Austen's 6 completed novels, ready for text analysis. """

    homepage = "https://github.com/juliasilge/janeaustenr"
    cran = "janeaustenr"

    version("1.0.0", sha256="b4c32ee1395ee4a8efe714c535c0fe578b0dbf5f3bb85b41fa5cc87569b8e8aa")
    version("0.1.5", sha256="992f6673653daf7010fe176993a01cd4127d9a88be428da8da7a28241826d6f3")
    version("0.1.4", sha256="318125445be20af3f2d17c384eec0c27b702d0e8c0823af41b0433cd1449b3fb")
    version("0.1.3", sha256="eaf5a1bd2ca1f8976bd4ca4359ee1d2cbc86453a1291bb7cca849e6fd3ba5fde")
    version("0.1.2", sha256="7078343e1e41ae56e7f18346aef0ff0e6c2826794f183111f48fb979fb9bb368")
    version("0.1.1", sha256="6e2091d8f595ade2593aea5ccb721e01ff35d399496ba7318b9d0e73674162b4")
    version("0.1.0", sha256="1edb97c1dc8f9f5a111883125bf214daf7866ea2ea64fca5c4d6fa63a984ea77")

    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
