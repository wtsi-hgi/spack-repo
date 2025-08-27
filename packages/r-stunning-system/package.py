from spack.package import *


class RStunningSystem(RPackage):
    """Stunning System Analysis Tools

    A comprehensive R package for stunning system analysis and data processing.
    Provides tools for analyzing complex systems with stunning visualizations and
    statistical methods."""

    homepage = "https://github.com/Eric-Kobayashi/stunning-system"
    git = "https://github.com/Eric-Kobayashi/stunning-system.git"

    license("MIT")

    # No releases; track latest commit with YYYYMMDD version per guidelines
    version("20250823", commit="547ff15ea0989dac8a889c7e76783a922a45a934")

    # Base R dependency
    depends_on("r@4.0.0:", type=("build", "run"))

    # Runtime imports from DESCRIPTION
    with default_args(type=("build", "run")):
        depends_on("r-dplyr@1.0.0:")
        depends_on("r-data-table@1.14.0:")
        depends_on("r-ggplot2@3.3.0:")
        depends_on("r-magrittr@2.0.0:")
        depends_on("r-stringr@1.4.0:")

    # Optional suggests as variants (default off)
    variant("tests", default=False, description="Enable testthat runtime support")
    depends_on("r-testthat@3.0.0:", type=("build", "run"), when="+tests")

    variant(
        "vignettes",
        default=False,
        description="Enable vignette building (knitr/rmarkdown)",
    )
    depends_on("r-knitr@1.30:", type=("build", "run"), when="+vignettes")
    depends_on("r-rmarkdown@2.5:", type=("build", "run"), when="+vignettes")

