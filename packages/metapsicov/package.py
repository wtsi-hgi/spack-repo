# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Metapsicov(Package):
    """MetaPSICOV2"""

    homepage = "https://github.com/psipred/metapsicov"
    url = "https://github.com/psipred/metapsicov/archive/refs/tags/v2.0.3.tar.gz"

    version("2.0.3", sha256="03944dc7ce634c52b72a67774b8495e6881bac9703aabfb53901dd284d811576")

    # depends_on("foo")

    def patch(self):
        filter_file("../", self.prefix + "/", "src/Makefile", string=True)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        cd("src")
        make()
        make("install")
