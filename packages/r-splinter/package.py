# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplinter(RPackage):
    """Splice Interpreter of Transcripts

    Provides tools to analyze alternative splicing sites, interpret outcomes based on sequence information, select and design primers for site validiation and give visual representation of the event to guide downstream experiments.
    """

    homepage = "https://github.com/dianalow/SPLINTER/"
    bioc = "SPLINTER"

    version("1.34.0", commit="f02d50248c8c7cb441829029322762e019bfc412")
    version("1.28.0", commit="501b0f955fb3526988fcecee2df5be6bf91834e7")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-seqlogo", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-bsgenome-mmusculus-ucsc-mm9", type=("build", "run"))
    depends_on("r-googlevis", type=("build", "run"))
