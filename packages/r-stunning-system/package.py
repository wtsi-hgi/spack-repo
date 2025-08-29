from spack.package import *


class RStunningSystem(RPackage):
    """Stunning System Analysis Tools.

    A comprehensive R package for stunning system analysis and data processing.
    Provides tools for analyzing complex systems with stunning visualizations
    and statistical methods.
    """

    homepage = "https://github.com/Eric-Kobayashi/stunning-system"
    git = "https://github.com/Eric-Kobayashi/stunning-system.git"

    # MIT + file LICENSE in DESCRIPTION
    license("MIT")

    # No releases; track by latest commit with date-based version id
    version("20250823", commit="547ff15ea0989dac8a889c7e76783a922a45a934")

    # Core dependencies from DESCRIPTION
    depends_on("r@4.0.0:", type=("build", "run"))
    depends_on("r-dplyr@1.0.0:", type=("build", "run"))
    depends_on("r-data-table@1.14.0:", type=("build", "run"))
    depends_on("r-ggplot2@3.3.0:", type=("build", "run"))
    depends_on("r-magrittr@2.0.0:", type=("build", "run"))
    depends_on("r-stringr@1.4.0:", type=("build", "run"))

    # Optional suggestions exposed as variants (default off)
    variant("testthat", default=False, description="Enable tests using testthat")
    variant("knitr", default=False, description="Enable vignette building with knitr")
    variant("rmarkdown", default=False, description="Enable vignette building with rmarkdown")

    depends_on("r-testthat@3.0.0:", when="+testthat", type=("build", "run"))
    depends_on("r-knitr@1.30:", when="+knitr", type=("build", "run"))
    depends_on("r-rmarkdown@2.5:", when="+rmarkdown", type=("build", "run"))

