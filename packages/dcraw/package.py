# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Dcraw(Package):
    """Decoding raw digital photos in Linux"""

    homepage = "https://dechifro.org/dcraw/"
    git = "https://github.com/ncruces/dcraw.git"

    version("9.28.8", tag="v9.28.8")

    depends_on("jasper")
    depends_on("libjpeg")
    depends_on("lcms@2:")

    def install(self, spec, prefix):
        which("gcc")("-o", "dcraw", "-O4", "dcraw.c", "-lm", "-ljasper", "-ljpeg", "-llcms2")

        mkdir(prefix.bin)
        install("./dcraw", prefix.bin)
