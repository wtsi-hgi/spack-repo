# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdcrnatools(RPackage):
    """GDCRNATools: an R/Bioconductor package for integrative analysis of lncRNA, mRNA, and miRNA data in GDC

    This is an easy-to-use package for downloading, organizing, and integrative analyzing RNA expression data in GDC with an emphasis on deciphering the lncRNA-mRNA related ceRNA regulatory network in cancer. Three databases of lncRNA-miRNA interactions including spongeScan, starBase, and miRcode, as well as three databases of mRNA-miRNA interactions including miRTarBase, starBase, and miRcode are incorporated into the package for ceRNAs network construction. limma, edgeR, and DESeq2 can be used to identify differentially expressed genes/miRNAs. Functional enrichment analyses including GO, KEGG, and DO can be performed based on the clusterProfiler and DO packages. Both univariate CoxPH and KM survival analyses of multiple genes can be implemented in the package. Besides some routine visualization functions such as volcano plot, bar plot, and KM plot, a few simply shiny apps are developed to facilitate visualization of results on a local webpage.
    """

    bioc = "GDCRNATools"

    version("1.28.0", commit="dd6735490b69e16d2fddd8716b2e4ec98c73b873")
    version("1.22.0", commit="6d2fd313aa616f150fad4237999f498174546efe")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-clusterprofiler", type=("build", "run"))
    depends_on("r-dose", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-survminer", type=("build", "run"))
    depends_on("r-pathview", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-genomicdatacommons", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
