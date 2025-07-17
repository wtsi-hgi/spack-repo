# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpimutacions(RPackage):
    """Robust outlier identification for DNA methylation data

    The package includes some statistical outlier detection methods for epimutations detection in DNA methylation data. The methods included in the package are MANOVA, Multivariate linear models, isolation forest, robust mahalanobis distance, quantile and beta. The methods compare a case sample with a suspected disease against a reference panel (composed of healthy individuals) to identify epimutations in the given case sample. It also contains functions to annotate and visualize the identified epimutations.
    """

    homepage = "https://github.com/isglobal-brge/epimutacions"
    bioc = "epimutacions"

    version("1.12.0", commit="148d72e490236cabd3750c8754f4babed3275301")
    version("1.6.1", commit="ba2e314657d34e9198984423a3e808df8ec3d36f")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-epimutacionsdata", type=("build", "run"))
    depends_on("r-minfi", type=("build", "run"))
    depends_on("r-bumphunter", type=("build", "run"))
    depends_on("r-isotree", type=("build", "run"))
    depends_on("r-robustbase", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-homo-sapiens", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
    depends_on("r-txdb-hsapiens-ucsc-hg18-knowngene", type=("build", "run"))
    depends_on("r-txdb-hsapiens-ucsc-hg38-knowngene", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ensembldb", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-illuminahumanmethylation450kmanifest", type=("build", "run"))
    depends_on("r-illuminahumanmethylationepicmanifest", type=("build", "run"))
    depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))
    depends_on("r-illuminahumanmethylationepicanno-ilm10b2-hg19", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
