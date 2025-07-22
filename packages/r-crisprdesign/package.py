# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprdesign(RPackage):
    """Comprehensive design of CRISPR gRNAs for nucleases and base editors

    Provides a comprehensive suite of functions to design and annotate CRISPR guide RNA (gRNAs) sequences. This includes on- and off-target search, on-target efficiency scoring, off-target scoring, full gene and TSS contextual annotations, and SNP annotation (human only). It currently support five types of CRISPR modalities (modes of perturbations): CRISPR knockout, CRISPR activation, CRISPR inhibition, CRISPR base editing, and CRISPR knockdown. All types of CRISPR nucleases are supported, including DNA- and RNA-target nucleases such as Cas9, Cas12a, and Cas13d. All types of base editors are also supported. gRNA design can be performed on reference genomes, transcriptomes, and custom DNA and RNA sequences. Both unpaired and paired gRNA designs are enabled.
    """

    homepage = "https://github.com/crisprVerse/crisprDesign"
    bioc = "crisprDesign"

    version("1.10.0", commit="30df11a48f5a1647b94d563793d8f39ae354faef")
    version("1.4.0", commit="47405b3ceddea0d2bd1854a8f5d27c737ff40c8b")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-crisprbase@1.1.3:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-crisprbowtie@0.99.8:", type=("build", "run"))
    depends_on("r-crisprscore@1.1.6:", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-genomicranges@1.38:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-matrixgenerics", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
