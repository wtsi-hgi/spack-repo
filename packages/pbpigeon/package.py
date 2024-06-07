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
#     spack install pbpigeon
#
# You can edit this file again by typing:
#
#     spack edit pbpigeon
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Pbpigeon(Package):
    """
    Pigeon is a PacBio Transcript Toolkit that contains tools to classify and filter full-length transcript
    isoforms into categories against a reference annotation.

    Pigeon is based off of SQANTI3 and the output is compatible with downstream analysis with Seurat.
    """

    homepage = "https://pigeon.how/classification/pigeon.html"
    url = "https://github.com/PacificBiosciences/pigeon/releases/download/v1.2.0/pigeon"

    license("BSD-3-Clause-Clear license")

    version("1.2.0", sha256="0202818fed1247d21b79bf58811402f7af2481b3731ebc1094b161cf03c0e009", expand=False)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/pigeon", prefix.bin.pbpigeon)
        chmod = which("chmod")
        chmod("+x", prefix.bin.pbpigeon)
