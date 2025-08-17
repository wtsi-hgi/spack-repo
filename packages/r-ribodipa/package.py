# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRibodipa(RPackage):
    """Differential pattern analysis for Ribo-seq data

    This package performs differential pattern analysis for Ribo-seq data. It identifies genes with significantly different patterns in the ribosome footprint between two conditions. RiboDiPA contains five major components including bam file processing, P-site mapping, data binning, differential pattern analysis and footprint visualization.
    """

    bioc = "RiboDiPA"

    version("1.16.0", commit="6888e6d47207295cf23654a6d4422f2b83813c24")
    version("1.10.0", commit="bb0b2d94e87b73fefbcfd9b18ea159ffa70c9664")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    # Required for building TxDb objects used by RiboDiPA
    depends_on("r-txdbmaker", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-elitism", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-reldist", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-qvalue", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
