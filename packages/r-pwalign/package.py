# Copyright 2013-2025 Lawrence Livermore National Security, LLC
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwalign(RPackage):
    """Pairwise alignment utilities.

    R wrapper/utilities providing pairwise sequence alignment functionality
    used by MethTargetedNGS.
    """

    cran = "pwalign"
    # Use CRAN Archive for removed packages
    url = "https://cran.r-project.org/src/contrib/Archive/pwalign/pwalign_0.2-4.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/pwalign"

    version("0.2-4", sha256="80ac577d2dc10f4cce6bdb1b5677172cb7e4716eddfb585630e99fe0450e6ee1")

    depends_on("r@3.0:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
