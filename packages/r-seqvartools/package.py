# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqvartools(RPackage):
    """Tools for variant data

    An interface to the fast-access storage format for VCF data provided in SeqArray, with tools for common operations and analysis.
    """

    homepage = "https://github.com/smgogarten/SeqVarTools"
    bioc = "SeqVarTools"

    version("1.46.0", commit="30f2bb3234f21beb9934a9bccf67e7035f2d7981")
    version("1.40.0", commit="1b6957a9fe47a7a971b0410a77108d9f8daa9f46")

    depends_on("r-seqarray", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-gdsfmt", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-gwasexacthw", type=("build", "run"))
    depends_on("r-logistf", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
