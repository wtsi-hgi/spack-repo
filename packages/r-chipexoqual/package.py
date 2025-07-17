# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipexoqual(RPackage):
    """ChIPexoQual

    Package with a quality control pipeline for ChIP-exo/nexus data.
    """

    homepage = "https:github.com/keleslab/ChIPexoQual"
    bioc = "ChIPexoQual"

    version("1.32.0", commit="1b97d57dca541b287aedcc7351c98b88b50ced5a")
    version("1.26.0", commit="fb1b0847bc43ce1707bcff6e61987ce7b005ca1b")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicalignments@1.0.1:", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-genomicranges@1.14.4:", type=("build", "run"))
    depends_on("r-ggplot2@1:", type=("build", "run"))
    depends_on("r-data-table@1.9.6:", type=("build", "run"))
    depends_on("r-rsamtools@1.16.1:", type=("build", "run"))
    depends_on("r-iranges@1.6:", type=("build", "run"))
    depends_on("r-s4vectors@0.8:", type=("build", "run"))
    depends_on("r-biovizbase@1.18:", type=("build", "run"))
    depends_on("r-broom@0.4:", type=("build", "run"))
    depends_on("r-rcolorbrewer@1.1:", type=("build", "run"))
    depends_on("r-dplyr@0.5:", type=("build", "run"))
    depends_on("r-scales@0.4:", type=("build", "run"))
    depends_on("r-viridis@0.3:", type=("build", "run"))
    depends_on("r-hexbin@1.27:", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
