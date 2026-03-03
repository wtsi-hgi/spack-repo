# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RSceptre(RPackage):
    """sceptre is an R package for single-cell CRISPR screen data analysis, emphasizing statistical rigor, massive scalability, and ease of use."""

    homepage = "https://katsevich-lab.github.io/sceptre/"
    url = "https://github.com/Katsevich-Lab/sceptre/archive/refs/tags/v0.10.1.tar.gz"

    version("0.10.1", sha256="245c17aba7bd694fecea28c0e90bc3d1f8a0ff8c015bb9291cc61a952d14d6de")
    version("0.10.0", sha256="21cc354f7f7e2bfdee2db0d1396fc3705784c8e961dcab4b0dcf32be8c203ad8")
    version("0.9.2", sha256="c1d13f4a5770c20b59b68b7973e62b7ff87d48beba6233e86afbf6396d0267cc")
    version("0.9.1", sha256="6f8360e30c2d48a3bb07038b987ecbea42c6f6b857bdebfca4ea505eb0270511")
    version("0.9.0", sha256="b3b832fbebf25b23216c8fe7cf6806177a143048116e3a2e736b1e1ecf139d04")

    depends_on("r-bh", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-crayon", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
