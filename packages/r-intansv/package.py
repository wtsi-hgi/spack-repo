# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntansv(RPackage):
    """Integrative analysis of structural variations

    This package provides efficient tools to read and integrate structural variations predicted by popular softwares. Annotation and visulation of structural variations are also implemented in the package.
    """

    bioc = "intansv"

    version("1.48.0", commit="0595695c47d22e3ac947ac9adea02a6a520af651")
    version("1.42.0", commit="7e3a7251c49ca69a4c7a13b8804bd2d83e292b68")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-ggbio", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
