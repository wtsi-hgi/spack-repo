# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgsc(RPackage):
    """Visualizing Single Cell Data

    Useful functions to visualize single cell and spatial data. It supports both 'SingleCellExperiment' and 'Seurat' objects. It also supports visualizing the data using grammar of graphics implemented in 'ggplot2'.
    """

    homepage = "https://github.com/YuLab-SMU/ggsc"
    url = "https://bioconductor.org/packages/release/bioc/src/contrib/ggsc_1.6.1.tar.gz"
    list_url = "https://bioconductor.org/packages/release/bioc/src/contrib/Archive/ggsc"

    version("1.6.1", sha256="238c23bcd36ae5fb2ee2001969c895a2fc4ce78af5372a13bfd9ea339689762b")
    version("1.0.2", commit="67f887190e24b7e641c801a82ee5a1c9fd19e778")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcppparallel", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-scattermore", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-tidydr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-yulab-utils", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))

    def patch(self):
        # Fix build with newer Armadillo: replace as_dense() on SpSubview_row
        filter_file(
            "w.row(i).as_dense()",
            "arma::conv_to<arma::rowvec>::from(arma::mat(w.row(i)))",
            "src/kde.cpp",
            string=True,
        )
