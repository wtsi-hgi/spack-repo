# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNorce(RPackage):
    """NoRCE: Noncoding RNA Sets Cis Annotation and Enrichment

    While some non-coding RNAs (ncRNAs) are assigned critical regulatory roles, most remain functionally uncharacterized. This presents a challenge whenever an interesting set of ncRNAs needs to be analyzed in a functional context. Transcripts located close-by on the genome are often regulated together. This genomic proximity on the sequence can hint to a functional association. We present a tool, NoRCE, that performs cis enrichment analysis for a given set of ncRNAs. Enrichment is carried out using the functional annotations of the coding genes located proximal to the input ncRNAs. Other biologically relevant information such as topologically associating domain (TAD) boundaries, co-expression patterns, and miRNA target prediction information can be incorporated to conduct a richer enrichment analysis. To this end, NoRCE includes several relevant datasets as part of its data repository, including cell-line specific TAD boundaries, functional gene sets, and expression data for coding & ncRNAs specific to cancer. Additionally, the users can utilize custom data files in their investigation. Enrichment results can be retrieved in a tabular format or visualized in several different ways. NoRCE is currently available for the following species: human, mouse, rat, zebrafish, fruit fly, worm, and yeast.
    """

    bioc = "NoRCE"

    version("1.20.0", commit="1384c443a7c90b87fd002a0d003aab0c6f00ed30")
    version("1.14.0", commit="3c4a8293535aabf461e9bf5c58ea093658340afc")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-keggrest", type=("build", "run"))
    depends_on("r-png", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-reactome-db", type=("build", "run"))
    depends_on("r-rwikipathways", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-dbplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-zlibbioc", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
