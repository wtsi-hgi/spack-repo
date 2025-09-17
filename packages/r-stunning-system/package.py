from spack.package import *


class RStunningSystem(RPackage):
    """Stunning System Analysis Tools.

    A comprehensive R package for system analysis and data processing, providing
    tools for visualizations and statistical methods.
    """

    homepage = "https://github.com/Eric-Kobayashi/stunning-system"
    git = "https://github.com/Eric-Kobayashi/stunning-system.git"

    license("MIT")

    # No releases/tags upstream; track by commit (date-based version id)
    version("20250823", commit="547ff15ea0989dac8a889c7e76783a922a45a934")

    # Core dependency
    depends_on("r@4.0.0:", type=("build", "run"))

    # Imports listed in DESCRIPTION
    with default_args(type=("build", "run")):
        depends_on("r-dplyr@1.0.0:")
        depends_on("r-data-table@1.14.0:")
        depends_on("r-ggplot2@3.3.0:")
        depends_on("r-magrittr@2.0.0:")
        depends_on("r-stringr@1.4.0:")

