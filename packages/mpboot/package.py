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
#     spack install mpboot
#
# You can edit this file again by typing:
#
#     spack edit mpboot
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Mpboot(CMakePackage):
    """fast phylogenetic maximum parsimony tree inference and bootstrap approximation."""

    homepage = "http://www.iqtree.org/mpboot"
    url = "https://github.com/diepthihoang/mpboot/archive/refs/tags/v1.2.tar.gz"
    git = "https://github.com/diepthihoang/mpboot.git"

    license("GPL-2.0")

    version("1.2", sha256="c7b40521b5c03770c85da86c928440cf77ebea656091bc805197b40e43114f2f")

    depends_on("llvm")

    def cmake_args(self):
        args = []
        args.append("-DIQTREE_FLAGS=avx")
        args.append("-DCMAKE_C_COMPILER={}/bin/clang".format(self.spec["llvm"].prefix))
        args.append("-DCMAKE_CXX_COMPILER={}/bin/clang++".format(self.spec["llvm"].prefix))
        args.append("-DCMAKE_CXX_STANDARD=11")
        return args

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(self.build_directory + "/mpboot-avx", prefix.bin.mpboot)
