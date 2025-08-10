from spack.package import *


class RMosdef(RPackage):
    """Run common DE/EA workflow tasks and reporting helpers (Bioconductor 'mosdef')."""

    bioc = "mosdef"

    # Bioconductor DESCRIPTION version
    version("1.5.1", commit="0964a99d45fa4a5bccac056ae78e61a0f3906a2c")

    depends_on("r@4.4:", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-ggplot2@3.5.0:", type=("build", "run"))
    depends_on("r-ggforce", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-topgo", type=("build", "run"))
    depends_on("r-go-db", type=("build", "run"))
    depends_on("r-clusterprofiler", type=("build", "run"))
    depends_on("r-goseq", type=("build", "run"))
    depends_on("r-enrichplot", type=("build", "run"))
