# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RImmunarch(RPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    cran = "immunarch"

    version("0.9.0", sha256="fe3adb275fe7d83702319c9a2ceb12c09b70d61422a89b789eb68b32ecc955fa")
    version("0.8.0", sha256="e0289d9b4f62ae8e7d0114d42156a1444f3e3ff450019fca5b170ab0bc52a741")
    version("0.7.0", sha256="dbbd9fc8ef41a44800bffdd98dc61f8ecc96be156901b49ab3524dc781895193")
    version("0.6.9", sha256="0fd096bfab198f082fd06d6df35d41e4b9bb6c8ba85fba4fac3c1a4898510155")
    version("0.6.8", sha256="0b81a38a5678bd93bf1a611b04b79f863e13e743ef3a741a6060a939a1bf4bfb")
    version("0.6.7", sha256="28b5922ac87e5e852b3abcf84f040ced3a97cd52e4847bacd3fc7b69d94069b7")
    version("0.6.6", sha256="64c945bb2e212606f595e47800cd27e6716807eb62011c5a28ffb2abbbccde38")
    version("0.6.5", sha256="2c80a62700130b5f2d862054e4c2ad6538484a50192cf630119bcc3106a9c16f")
    version("0.6.4", sha256="a3d51355f59fa4f9b00147ff161194777bd894ec0388fe293696e32361195ceb")

    depends_on("r@4.0.0:", type=("build", "run"))
    depends_on("r-ggplot2@3.1.0:", type=("build", "run"))
    depends_on("r-dplyr@0.8.0:", type=("build", "run"))
    depends_on("r-dtplyr@1.0.0:", type=("build", "run"))
    depends_on("r-data-table@1.12.6:", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-factoextra@1.0.4:", type=("build", "run"))
    depends_on("r-fpc", type=("build", "run"))
    depends_on("r-upsetr@1.4.0:", type=("build", "run"))
    depends_on("r-pheatmap@1.0.12:", type=("build", "run"))
    depends_on("r-ggrepel@0.8.0:", type=("build", "run"))
    depends_on("r-reshape2@1.4.2:", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-mass@7.3:", type=("build", "run"))
    depends_on("r-rtsne@0.15:", type=("build", "run"))
    depends_on("r-readxl@1.3.1:", type=("build", "run"))
    depends_on("r-shiny@1.4.0:", type=("build", "run"))
    depends_on("r-shinythemes", type=("build", "run"))
    depends_on("r-airr", type=("build", "run"))
    depends_on("r-ggseqlogo", type=("build", "run"))
    depends_on("r-ggalluvial@0.10.0:", type=("build", "run"))
    depends_on("r-rcpp@1.0:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-ggpubr@0.2:", type=("build", "run"))
    depends_on("r-rlang@0.4:", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-stringdist", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-rlist", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-phangorn", type=("build", "run"))
    depends_on("r-uuid", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-ggraph", type=("build", "run"))
