# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install r-epiregulon
#
# You can edit this file again by typing:
#
#     spack edit r-epiregulon
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class REpiregulon(RPackage):
    """Gene regulatory network inference from single cell epigenomic data.

    Gene regulatory networks model the underlying gene regulation hierarchies
    that drive gene expression and observed phenotypes. Epiregulon infers TF
    activity in single cells by constructing a gene regulatory network (regulons).
    This is achieved through integration of scATAC-seq and scRNA-seq data and
    incorporation of public bulk TF ChIP-seq data. Links between regulatory
    elements and their target genes are established by computing correlations
    between chromatin accessibility and gene expressions."""

    homepage = "https://github.com/xiaosaiyao/epiregulon/"
    git = "https://github.com/xiaosaiyao/epiregulon.git"
    urls = [
        "https://www.bioconductor.org/packages/release/bioc/src/contrib/epiregulon_1.2.0.tar.gz",
        "https://www.bioconductor.org/packages/3.20/bioc/src/contrib/Archive/epiregulon/epiregulon_1.2.0.tar.gz",
    ]
    bioc = "epiregulon"

    license("MIT")

    version("2.0.1", commit="3d373ab2f2337832866ab234410b1c68e8b5bada")
    version("1.4.0", tag="RELEASE_3_21")
    version("1.2.0", sha256="5b81475a4bb2d1e0ad3f22e3996e7d024fddb566074e30ac49071bbaa10b596e")

    # Depends
    depends_on("r@4.4:", when="@2.0.1:", type=("build", "run"))
    depends_on("r@4.4:", when="@:1", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))

    # Imports
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-bluster", when="@:1", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-entropy", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
    depends_on("r-scuttle", type=("build", "run"))
    depends_on("r-scmultiome", when="@:1", type=("build", "run"))
    depends_on("r-scmultiome", when="@2.0.1:", type=("build"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-aucell", when="@:1", type=("build", "run"))
    depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
    depends_on("r-bsgenome-hsapiens-ucsc-hg38", type=("build", "run"))
    depends_on("r-bsgenome-mmusculus-ucsc-mm10", type=("build", "run"))
    depends_on("r-motifmatchr", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-beachmat", when="@:1", type=("build", "run"))
    depends_on("r-assorthead", when="@:1", type=("build", "run"))
    depends_on("r-scrapper", when="@2.0.1:", type=("build", "run"))

    # Suggests
    depends_on("r-knitr", type=("build"))
    depends_on("r-rmarkdown", type=("build"))
    depends_on("r-biocstyle", type=("build"))
    depends_on("r-testthat@3.0.0:", type=("build"))
    depends_on("r-coin", type=("build"))
    depends_on("r-scater", type=("build"))
    depends_on("r-beachmat-hdf5", when="@:1", type=("build"))

    def patch(self):
        if self.spec.satisfies("@2.0.1:"):
            filter_file("R (>= 4.5.0)", "R (>= 4.4.0)", "DESCRIPTION", string=True)
