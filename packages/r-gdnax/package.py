# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdnax(RPackage):
    """Diagnostics for assessing genomic DNA contamination in RNA-seq data

    Provides diagnostics for assessing genomic DNA contamination in RNA-seq data, as well as plots representing these diagnostics. Moreover, the package can be used to get an insight into the strand library protocol used and, in case of strand-specific libraries, the strandedness of the data. Furthermore, it provides functionality to filter out reads of potential gDNA origin.
    """

    homepage = "https://github.com/functionalgenomics/gDNAx"
    bioc = "gDNAx"

    version("1.6.1", commit="a0f4a5f064d9bf0d318a4a584530727bf8f1e394")
    version("1.0.2", commit="0fb296997c1f49537fbca39ec7f690ebb890dda5")
    version("1.0.1", md5="4f51a23263fff85c936d0319a2c0e1de")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicfiles", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-bitops", type=("build", "run"))
    depends_on("r-plotrix", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
