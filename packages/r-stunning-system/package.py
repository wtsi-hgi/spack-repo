# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

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

    # No tagged releases; use latest commit with YYYYMMDD version.
    version("20250823", commit="547ff15ea0989dac8a889c7e76783a922a45a934")

    # Core R requirement
    depends_on("r@4.0.0:", type=("build", "run"))

    # Required imports
    with default_args(type=("build", "run")):
        depends_on("r-dplyr@1.0.0:")
        depends_on("r-data-table@1.14.0:")
        depends_on("r-ggplot2@3.3.0:")
        depends_on("r-magrittr@2.0.0:")
        depends_on("r-stringr@1.4.0:")

    # Optional suggests as variants (default off)
    variant("tests", default=False, description="Enable suggested test dependencies (testthat)")
    variant("vignettes", default=False, description="Enable vignette build deps (knitr, rmarkdown)")

    depends_on("r-testthat@3.0.0:", when="+tests", type=("build", "run"))
    depends_on("r-knitr@1.30:", when="+vignettes", type=("build", "run"))
    depends_on("r-rmarkdown@2.5:", when="+vignettes", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        # Basic import test to validate install
        with working_dir("spack-test", create=True):
            R("-q", "-e", "library(stunningSystem)")

