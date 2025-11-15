# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStunningSystem(RPackage):
    """Stunning System Analysis Tools

    Toolkit for analyzing complex systems with visualization and statistical
    workflows.
    """

    homepage = "https://github.com/Eric-Kobayashi/stunning-system"
    git = "https://github.com/Eric-Kobayashi/stunning-system.git"

    license("MIT")

    version("20250823", commit="547ff15ea0989dac8a889c7e76783a922a45a934")

    depends_on("r@4.0.0:", type=("build", "run"))
    depends_on("r-dplyr@1.0.0:", type=("build", "run"))
    depends_on("r-data-table@1.14.0:", type=("build", "run"))
    depends_on("r-ggplot2@3.3.0:", type=("build", "run"))
    depends_on("r-magrittr@2.0.0:", type=("build", "run"))
    depends_on("r-stringr@1.4.0:", type=("build", "run"))
