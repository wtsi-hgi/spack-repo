# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxdbmaker(RPackage):
    """ A set of tools for making TxDb objects from genomic annotations from various sources (e.g. UCSC, Ensembl, and GFF files). These tools allow the user to download the genomic locations of transcripts, exons, and CDS, for a given assembly, and to import them in a TxDb object. TxDb objects are implemented in the GenomicFeatures package, together with flexible methods for extracting the desired features in convenient formats."""

    homepage = "https://bioconductor.org/packages/release/bioc/html/txdbmaker.html"
    url = "https://bioconductor.org/packages/3.22/bioc/src/contrib/txdbmaker_1.6.0.tar.gz"
    bioc = "txdbmaker"

    version("1.6.0", sha256="1746d7d93dd05e87fdde4d04b564f735e48a5d427b56a017dd8231b6ac9d9f65")
    version("1.4.2", sha256="9d5d3d90603a396a4d585cf6d97d887420751bf730d6c19079f1bf01f828acd1", url="https://bioconductor.org/packages/3.21/bioc/src/contrib/txdbmaker_1.4.2.tar.gz")

    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocio", type=("build", "run"))
    depends_on("r-biomart@2.59.1:", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-genomeinfodb@1.39.9:", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-genomicranges@:1.61.0", type=("build", "run"), when="@:1.5.0")
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-rsqlite@2.0:", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-ucsc-utils", type=("build", "run"))
    depends_on("r-genomicfeatures@1.61.4:", type=("build", "run"), when="@1.6.0")
    depends_on("r-genomicranges@1.61.1:", type=("build", "run"), when="@1.6.0")
    depends_on("r-s4vectors@0.47.6:", type=("build", "run"), when="@1.6.0:")
    depends_on("r-seqinfo", type=("build", "run"), when="@1.6.0:")
