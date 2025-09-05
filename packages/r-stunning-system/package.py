from spack.package import *


class RStunningSystem(RPackage):
    """Stunning System Analysis Tools.

    A comprehensive R package for stunning system analysis and data
    processing. Provides tools for analyzing complex systems with
    stunning visualizations and statistical methods.
    """

    homepage = "https://github.com/Eric-Kobayashi/stunning-system"
    git = "https://github.com/Eric-Kobayashi/stunning-system.git"

    license("MIT")

    # No releases; track latest commit dated 2025-08-23
    version("20250823", commit="547ff15ea0989dac8a889c7e76783a922a45a934")

    # R version per DESCRIPTION: Depends: R (>= 4.0.0)
    depends_on("r@4.0.0:", type=("build", "run"))

    # Imports
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))

    # Suggests (use all optional deps for R packages)
    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))

