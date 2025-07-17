# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsa2dist(RPackage):
    """MSA2dist calculates pairwise distances between all sequences of a DNAStringSet or a AAStringSet using a custom score matrix and conducts codon based analysis

    MSA2dist calculates pairwise distances between all sequences of a DNAStringSet or a AAStringSet using a custom score matrix and conducts codon based analysis. It uses scoring matrices to be used in these pairwise distance calcualtions which can be adapted to any scoring for DNA or AA characters. E.g. by using literal distances MSA2dist calculates pairwise IUPAC distances.
    """

    homepage = "https://gitlab.gwdg.de/mpievolbio-it/MSA2dist"
    bioc = "MSA2dist"

    version("1.12.0", commit="d7a8634defc569af6557bb350e6e392b42f8d161")
    version("1.6.0", commit="c88df72118c7639191c8be67515187bfde898d5f")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-seqinr", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-rcppthread", type=("build", "run"))
