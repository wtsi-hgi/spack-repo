# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCexor(RPackage):
    """An R package to uncover high-resolution protein-DNA interactions in ChIP-exo replicates

    Strand specific peak-pair calling in ChIP-exo replicates. The cumulative Skellam distribution function is used to detect significant normalised count differences of opposed sign at each DNA strand (peak-pairs). Then, irreproducible discovery rate for overlapping peak-pairs across biological replicates is computed.
    """

    bioc = "CexoR"

    version("1.46.0", commit="044e130f5c10fe9ba98612bdf0ddf85b44a256a5")
    version("1.40.0", commit="0eb2404b204f223947f48347d011bff8f858f618")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-idr", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-genomation", type=("build", "run"))
