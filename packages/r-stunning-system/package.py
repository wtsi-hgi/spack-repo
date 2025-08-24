from spack.package import *


class RStunningSystem(RPackage):
    """Stunning System Analysis Tools in R.

    Provides tools for analyzing complex systems with visualizations and
    statistical methods.
    """

    homepage = "https://github.com/Eric-Kobayashi/stunning-system"
    git = "https://github.com/Eric-Kobayashi/stunning-system.git"

    license("MIT")

    # No releases/tags; use latest commit with date-based version.
    version("20250823", commit="547ff15ea0989dac8a889c7e76783a922a45a934")

    # Core R requirement
    depends_on("r@4.0.0:", type=("build", "run"))

    # Runtime imports from DESCRIPTION
    with default_args(type=("build", "run")):
        depends_on("r-dplyr@1.0.0:")
        depends_on("r-data-table@1.14.0:")
        depends_on("r-ggplot2@3.3.0:")
        depends_on("r-magrittr@2.0.0:")
        depends_on("r-stringr@1.4.0:")

    # Optional features from Suggests
    variant("vignettes", default=False, description="Build vignettes and docs")
    depends_on("r-knitr@1.30:", when="+vignettes", type=("build", "run"))
    depends_on("r-rmarkdown@2.5:", when="+vignettes", type=("build", "run"))

    variant("tests", default=False, description="Enable test dependencies")
    depends_on("r-testthat@3.0.0:", when="+tests", type=("build", "run"))

