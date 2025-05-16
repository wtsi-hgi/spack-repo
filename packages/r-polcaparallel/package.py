# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RPolcaparallel(RPackage):
    """A reimplementation of poLCA [CRAN, GitHub] in C++. It tries to reproduce results and be as similar as possible to the original code but runs faster, especially with multiple repetitions by using multiple threads."""

    homepage = "https://github.com/QMUL/poLCAParallel"
    url = "https://github.com/QMUL/poLCAParallel/archive/refs/tags/v1.1.0.tar.gz"

    version("1.2.2", sha256="19fe140f8633eea19a23d50b73200cc96755c641d6d59bf7bfa4ff188e487d13")
    version("1.2.1", sha256="32b72ca98f1e82726486c860e198d3e84207e1102577c78f76a96ca16e12b323")
    version("1.2.0", sha256="57fa81e7318b99848560dc1a707ca4c36fb0fccbe26f4c8e70b992688e1f5e04")
    version("1.1.1", sha256="3b79cc377f9b23539b292b77df19501070ec3402e4c325e3605d6affa09bfd56")
    version("1.1.0", sha256="4bcc1e306d0acc9c539f96580a855f167ba30ae5594c9f019489c959d6f2c750")
    version("1.0.1", sha256="de4b8f582159aa3c871373e47d7816b5a5588d401944dc1418afe7dcbc9f113a")
    version("1.0.0", sha256="7278abf6d57b4ca58abfa09b4c5b9ecc34703f14800f00a7a65f04ea0485d308")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-scatterplot3d", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-polca", type=("build", "run"))
