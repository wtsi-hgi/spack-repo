# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Stracode(Package):
    """Starcode: sequence clustering based on all-pairs search.

    This package builds the Starcode binary from the 1.3 GitHub release.
    """

    maintainers("softpack-bot")

    homepage = "https://github.com/gui11aume/starcode"
    url = "https://github.com/gui11aume/starcode/archive/refs/tags/1.3.tar.gz"

    license("GPL-3.0-or-later")

    version("1.3", sha256="e0af6518f0467a9d68f338bebb2c7487262ea3679584b5024655460f2ff226a9")

    # No external dependencies; builds with a C compiler and pthread/math.
    def patch(self):
        # GCC 10+ defaults to -fno-common which breaks old-style globals.
        # Add -fcommon to release flags to avoid multiple definition errors.
        if self.compiler.name == "gcc" and self.compiler.version >= Version("10"):
            filter_file(
                "REL_CFLAGS= -std=c99 -O3 -Wall",
                "REL_CFLAGS= -std=c99 -O3 -Wall -fcommon",
                "Makefile",
                string=True,
            )

    def install(self, spec, prefix):
        make()
        mkdir(prefix.bin)
        install("starcode", prefix.bin)

    @run_after("install")
    def install_test(self):
        # Prefer CLI check if available
        with working_dir("spack-test", create=True):
            starcode = Executable(join_path(self.prefix.bin, "starcode"))
            starcode("--help")
