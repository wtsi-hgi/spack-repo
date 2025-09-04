# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtmap(RPackage):
    """Two-Tier Mapper: a clustering tool based on topological data analysis

    TTMap is a clustering method that groups together samples with the same
    deviation in comparison to a control group. It is specially useful when the
    data is small. It is parameter free.
    """

    homepage = "https://bioconductor.org/packages/TTMap"
    git = "https://git.bioconductor.org/packages/TTMap.git"

    # Bioconductor 3.18 release corresponds to TTMap 1.24.0
    version("1.24.0", commit="86fdbd0443b1b9f4bc0aa347d738e518b6475d57")

    depends_on("r-rgl", type=("build", "run"))
    depends_on("r-colorramps", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
