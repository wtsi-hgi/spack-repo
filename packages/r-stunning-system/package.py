from spack.package import *


class RStunningSystem(RPackage):
    """Stunning System Analysis Tools."""

    cran = "stunningSystem"
    git = "https://github.com/Eric-Kobayashi/stunning-system.git"

    version("20250823", commit="547ff15ea0989dac8a889c7e76783a922a45a934")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-dplyr@1.0:", type=("build", "run"))
    depends_on("r-data-table@1.14:", type=("build", "run"))
    depends_on("r-ggplot2@3.3:", type=("build", "run"))
    depends_on("r-magrittr@2.0:", type=("build", "run"))
    depends_on("r-stringr@1.4:", type=("build", "run"))

