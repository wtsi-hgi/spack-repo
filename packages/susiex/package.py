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
#     spack install susiex
#
# You can edit this file again by typing:
#
#     spack edit susiex
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Susiex(MakefilePackage):
    """
    SuSiEx is a C++ based command line tool that performs cross-ancestry
    fine-mapping using GWAS summary statistics and LD reference panels.
    The method is built on the Sum of Single Effects (SuSiE) model
    """

    homepage = "https://github.com/getian107/SuSiEx"
    url = "https://github.com/getian107/SuSiEx/archive/refs/tags/v1.1.2.tar.gz"

    license("MIT")

    version("1.1.2", sha256="87bb8bb6dcc73dce00e9be694e5eadc106b070eb2e05b71244a1d5a7fcde07d2")
    version("1.1.1", sha256="f2c212e524ef0c87423b60a4404e2a56143ff5843d89275692a591b6a959cab1")
    version("1.1.0", sha256="b67dca665e05b1e2a715033c29ad1485b8b3408edcf758d6f5f31a3bd202662c")
    version("1.0.0", sha256="131ae771a1cd48fec4ee82967707d2b0922b45e79f1defce3ddb5ea5a3aa18f1")

    def build(self, spec, prefix):
        cd("src")
        make("all")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("../bin/SuSiEx", prefix.bin)
