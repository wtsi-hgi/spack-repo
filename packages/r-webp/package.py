# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RWebp(RPackage):
    """Lossless webp images are 26% smaller in size compared to PNG. Lossy webp images are 25-34% smaller in size compared to JPEG."""

    homepage = "https://jeroen.r-universe.dev/webp"
    cran = "webp"

    version("1.2.0", sha256="d3810d351e6d4427d25d90e9074ec0d8b001c41a2d0791442b810de764c6356b")
    version("1.1.0", sha256="06ae1f069842f8287758fb2040fe40032740f7571f2ff0347e26b9e3203634a5")
    version("1.0", sha256="8da10925b202523ff5c4d46155af6ee7d6d690a9a947c3c3d2371aacbe7827c0")
    version("0.4", sha256="d9c0ea8508deca5622750c52c1c4af7c4fca64ee88d83cd25b17679dad975e4b")
    version("0.3", sha256="b1940be7e8db14c2a9ceedfe74fc8bb39ac19a7742dff23f918a88e1e55d5ebb")
    version("0.2", sha256="5a15e4ec1f353f814274c94c5b75525060c3972fafde0bacf5b238e739188bdb")

    depends_on("r-jpeg", type=("build", "run"))
    depends_on("r-png", type=("build", "run"))
