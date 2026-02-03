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
#     spack install r-metaphlantophyloseq
#
# You can edit this file again by typing:
#
#     spack edit r-metaphlantophyloseq
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RMetaphlantophyloseq(RPackage):
    """A simple R package to convert MetaPhlAn 4 output profiles to a phyloseq object."""

    homepage = "https://jrotzetter.github.io/metaphlanToPhyloseq/"
    url = "https://github.com/jrotzetter/metaphlanToPhyloseq/archive/refs/tags/v0.2.0.tar.gz"


    license("MIT")

    version("0.2.0", sha256="eccf4aa2ff841216f68ec933209f5d702173213f21e984aa563279fb51831592")

    depends_on("r-dplyr@1.1.4:")
    depends_on("r-phyloseq@1.46.0:")
    depends_on("r-r-utils")

    @run_after("install")
    def install_test(self):
        rscript = Executable(join_path(self.spec["r"].prefix.bin, "Rscript"))
        rscript("-e", 'library("metaphlanToPhyloseq")')
