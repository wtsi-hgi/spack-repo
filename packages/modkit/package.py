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
#     spack install modkit
#
# You can edit this file again by typing:
#
#     spack edit modkit
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Modkit(Package):
    """A bioinformatics tool for working with modified bases from Oxford Nanopore.
    Specifically for converting modBAM to bedMethyl files using best practices,
    but also manipulating modBAM files and generating summary statistics."""

    homepage = "https://github.com/nanoporetech/modkit"
    url = "https://github.com/nanoporetech/modkit/releases/download/v0.4.3/modkit_v0.4.3_u16_x86_64.tar.gz"

    # Custom ONT license
    license("ONT-PL-1.0")

    version("0.4.3", sha256="e83fd367464ae299a34b4e6d2561d19202d2e5b7f22e38a40160a548bde36fbd")
    version("0.4.2", sha256="ede6fb23f31a4db91f48b1fe376e3916efddd1630ac5b05bcc61aba68553411b")
    version("0.4.1", sha256="d6cb43f2848e6ce3ad01703ed83505990767bf8c5c8acbde215b01bc701f77dc")
    version("0.4.0", sha256="6cf74779a93aa3a072384e242a374c0282932b1c5fb6c38a7dec1a551d94a670")
    version("0.3.3", sha256="88ec890556f2106513e3db461efa005817ff2d59d933d4beaa4b4ffe9f06f340")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("modkit", prefix.bin.modkit)
        chmod = which("chmod")
        chmod("+x", prefix.bin.modkit)
