# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBase64enc(RPackage):
    """Tools for base64 encoding."""

    cran = "base64enc"

    version("0.1-3", sha256="6d856d8a364bcdc499a0bf38bfd283b7c743d08f0b288174fba7dbf0a04b688d")
    version("0.1-2", sha256="05fed8fde229fce48f5b9cd34f3bf92f2ca63d6038ba7cb9d37a2904e83e4b34")
    version("0.1-1", sha256="9b021467514c4cf847d22f499fd593ea8065cf8f5057c8697dd13855accdd429")
    version("0.1-0", sha256="2b5f52ca9a6bac99f1aebdbcf30e8c257bad8160797d11c5fc3aa7a6bebb6852")

    depends_on("r@2.9.0:", type=("build", "run"))
