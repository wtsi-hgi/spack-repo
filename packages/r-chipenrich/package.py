# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipenrich(RPackage):
    """Gene Set Enrichment For ChIP-seq Peak Data

    ChIP-Enrich and Poly-Enrich perform gene set enrichment testing using peaks called from a ChIP-seq experiment. The method empirically corrects for confounding factors such as the length of genes, and the mappability of the sequence surrounding genes.
    """

    bioc = "chipenrich"

    version("2.32.0", commit="28602b9471c14667541b05c67bf0e3a96fb807d9")
    version("2.26.0", commit="8330eab5ddf71561ec30de856c824890b5f6feb2")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-chipenrich-data", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-latticeextra", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-mgcv", type=("build", "run"))
    depends_on("r-org-dm-eg-db", type=("build", "run"))
    depends_on("r-org-dr-eg-db", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-org-mm-eg-db", type=("build", "run"))
    depends_on("r-org-rn-eg-db", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-rms", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-s4vectors@0.23.10:", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
