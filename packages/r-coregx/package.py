# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoregx(RPackage):
    """Classes and Functions to Serve as the Basis for Other 'Gx' Packages

    A collection of functions and classes which serve as the foundation for our lab's suite of R packages, such as 'PharmacoGx' and 'RadioGx'. This package was created to abstract shared functionality from other lab package releases to increase ease of maintainability and reduce code repetition in current and future 'Gx' suite programs. Major features include a 'CoreSet' class, from which 'RadioSet' and 'PharmacoSet' are derived, along with get and set methods for each respective slot. Additional functions related to fitting and plotting dose response curves, quantifying statistical correlation and calculating area under the curve (AUC) or survival fraction (SF) are included. For more details please see the included documentation, as well as: Smirnov, P., Safikhani, Z., El-Hachem, N., Wang, D., She, A., Olsen, C., Freeman, M., Selby, H., Gendoo, D., Grossman, P., Beck, A., Aerts, H., Lupien, M., Goldenberg, A. (2015) <doi:10.1093/bioinformatics/btv723>. Manem, V., Labie, M., Smirnov, P., Kofia, V., Freeman, M., Koritzinksy, M., Abazeed, M., Haibe-Kains, B., Bratman, S. (2018) <doi:10.1101/449793>.
    """

    bioc = "CoreGx"

    version("2.12.0", commit="df5b149d3101015c6ee0253e8984e3aae2f87cf5")
    version("2.6.1", commit="a9b3365a61a39b91e7b012a9ad73cd9a03f781ae")
    version("2.6.0", md5="3556f412bd014d5294b15feb8342d78e")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-matrixgenerics", type=("build", "run"))
    depends_on("r-piano", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-bumpymatrix", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-lsa", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-crayon", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-bench", type=("build", "run"))
