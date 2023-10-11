# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class REgg(RPackage):
    """Miscellaneous functions to help customise 'ggplot2' objects."""

    cran = "egg"

    version("0.4.5", sha256="15c8ba7cf2676eb0460de7e5dfbc89fc3175ac22a8869cfd44d66d156fd6c7bb")
    version("0.4.2", sha256="deda008e8aabce9bfbb50b725f390f28a50fb54962f5cc754d45760745461846")
    version("0.4.0", sha256="b6dab7fdab4154f3877f55807a138f63d5941bff1ceb9e3b32bd34b9b920f187")
    version("0.2.0", sha256="b29c954739ce42ab498619ed9ae4c637400cc2ca70b39e23e5ef4f7597ed660e")

    depends_on("r-gridextra@2.3:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gtable", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-png", type=("build", "run"))
