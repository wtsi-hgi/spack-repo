from spack.package import *


class RStunningSystem(RPackage):
    """Stunning System Analysis Tools. A comprehensive R package for stunning
    system analysis and data processing. Provides tools for analyzing complex
    systems with stunning visualizations and statistical methods."""

    homepage = "https://github.com/Eric-Kobayashi/stunning-system"
    git = "https://github.com/Eric-Kobayashi/stunning-system.git"

    license("MIT")

    # No tagged releases at time of packaging; using latest commit with date.
    version("20250823", commit="547ff15ea0989dac8a889c7e76783a922a45a934")

    # R version
    depends_on("r@4:", type=("build", "run"))

    # Imports
    depends_on("r-dplyr@1.0.0:", type=("build", "run"))
    depends_on("r-data-table@1.14.0:", type=("build", "run"))
    depends_on("r-ggplot2@3.3.0:", type=("build", "run"))
    depends_on("r-magrittr@2.0.0:", type=("build", "run"))
    depends_on("r-stringr@1.4.0:", type=("build", "run"))

    # Suggests (treat as hard deps per repo guidelines for R packages)
    depends_on("r-testthat@3.0.0:", type=("build", "run"))
    depends_on("r-knitr@1.30:", type=("build", "run"))
    depends_on("r-rmarkdown@2.5:", type=("build", "run"))

