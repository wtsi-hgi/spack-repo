# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os

from spack.package import *


class HsakmtRoct(CMakePackage):
    """This is a thunk python recipe to build and install Thunk Interface.
    Thunk Interface is a user-mode API interfaces used to interact
    with the ROCk driver."""


    variant("shared", default=True, description="Build shared or static library")



    @run_after("install")
    @on_package_attributes(run_tests=True)
    def check_install(self):

        test_dir = "tests/kfdtest"
        with working_dir(test_dir, create=True):
            cmake_bin = join_path(self.spec["cmake"].prefix.bin, "cmake")
            prefixes = ";".join(
                [
                    self.spec["libdrm"].prefix,
                    self.spec["hsakmt-roct"].prefix,
                    self.spec["numactl"].prefix,
                    self.spec["pkgconfig"].prefix,
                    self.spec["llvm-amdgpu"].prefix,
                    self.spec["zlib-api"].prefix,
                    self.spec["ncurses"].prefix,
                ]
            )
            hsakmt_path = ";".join([self.spec["hsakmt-roct"].prefix])
            cc_options = [
                "-DCMAKE_PREFIX_PATH=" + prefixes,
                "-DLIBHSAKMT_PATH=" + hsakmt_path,
                ".",
            ]
            self.run_test(cmake_bin, cc_options)
            make()
            os.environ["LD_LIBRARY_PATH"] = hsakmt_path
            os.environ["BIN_DIR"] = os.getcwd()
            self.run_test("scripts/run_kfdtest.sh")
            make("clean")