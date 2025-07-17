# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebet(RPackage):
    """The subREgion-based BurdEn Test (REBET)

    There is an increasing focus to investigate the association between rare variants and diseases. The REBET package implements the subREgion-based BurdEn Test which is a powerful burden test that simultaneously identifies susceptibility loci and sub-regions.
    """

    bioc = "REBET"

    version("1.26.0", commit="ce98409f9ae0d9906f5020ea74745182869c4e6b")
    version("1.20.0", commit="5ca181cceee6c848fd3871825742025168278542")

    depends_on("r-asset", type=("build", "run"))
