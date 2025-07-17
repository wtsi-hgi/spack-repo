# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeriodicdna(RPackage):
    """Set of tools to identify periodic occurrences of k-mers in DNA sequences

    This R package helps the user identify k-mers (e.g. di- or tri-nucleotides) present periodically in a set of genomic loci (typically regulatory elements). The functions of this package provide a straightforward approach to find periodic occurrences of k-mers in DNA sequences, such as regulatory elements. It is not aimed at identifying motifs separated by a conserved distance; for this type of analysis, please visit MEME website.
    """

    homepage = "https://github.com/js2264/periodicDNA"
    bioc = "periodicDNA"

    version("1.18.0", commit="1ba030b8c42aa66d7304b31df5b63df73eb5da90")
    version("1.12.0", commit="70bd9f45550be0c7ed144ad48b97b5e640d8d997")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-zoo", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
