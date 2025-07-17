# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGolubesets(RPackage):
    """exprSets for golub leukemia data

    representation of public golub data with some covariate data of provenance unknown to the maintainer at present; now employs ExpressionSet format
    """

    bioc = "golubEsets"

    version("1.50.0", commit="9ab1c6bfa1cd19c6eb5ccfada4fa33f88266b948")
    version("1.44.0", commit="0c2ab6b2e23bdf9bb7b2a411f7a591514c7e60f2")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
