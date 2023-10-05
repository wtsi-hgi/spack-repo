# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RPalmerpenguins(RPackage):
    """Size measurements, clutch observations, and blood isotope ratios for adult foraging Adélie, Chinstrap, and Gentoo penguins observed on islands in the Palmer Archipelago near Palmer Station, Antarctica."""

    homepage = "https://allisonhorst.github.io/palmerpenguins/"
    cran = "palmerpenguins"

    version("0.1.1", sha256="2a40d48ba6c7978fdf2a6daf647ccb39cd17590680138931d11194d3dd1a30b4")
    version("0.1.0", sha256="fdcc58bcf1311b962e94b13d0ab3729e4b6656d21bd8f0329f07473a1b1b3360")

    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-recipes", type=("build", "run"))
