# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Oarfish(Package):
    """Transcript-level quantification for long-read RNA-seq datasets."""

    maintainers("softpack-bot")

    homepage = "https://combine-lab.github.io/oarfish"
    url = "https://github.com/COMBINE-lab/oarfish/archive/refs/tags/v0.9.4.tar.gz"

    license("BSD-3-Clause")

    version("0.9.4", sha256="d991443d224edd97d6951b5d99c17bc1c920dc137fb0c606bc3dc5b9f3d25b62")

    depends_on("rust-bootstrap@1.91:", type="build")
    depends_on("git", type="build")

    def install(self, spec, prefix):
        cargo = Executable(join_path(spec["rust-bootstrap"].prefix.bin, "cargo"))
        cargo("install", "--locked", "--root", prefix, "--path", ".")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            oarfish = Executable(join_path(self.prefix.bin, "oarfish"))
            oarfish("--help")
