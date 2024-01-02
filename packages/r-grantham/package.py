# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RGrantham(RPackage):
    """A minimal set of routines to calculate the 'Grantham' distance."""

    homepage = "https://maialab.org/grantham/"
    cran = "grantham"

    version("0.1.1", sha256="e66436d888e64bcac02263e8b383184be4c178dcac2d4bef7ad5d802fde1f330")
    version("0.1.0", sha256="ef3760d8b51c77556e0ab6e780fde5977650b9d12b9a278bc1e841edd61a8831")

    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-vctrs", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
