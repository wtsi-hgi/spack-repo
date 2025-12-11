# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Bmdca(AutotoolsPackage):
    """Boltzmann-machine Direct Coupling Analysis (bmDCA) infers Potts models
    from multiple sequence alignments using an OpenMP-enabled C++11 codebase."""

    homepage = "https://github.com/ranganathanlab/bmDCA"
    url = "https://github.com/ranganathanlab/bmDCA/archive/refs/tags/v0.8.12.tar.gz"
    git = "https://github.com/ranganathanlab/bmDCA.git"

    license("GPL-3.0-or-later")

    version("0.8.12", sha256="542991c51ba1e9d74b500e09e80d43f716fe4214a24d71f580a24df667762049")

    force_autoreconf = True

    depends_on("armadillo")
    depends_on("openblas")
    depends_on("netlib-lapack")

    depends_on("pkgconfig", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    @run_after("install")
    def install_test(self):
        """Run the built-in usage message to verify the binary starts."""
        with working_dir("spack-test", create=True):
            Executable(join_path(self.prefix.bin, "bmdca"))("-h")
