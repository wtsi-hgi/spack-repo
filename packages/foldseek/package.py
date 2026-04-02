# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Foldseek(CMakePackage):
    """Foldseek enables fast and sensitive comparisons of large protein structure sets"""

    homepage = "https://github.com/steineggerlab/foldmason"
    url = "https://github.com/steineggerlab/foldmason/archive/refs/tags/4-dd3c235.tar.gz"

    license("GPL-3.0-only")

    version("4-dd3c235", sha256="f01c261d822f68a615ef43c56dbe4b7ffed57c3115bdfd0299a33680dfaae67d")
    version(
        "9-427df8a",
        sha256="b17d2d85b49a8508f79ffd8b15e54afc5feef5f3fb0276a291141ca5dbbbe8bc",
        url="https://github.com/steineggerlab/foldseek/archive/refs/tags/9-427df8a.tar.gz",
    )
    version(
        "8-ef4e960",
        sha256="c74d02c4924d20275cc567783b56fff10e76ed67f3d642f53c283f67c4180a1e",
        url="https://github.com/steineggerlab/foldseek/archive/refs/tags/8-ef4e960.tar.gz",
    )
    version(
        "7-04e0ec8",
        sha256="009d722d600248a680b9e1e9dcb3bf799f8be8de41e80a598b7f39a5ced54191",
        url="https://github.com/steineggerlab/foldseek/archive/refs/tags/7-04e0ec8.tar.gz",
    )

    depends_on("zlib-api")
    depends_on("bzip2")
    depends_on("openmpi")
    depends_on("rust", type="build")
    depends_on("rust@1.78.0", when="@:9", type="build")

    @run_after("install")
    def install_test(self):
        """Basic invocation to ensure the CLI is runnable"""

        exe_path = None
        for name in ["foldmason", "foldseek"]:
            candidate = join_path(self.prefix.bin, name)
            if os.path.exists(candidate):
                exe_path = candidate
                break

        if exe_path is None:
            raise RuntimeError("foldseek installation is missing its executable")

        cli = Executable(exe_path)
        with working_dir("spack-test", create=True):
            cli("--help")
