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
#     spack install slamem
#
# You can edit this file again by typing:
#
#     spack edit slamem
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Slamem(MakefilePackage):
    """slaMEM is a tool used to efficiently retrieve MEMs (Maximal Exact Matches) between a reference genome sequence and one or more query sequences."""

    homepage = "https://github.com/sguizard/slaMEM"
    url = "https://github.com/sguizard/slaMEM/archive/refs/tags/v0.8.5.tar.gz"

    license("GPL-3.0")

    version("0.8.5", sha256="e4cc49715b7552463d10757ce1779de3d13d4d0012f633de26045fafcb273603")
    version("0.8.4", sha256="eacd7308ce11485ab3dfa051f128038b6ad674a780ff05131ded7c297273da1a")
    version("0.8.3", sha256="6f3d744a878d4a20c2035d1c2e39c58a97abc5b3feb54cbda0fb2678f6308f9b")

    # depends_on("zlib")

    def install(self, spec, prefix):
        make()
        mkdirp(prefix.bin)
        install("slaMEM", prefix.bin)
