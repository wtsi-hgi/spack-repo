# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeve2006(RPackage):
    """expression and CGH data on breast cancer cell lines

    Experimental organization of combined expression and CGH data
    """

    bioc = "Neve2006"

    version("0.46.0", commit="90d2c68f50cc971d53c38993691aa81633a1bb73")
    version("0.40.0", commit="3cfc0a9e8b7db4fa889129c19b07fe8286632931")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-biobase@1.14:", type=("build", "run"))
    depends_on("r-hgu133a-db", type=("build", "run"))
    depends_on("r-annotate", type=("build", "run"))
