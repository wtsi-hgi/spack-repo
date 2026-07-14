from spack.package import *


class RTidypolars(RPackage):
    """More efficient tidyverse code, using Polars in the background."""

    homepage = "https://tidypolars.etiennebacher.com/"
    url = "https://github.com/etiennebacher/tidypolars/archive/refs/tags/v0.19.0.tar.gz"
    git = "https://github.com/etiennebacher/tidypolars.git"

    license("MIT")

    version("0.19.0", sha256="07c8d92aa00aa4cda24a380de2be8efb2232846125dcb3246e154d1f2853c714")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-dplyr@1.2:", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"))
    depends_on("r-polars@1.13.0:", type=("build", "run"))
    depends_on("r-rlang@1.1.0:", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
    depends_on("r-vctrs", type=("build", "run"))
