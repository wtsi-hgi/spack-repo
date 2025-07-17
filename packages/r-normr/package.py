# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormr(RPackage):
    """Normalization and difference calling in ChIP-seq data

    Robust normalization and difference calling procedures for ChIP-seq and alike data. Read counts are modeled jointly as a binomial mixture model with a user-specified number of components. A fitted background estimate accounts for the effect of enrichment in certain regions and, therefore, represents an appropriate null hypothesis. This robust background is used to identify significantly enriched or depleted regions.
    """

    homepage = "https://github.com/your-highness/normR"
    bioc = "normr"

    version("1.34.0", commit="7cf57fa24d0c9975b4c5cdcec517eb0341b2af72")
    version("1.28.0", commit="94c7eb2e64aca7de76c4a8a035612573c04a069b")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-qvalue@2.2:", type=("build", "run"))
    depends_on("r-bamsignals@1.4:", type=("build", "run"))
    depends_on("r-rtracklayer@1.32:", type=("build", "run"))
