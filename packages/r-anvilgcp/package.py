# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnvilgcp(RPackage):
    """The GCP R Client for the AnVIL

    Provides functions to interact with Google Cloud Platform (GCP)
    services on the AnVIL platform. Designed to work with the AnVIL
    package; end-user interaction with this package is typically minimal.
    """

    bioc = "AnVILGCP"

    # Use Bioconductor git commit for this release
    version("1.2.0", commit="1f99346")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-anvilbase", type=("build", "run"))
    depends_on("r-biocbaseutils", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
