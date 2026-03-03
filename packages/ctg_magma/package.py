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
#     spack install ctg-magma
#
# You can edit this file again by typing:
#
#     spack edit ctg-magma
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class CtgMagma(MakefilePackage):
    """MAGMA: Generalized Gene-Set Analysis of GWAS Data"""

    homepage = "https://cncr.nl/research/magma"
    url = "https://vu.data.surfsara.nl/index.php/s/8qDPUbOTrZ9lW2b/download?path=%2F&files=magma_v1.07b_source.zip"

    version(
        "1.07b",
        sha256="b8f6c9c5b81cedec51b2e3daafe2519f02423a7d18321f5a91534461d40538f0",
        url="https://vu.data.surfsara.nl/index.php/s/8qDPUbOTrZ9lW2b/download?path=%2F&files=magma_v1.07b_source.zip",
    )

    def flag_handler(self, name, flags):
        if name.lower() == "cxxflags":
            flags.append("-fpermissive")
        return (flags, None, None)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("magma", prefix.bin)
