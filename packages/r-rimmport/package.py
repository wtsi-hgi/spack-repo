# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRimmport(RPackage):
    """RImmPort: Enabling Ready-for-analysis Immunology Research Data

    The RImmPort package simplifies access to ImmPort data for analysis in the R environment. It provides a standards-based interface to the ImmPort study data that is in a proprietary format.
    """

    homepage = "http://bioconductor.org/packages/RImmPort/"
    bioc = "RImmPort"

    version("1.36.0", commit="3fff86d97582c7368cdd0901de444751abbdd265")
    version("1.30.0", commit="9018732c79ef4f9cbb3dad71e207efcb36b49f0c")

    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-sqldf", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
