# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignac(RPackage):
    """Analysis of Single-Cell Chromatin Data.

    A framework for the analysis and exploration of single-cell chromatin data.
    The 'Signac' package contains functions for quantifying single-cell
    chromatin data, computing per-cell quality control metrics, dimension
    reduction and normalization, visualization, and DNA sequence motif
    analysis. Reference: Stuart et al. (2021)
    <doi:10.1038/s41592-021-01282-5>."""

    homepage = "https://github.com/stuart-lab/signac"
    git = "https://github.com/stuart-lab/signac.git"
    url = "https://github.com/stuart-lab/signac/archive/refs/tags/1.16.0.tar.gz"

    license("MIT")

    version("1.16.0", sha256="3e0ee08373b091b9e988e26346d00ccf33f535aae43768e01278d8f0dc5278ed")
    version("1.15.0", sha256="9d9889631656b6af80a8cc9a25b9f37c614ee214c2a2582ccb36e582bbeeddc3")
    version("1.14.0", sha256="772ca2a1abe533d6a90a5dd32113099b0155e4ef6fecb8e727e2b26866f4f1b7")
    version("1.9.0", sha256="3f9090e127946bd498e42db959a4e3000db8907aa5e5c73ba46bc949389825df")
    version("1.8.0", sha256="954e01a166fc60222672b95bc97ee0e059e3a00cbb373de6bf513b9e1f0913ce")
    version("1.7.0", sha256="58d5195c380ac204b9e1995a606215b9852085f7e7b7d6d2f25d984e612005e4")

    depends_on("r@4.0.0:", type=("build", "run"))
    depends_on("r@4.1.0:", type=("build", "run"), when="@1.14.0:")
    depends_on("r-genomeinfodb@1.29.3:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-seuratobject@4.0.0:", type=("build", "run"))
    depends_on("r-seuratobject@5.0.2:", type=("build", "run"), when="@1.14.0:")
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr@1.0.0:", type=("build", "run"))
    depends_on("r-future", type=("build", "run"))
    depends_on("r-future-apply", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"), when="@1.10.0:")
    depends_on("r-irlba", type=("build", "run"))
    depends_on("r-pbapply", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-fastmatch", type=("build", "run"))
    depends_on("r-rcpproll", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
    depends_on("r-vctrs", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"), when="@1.12.0:")
    depends_on("zlib-api")

    def url_for_version(self, version):
        return f"https://github.com/stuart-lab/signac/archive/refs/tags/{version}.tar.gz"
