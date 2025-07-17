# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlp(RPackage):
    """Mean Log P Analysis

    Pathway analysis based on p-values associated to genes from a genes expression analysis of interest. Utility functions enable to extract pathways from the Gene Ontology Biological Process (GOBP), Molecular Function (GOMF) and Cellular Component (GOCC), Kyoto Encyclopedia of Genes of Genomes (KEGG) and Reactome databases. Methodology, and helper functions to display the results as a table, barplot of pathway significance, Gene Ontology graph and pathway significance are available.
    """

    bioc = "MLP"

    version("1.56.0", commit="8183b53da0a9211aad6e151a325a56e62a18ef9a")
    version("1.50.0", commit="aa5a0400d818c795ea9a926a99b99fc0bc46a0d1")

    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
