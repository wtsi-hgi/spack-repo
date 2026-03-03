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
#     spack install bwa-mem2
#
# You can edit this file again by typing:
#
#     spack edit bwa-mem2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
from pathlib import Path


class BwaMem2(MakefilePackage):
    """The tool bwa-mem2 is the next version of the bwa-mem algorithm in bwa. It produces alignment identical to bwa and is ~1.3-3.1x faster depending on the use-case, dataset and the running machine.

    The original bwa was developed by Heng Li (@lh3). Performance enhancement in bwa-mem2 was primarily done by Vasimuddin Md (@yuk12) and Sanchit Misra (@sanchit-misra) from Parallel Computing Lab, Intel. bwa-mem2 is distributed under the MIT license.
    """

    homepage = "https://github.com/bwa-mem2/bwa-mem2"
    url = "https://github.com/bwa-mem2/bwa-mem2/archive/refs/tags/v2.2.1.tar.gz"
    git = "https://github.com/bwa-mem2/bwa-mem2.git"
    submodules = True

    license("MIT")

    version("2.2.1", tag="v2.2.1")

    depends_on("zlib-api")

    def patch(self):
        filter_file(
            "#if defined(__GNUC__) && !defined(__clang__)",
            "#if defined(__GNUC__) && __GNUC__ < 11 && !defined(__clang__)",
            "src/utils.h",
            string=True,
        )

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        for exe in Path(self.stage.source_path).glob("bwa-mem2*"):
            install(str(exe), join_path(prefix.bin, exe.name))
        chmod = which("chmod")
        chmod("+x", join_path(prefix.bin, "bwa-mem2"))
