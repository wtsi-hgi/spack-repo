# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactomegsa(RPackage):
    """Client for the Reactome Analysis Service for comparative multi-omics gene set analysis

    The ReactomeGSA packages uses Reactome's online analysis service to perform a multi-omics gene set analysis. The main advantage of this package is, that the retrieved results can be visualized using REACTOME's powerful webapplication. Since Reactome's analysis service also uses R to perfrom the actual gene set analysis you will get similar results when using the same packages (such as limma and edgeR) locally. Therefore, if you only require a gene set analysis, different packages are more suited.
    """

    homepage = "https://github.com/reactome/ReactomeGSA"
    bioc = "ReactomeGSA"

    version("1.22.0", commit="6e8adbb35bacb6c881b0826b364d39ea1a54f19b")
    version("1.16.1", commit="6785d7ec3c1a32e1b08f84032a285c362c211b4f")

    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-progress", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
