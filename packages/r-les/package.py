# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLes(RPackage):
    """Identifying Differential Effects in Tiling Microarray Data

    The 'les' package estimates Loci of Enhanced Significance (LES) in tiling microarray data. These are regions of regulation such as found in differential transcription, CHiP-chip, or DNA modification analysis. The package provides a universal framework suitable for identifying differential effects in tiling microarray data sets, and is independent of the underlying statistics at the level of single probes.
    """

    bioc = "les"

    version("1.58.0", commit="b6c75988acbdbcf95aac59a0c03f146a2dae84bd")
    version("1.52.0", commit="0c480dceacbaadb66489dcba76fe329c80b3de06")

    depends_on("r@2.13.2:", type=("build", "run"))
    depends_on("r-fdrtool", type=("build", "run"))
    depends_on("r-boot", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
