# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeformats(RPackage):
    """Differential gene expression data formats converter

    Convert between different data formats used by differential gene expression analysis tools.
    """

    homepage = "https://github.com/aoles/DEFormats"
    bioc = "DEFormats"

    version("1.36.0", commit="d2171c8176a62cc6bed2dee84983b8ced704ee53")
    version("1.30.0", commit="aeab5ae4cb639ad2f9db9d1d1192eaf56acf520c")

    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-edger@3.13.4:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
