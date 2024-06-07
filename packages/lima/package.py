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
#     spack install lima
#
# You can edit this file again by typing:
#
#     spack edit lima
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Lima(Package):
    """
    lima is the standard tool to identify barcode and primer sequences in PacBio
    single-molecule sequencing data. It powers the Demultiplex Barcodes GUI-based
    analysis applications.
    """

    homepage = "https://lima.how/"
    url = "https://github.com/PacificBiosciences/barcoding/releases/download/v2.9.0/lima.tar.gz"

    license("BSD-3-Clause-Clear license")

    version("2.9.0", sha256="a13437bc7a90ab5df3c19eac44384de2a14370d0391586b5aa63a6478f9c2c53")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/lima", prefix.bin.lima)
        install(self.stage.source_path + "/lima-undo", join_path(prefix.bin, "lima-undo"))
        chmod = which("chmod")
        chmod("+x", prefix.bin.lima)
        chmod("+x", join_path(prefix.bin, "lima-undo"))
