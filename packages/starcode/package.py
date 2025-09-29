# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Starcode(Package):
    """Starcode is a DNA sequence clustering software."""

    homepage = "https://github.com/gui11aume/starcode"
    git = "https://github.com/gui11aume/starcode"

    version("1.4", tag="1.4")
    version("1.3", tag="1.3")

    depends_on("gcc@9.4.0", type=("build", "link"))

    def install(self, spec, prefix):
        make()
        mkdir(prefix + "/bin")
        install("starcode", prefix + "/bin")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            starcode = Executable(join_path(self.prefix.bin, "starcode"))
            starcode("--help")
