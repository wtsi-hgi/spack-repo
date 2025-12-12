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
#     spack install bmdca
#
# You can edit this file again by typing:
#
#     spack edit bmdca
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Bmdca(AutotoolsPackage):
    """Fork of matteofigliuzzi/bmDCA repository for Boltzmann-machine Direct Coupling Analysis (bmDCA)."""

    homepage = "https://github.com/ranganathanlab/bmDCA"
    url = "https://github.com/ranganathanlab/bmDCA/archive/refs/tags/v0.8.12.tar.gz"

    license("GNU-GPL-3.0-only")

    version("0.8.12", sha256="542991c51ba1e9d74b500e09e80d43f716fe4214a24d71f580a24df667762049")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkg-config", type="build")
    depends_on("netlib-lapack")
    depends_on("openblas")
    depends_on("armadillo")

    @run_after("install")
    def install_test(self):
        """Run the built-in usage message to verify the binary starts."""
        with working_dir("spack-test", create=True):
            Executable(join_path(self.prefix.bin, "bmdca"))("-h")
