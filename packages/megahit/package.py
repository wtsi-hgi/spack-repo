# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Megahit(CMakePackage):
    """MEGAHIT: An ultra-fast single-node solution for
    large and complex metagenomics assembly via succinct de Bruijn graph"""

    homepage = "https://github.com/voutcn/megahit"
    url = "https://github.com/voutcn/megahit/archive/v1.1.3.tar.gz"

    license("GPL-3.0-only")

    version("1.2.9", sha256="09026eb07cc4e2d24f58b0a13f7a826ae8bb73da735a47cb1cbe6e4693118852")
    version("1.2.8", sha256="9f64c75920cd08cc41e7c9bbd0dba0e36a08cade8a6bdc7b91d46ed106ef44c9")
    version("1.2.7", sha256="9bd0bfd6946015feec9b5d98ff03688b9e6b634b7546b9b24481339bd5389f07")
    version("1.2.6", sha256="0fcd63e4fe4d4ee0d19ef4b63843b5d815bbcd0d5245e6f6e63082c3ee406d22")

    depends_on("zlib-api")
    depends_on("python", type="run")
