# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpaanalyze(RPackage):
    """Retrieve and analyze data from the Human Protein Atlas

    Provide functions for retrieving, exploratory analyzing and visualizing the Human Protein Atlas data.
    """

    homepage = "https://github.com/anhtr/HPAanalyze"
    bioc = "HPAanalyze"

    version("1.26.1", commit="a412daaa6259ed7bc328f632f03bd1e1b5787d4a")
    version("1.20.0", commit="d0249905867ca73bd370a5993836a326f1bcc63e")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-openxlsx", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
