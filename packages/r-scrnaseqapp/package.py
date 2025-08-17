# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrnaseqapp(RPackage):
    """A single-cell RNAseq Shiny app-package

    scRNAseqApp is a Shiny app package that allows users to visualize single cell data interactively. It was modified from ShinyCell and repackaged to a tool to show multiple data. It can visulize the data with multiple information side by side.
    """

    homepage = "https://github.com/jianhong/scRNAseqApp"
    bioc = "scRNAseqApp"

    version("1.8.0", commit="2c1da567c04cb5a6691c1692f511a65b7843cf25")
    version("1.2.2", commit="b79269170aecbcea9614ecc43a6906b1fbc32eb7")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-bibtex", type=("build", "run"))
    depends_on("r-bslib", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-colourpicker", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-ggdendro", type=("build", "run"))
    depends_on("r-ggforce", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-ggridges", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-hdf5r", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-refmanager", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-scrypt", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-seuratobject", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinyhelper", type=("build", "run"))
    depends_on("r-shinymanager", type=("build", "run"))
    depends_on("r-slingshot", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-sortable", type=("build", "run"))
    depends_on("r-xfun", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
