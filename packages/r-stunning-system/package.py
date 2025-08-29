from spack.package import *


class RStunningSystem(RPackage):
    """Stunning System Analysis Tools

    A comprehensive R package for stunning system analysis and data processing.
    Provides tools for analyzing complex systems with stunning visualizations
    and statistical methods.
    """

    homepage = "https://github.com/Eric-Kobayashi/stunning-system"
    git = "https://github.com/Eric-Kobayashi/stunning-system.git"

    license("MIT")

    # No releases/tags; track by commit/date
    version("20250823", commit="547ff15ea0989dac8a889c7e76783a922a45a934")

    # Optional suggests as variants (default off)
    variant("testthat", default=False, description="Enable suggested dependency r-testthat")
    variant("knitr", default=False, description="Enable suggested dependency r-knitr")
    variant("rmarkdown", default=False, description="Enable suggested dependency r-rmarkdown")

    depends_on("r@4.0.0:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("r-dplyr")
        depends_on("r-data-table")
        depends_on("r-ggplot2")
        depends_on("r-magrittr")
        depends_on("r-stringr")

    # Optional suggests
    depends_on("r-testthat", when="+testthat", type=("build", "run"))
    depends_on("r-knitr", when="+knitr", type=("build", "run"))
    depends_on("r-rmarkdown", when="+rmarkdown", type=("build", "run"))

