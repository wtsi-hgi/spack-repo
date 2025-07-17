# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColonca(RPackage):
    """exprSet for Alon et al. (1999) colon cancer data

    exprSet for Alon et al. (1999) colon cancer data
    """

    bioc = "colonCA"

    version("1.50.0", commit="92f8afdcdfd3354e258e6b3dbbb5d67ec254559c")
    version("1.44.0", commit="70ea91ad7c86822e8af8ee22ee90f80a8189889e")

    depends_on("r-biobase@2.5.5:", type=("build", "run"))
