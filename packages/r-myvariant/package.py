# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMyvariant(RPackage):
    """Accesses MyVariant.info variant query and annotation services

    MyVariant.info is a comprehensive aggregation of variant annotation resources. myvariant is a wrapper for querying MyVariant.info services
    """

    bioc = "myvariant"

    version("1.38.0", commit="a28207a43bdff19a30846ccbe8104dcd44572f21")
    version("1.32.0", commit="1555368cb3e7635e3e526b1d77adfd7bdb542474")

    depends_on("r@3.2.1:", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
