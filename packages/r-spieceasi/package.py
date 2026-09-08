# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpieceasi(RPackage):
    """Sparse inverse covariance for ecological statistical inference.

    SpiecEasi estimates networks from the precision matrix of compositional
    microbial abundance data.
    """

    homepage = "https://github.com/zdk123/SpiecEasi"
    url = "https://github.com/zdk123/SpiecEasi/archive/refs/tags/v1.1.1.tar.gz"

    license("GPL-2.0-or-later")

    version("1.1.1", sha256="0f79f5c86a2d28a469116c2f19c29746a7a3495776dcff4d83754137b6158e63")
    version("1.1.0", sha256="989634c536409b84cf1036904460a57c7268ffb639fe2e414142c484e1e8026c")
    version("1.0.7", sha256="1f72dde985bab2ffee63c4b1e2bf0eb4796243750ecb8f576598408fdaa9d1dd")
    version("1.0.5", sha256="c37d51829d5fcf472094419e6a6be37a42de46103c1496e75c921c218d652914")
    version("1.0.2", sha256="ff8930a01a211ebcdf719336f26d385e92a7515db0cf6a07e50923b9e8dd8e37")
    version("1.0.0", sha256="b2cf88fc60c67185edd6b4b578eaa1a6e0a96604466db83be1c88df6bd4903bc")
    version("0.1.4", sha256="75c6dbc37616938f1263a0eacfcf97febfc8e9e2abb7e11a496131a791297422")

    depends_on("r@3.0:", type=("build", "run"))
    depends_on("r@3.3:", when="@1.0:", type=("build", "run"))
    depends_on("r@3.6:", when="@1.1:", type=("build", "run"))

    depends_on("r-huge", type=("build", "run"))
    depends_on("r-huge@1.3.2:", when="@1.0.7:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-vgam", type=("build", "run"))
    depends_on("r-pulsar", when="@1.0:", type=("build", "run"))
    depends_on("r-pulsar@0.3.4:", when="@1.0.2:", type=("build", "run"))
    depends_on("r-glmnet", when="@1.1:", type=("build", "run"))
    depends_on("r-rcpp", when="@1.1:", type=("build", "run"))
    depends_on("r-rcpparmadillo", when="@1.1:", type=("build", "run"))
