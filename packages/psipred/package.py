# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Psipred(Package):
    """"""

    homepage = "https://github.com/psipred/psipred"
    url = "https://github.com/psipred/psipred/archive/refs/tags/v4.0.tar.gz"

    version("4.0", sha256="ce4c901c8f152f6e93e4f70dc8079a5432fc64d02bcc0215893e33fbacb1fed2")

    def patch(self):
        filter_file("../bin", self.prefix.bin, "src/Makefile", string=True)

    def install(self, spec, prefix):
        cd("src")
        make()
        mkdir(prefix.bin)
        make("install")
