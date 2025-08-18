# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTerratcgadata(RPackage):
    """OpenAccess TCGA Data on Terra as MultiAssayExperiment

    Leverage the existing open access TCGA data on Terra with well-established Bioconductor infrastructure. Make use of the Terra data model without learning its complexities. With a few functions, you can copy / download and generate a MultiAssayExperiment from the TCGA example workspaces provided by Terra.
    """

    homepage = "https://github.com/waldronlab/terraTCGAdata"
    bioc = "terraTCGAdata"

    version("1.12.0", commit="1b3a559ecbe676429b6b5f060fe6b7048d3b439a")
    version("1.6.0", commit="4cdd117f578777521d196a66e5494fd31891b308")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-anvil", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-raggedexperiment", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tcgautils", type=("build", "run"))
    # Required by upstream DESCRIPTION (AnVILGCP)
    depends_on("r-anvilgcp", type=("build", "run"))
