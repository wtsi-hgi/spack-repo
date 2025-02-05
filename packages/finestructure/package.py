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
#     spack install finestructure
#
# You can edit this file again by typing:
#
#     spack edit finestructure
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Finestructure(Package):
    """FineSTRUCTURE is a fast and powerful algorithm for identifying population
    structure using dense sequencing data."""

    homepage = "https://people.maths.bris.ac.uk/~madjl/finestructure/finestructure.html"
    url = "https://people.maths.bris.ac.uk/~madjl/finestructure/fs_4.1.1.zip"

    maintainers("daniellawson9")

    version("4.1.1", sha256="7af2dd51b02bf117e364f70e76d03920b0cd9ec17111b5be94dd2a5ab906b75e")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("fs_linux_glibc2.3", prefix.bin.fs)
        which("chmod")("+x", prefix.bin.fs)
