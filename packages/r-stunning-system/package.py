# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStunningSystem(RPackage):
    """Stunning System Analysis Tools

    An R package providing tools for analyzing complex systems with
    visualizations and statistical methods.
    """

    homepage = "https://github.com/Eric-Kobayashi/stunning-system"
    git = "https://github.com/Eric-Kobayashi/stunning-system.git"

    license("MIT")

    # No releases; track by commit date + full commit hash
    version(
        "20250823",
        commit="547ff15ea0989dac8a889c7e76783a922a45a934",
    )

    # Core R dependency
    depends_on("r@4.0.0:", type=("build", "run"))

    # Imports from DESCRIPTION (runtime requirements)
    with default_args(type=("build", "run")):
        depends_on("r-dplyr@1.0.0:")
        depends_on("r-data-table@1.14.0:")
        depends_on("r-ggplot2@3.3.0:")
        depends_on("r-magrittr@2.0.0:")
        depends_on("r-stringr@1.4.0:")

    # Optional/suggested features as variants (disabled by default)
    variant("tests", default=False, description="Enable testthat dependency")
    variant("knitr", default=False, description="Enable vignette building with knitr")
    variant("rmarkdown", default=False, description="Enable vignette building with rmarkdown")

    with default_args(type=("build", "run")):
        depends_on("r-testthat@3.0.0:", when="+tests")
        depends_on("r-knitr@1.30:", when="+knitr")
        depends_on("r-rmarkdown@2.5:", when="+rmarkdown")

