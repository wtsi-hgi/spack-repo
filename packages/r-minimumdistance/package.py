# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinimumdistance(RPackage):
    """A Package for De Novo CNV Detection in Case-Parent Trios

    Analysis of de novo copy number variants in trios from high-dimensional genotyping platforms.
    """

    bioc = "MinimumDistance"

    version("1.52.1", commit="3c4f502542d7ce53c1e43bca9297de2f07ce3adc")
    version("1.46.0", commit="b1328d88c2df0166c458dc4b41f3bf7d1072cb20")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-vanillaice@1.47.1:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-matrixgenerics", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-s4vectors@0.23.18:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges@1.17.16:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.15.4:", type=("build", "run"))
    depends_on("r-oligoclasses", type=("build", "run"))
    depends_on("r-dnacopy", type=("build", "run"))
    depends_on("r-ff", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
