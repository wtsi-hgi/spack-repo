from spack.package import *


class RStunningSystem(RPackage):
    """Stunning System Analysis Tools.

    A comprehensive R package for stunning system analysis and data
    processing. Provides tools for analyzing complex systems with
    visualizations and statistical methods.
    """

    homepage = "https://github.com/Eric-Kobayashi/stunning-system"
    git = "https://github.com/Eric-Kobayashi/stunning-system.git"

    license("MIT")

    # No releases; track latest commit using date-based version id
    version("20250823", commit="547ff15ea0989dac8a889c7e76783a922a45a934")

    # Core requirements from DESCRIPTION
    depends_on("r@4.0.0:", type=("build", "run"))
    depends_on("r-dplyr@1.0.0:", type=("build", "run"))
    depends_on("r-data-table@1.14.0:", type=("build", "run"))
    depends_on("r-ggplot2@3.3.0:", type=("build", "run"))
    depends_on("r-magrittr@2.0.0:", type=("build", "run"))
    depends_on("r-stringr@1.4.0:", type=("build", "run"))

    # Optional (Suggests) as variants disabled by default
    variant("test", default=False, description="Enable test dependencies")
    variant("docs", default=False, description="Enable vignette/documentation dependencies")

    with when("+test"):
        depends_on("r-testthat@3.0.0:", type=("build", "run"))

    with when("+docs"):
        depends_on("r-knitr@1.30:", type=("build", "run"))
        depends_on("r-rmarkdown@2.5:", type=("build", "run"))

