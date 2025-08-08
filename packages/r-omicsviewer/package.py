from spack.package import *


class ROmicsviewer(RPackage):
    """
    Interactive and explorative visualization of SummarizedExperssionSet or
    ExpressionSet using omicsViewer.
    """

    homepage = "https://github.com/mengchen18/omicsViewer"
    git      = "https://git.bioconductor.org/packages/omicsViewer"

    version("1.12.0", commit="14dd3bd12818893e833647fa4ee767ccc8e8615b")

    # Core R
    depends_on("r@4.2:", type=("build", "run"))

    # Imports listed in DESCRIPTION
    depends_on("r-survminer", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-fastmatch", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-beeswarm", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinythemes", type=("build", "run"))
    depends_on("r-shinywidgets", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-networkd3", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-fgsea", type=("build", "run"))
    depends_on("r-openxlsx", type=("build", "run"))
    depends_on("r-psych", type=("build", "run"))
    depends_on("r-shinybusy", type=("build", "run"))
    depends_on("r-ggseqlogo", type=("build", "run"))
    depends_on("r-htmlwidgets", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-flatxml", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-shinycssloaders", type=("build", "run"))
    depends_on("r-rocr", type=("build", "run"))

    # Missing in upstream recipe but required by DESCRIPTION
    depends_on("r-drc", type=("build", "run"))
