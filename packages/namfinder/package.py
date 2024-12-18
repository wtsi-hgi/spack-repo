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
#     spack install namfinder
#
# You can edit this file again by typing:
#
#     spack edit namfinder
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Namfinder(CMakePackage):
    """Fast computation of shared regions between sequences."""

    homepage = "https://github.com/ksahlin/namfinder"
    url = "https://github.com/ksahlin/namfinder/archive/refs/tags/v0.1.3.tar.gz"

    license("MIT")

    version("0.1.3", sha256="c83862b9ed656ea0e639c8a2e28a83f671248b04f23a45106ece6800c2a7cc75")
    version("0.1.2", sha256="a62158ed5ec90e68c9e3a6165d4ec95dc50f27289cbb65318bd1fb6081d60b3e")
    version("0.1.1", sha256="44bbba3209372481c9d0c756d9a6e9bd07eb88e8c57e68bd07a4f8fae6e7d07f")
    version("0.1", sha256="bb57654d9b7c5b492308f5c00bd38649ad567f127388302293c24e42d78b4e19")

    depends_on("zlib")

    def cmake_args(self):
        args = ["-DCMAKE_C_FLAGS=-march=native", "-DCMAKE_CXX_FLAGS=-march=native"]
        return args
