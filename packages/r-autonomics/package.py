# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutonomics(RPackage):
    """Generifying and intuifying cross-platform omics analysis

    This package offers a generic and intuitive solution for cross-platform omics data analysis. It has functions for import, preprocessing, exploration, contrast analysis and visualization of omics data. It follows a tidy, functional programming paradigm.
    """

    homepage = "https://github.com/bhagwataditya/autonomics"
    bioc = "autonomics"

    version("1.16.0", commit="a47f4dfc03db39c7572e0a631bf337f79258d9a3")
    version("1.10.2", commit="230045ce836fff0167aa01b664ccc4ea6c3c4631")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-abind", type=("build", "run"))
    depends_on("r-assertive-base", type=("build", "run"))
    depends_on("r-assertive-files", type=("build", "run"))
    depends_on("r-assertive-numbers", type=("build", "run"))
    depends_on("r-assertive-sets", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-bit64", type=("build", "run"))
    depends_on("r-colorspace", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-pcamethods", type=("build", "run"))
    depends_on("r-rappdirs", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-readxl", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
