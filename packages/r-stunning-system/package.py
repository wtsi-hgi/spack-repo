from spack.package import *


class RStunningSystem(RPackage):
    """Stunning System Analysis Tools."""

    homepage = "https://github.com/Eric-Kobayashi/stunning-system"
    git = "https://github.com/Eric-Kobayashi/stunning-system.git"

    version("20250823", commit="547ff15ea0989dac8a889c7e76783a922a45a934")

    depends_on("r@4.0:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
