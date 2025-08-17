# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotifbreakr(RPackage):
    """A Package For Predicting The Disruptiveness Of Single Nucleotide Polymorphisms On Transcription Factor Binding Sites

    We introduce motifbreakR, which allows the biologist to judge in the first place whether the sequence surrounding the polymorphism is a good match, and in the second place how much information is gained or lost in one allele of the polymorphism relative to another. MotifbreakR is both flexible and extensible over previous offerings; giving a choice of algorithms for interrogation of genomes with motifs from public sources that users can choose from; these are 1) a weighted-sum probability matrix, 2) log-probabilities, and 3) weighted by relative entropy. MotifbreakR can predict effects for novel or previously described variants in public databases, making it suitable for tasks beyond the scope of its original design. Lastly, it can be used to interrogate any genome curated within Bioconductor (currently there are 32 species, a total of 109 versions).
    """

    bioc = "motifbreakR"

    version("2.22.0", commit="f754fca2e68b21ec3d636d7d68b04b57e93ff283")
    version("2.16.0", commit="741df7f83db5217c36960215bc22ff5367596ceb")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-motifdb", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-motifstack", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-tfmpvalue", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    # Required CRAN UI dependencies referenced by the package
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-bsicons", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
