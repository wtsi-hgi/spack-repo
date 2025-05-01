# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Lima(Package):
    """
    lima is the standard tool to identify barcode and primer sequences in PacBio
    single-molecule sequencing data. It powers the Demultiplex Barcodes GUI-based
    analysis applications.
    """

    homepage = "https://lima.how/"
    url = "https://github.com/PacificBiosciences/barcoding/releases/download/v2.9.0/lima.tar.gz"

    license("BSD-3-Clause-Clear")

    version("2.13.0", sha256="89601814e220f3bc4e062113281ce282767dffa8d65b4bf085597c9db47033da")
    version("2.9.0", sha256="a13437bc7a90ab5df3c19eac44384de2a14370d0391586b5aa63a6478f9c2c53")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/lima", prefix.bin.lima)
        install(self.stage.source_path + "/lima-undo", join_path(prefix.bin, "lima-undo"))
        chmod = which("chmod")
        chmod("+x", prefix.bin.lima)
        chmod("+x", join_path(prefix.bin, "lima-undo"))
