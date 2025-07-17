# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirage(RPackage):
    """MiRNA Ranking by Gene Expression

    The package contains functions for inferece of target gene regulation by miRNA, based on only target gene expression profile.
    """

    bioc = "MiRaGE"

    version("1.50.0", commit="7757d1c370fa938932f0d44d97590f9284319761")
    version("1.44.0", commit="f54de47baeb470b003c2111ecfdafb3daaac02a8")

    depends_on("r@3.1:", type=("build", "run"))
    depends_on("r-biobase@2.23.3:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
