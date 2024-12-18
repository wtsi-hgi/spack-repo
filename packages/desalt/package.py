# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install desalt
#
# You can edit this file again by typing:
#
#     spack edit desalt
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os

from spack.package import *


class Desalt(Package):
    """De Bruijn graph-based Spliced Aligner for Long Transcriptome reads."""

    homepage = "https://github.com/ydLiu-HIT/deSALT"
    git = "https://github.com/ydLiu-HIT/deSALT.git"

    license("MIT")

    version("1.5.6", tag="v1.5.6")

    depends_on("zlib")

    def flag_handler(self, name, flags):
        if name.lower() == "cflags":
            flags.append("-fcommon")
        return (flags, None, None)

    def patch(self):
        os.remove("src/deBGA")

    def install(self, spec, prefix):
        cd("src/deBGA-master")
        make()
        cd("..")
        make()
        mkdirp(prefix.bin)
        install("deSALT", prefix.bin)
