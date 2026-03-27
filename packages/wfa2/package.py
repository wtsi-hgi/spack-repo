# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Wfa2(CMakePackage):
    """Wavefront Alignment Algorithm v2 implementations providing C and C++
    libraries for fast gap-affine sequence alignment."""

    homepage = "https://github.com/smarco/WFA2-lib"
    url = "https://github.com/smarco/WFA2-lib/archive/refs/tags/v2.3.6.tar.gz"

    license("MIT")

    version("2.3.6", sha256="fd74c4bfdd5764ae8668cdeee7a80bfa35583b1980e261daa9dbf425bf12bb0b")
    version("2.3.5", sha256="2609d5f267f4dd91dce1776385b5a24a2f1aa625ac844ce0c3571c69178afe6e")
    version("2.3.4", sha256="3a02d19b45c7efcdcabdd956421b1e449e771fca0b0f072e02d7aa65ebb29f23")
    version("2.3.3", sha256="2569650cdba395f42513a4d2c9175724a736047bb7da99a162c0abdbd651698f")

    depends_on("cmake@3.16:", type="build")
    depends_on("pkgconfig", type=("build", "test"))

    def patch(self):
        # Upstream enables -march=native for Release builds which breaks
        # portability on generic build hosts.
        filter_file(
            "-march=native ",
            "",
            "CMakeLists.txt",
            string=True,
        )

    @run_after("install")
    def install_test(self):
        pkg_config = which("pkg-config")
        pkg_paths = []
        for libdir in ("lib", "lib64"):
            pkgdir = join_path(getattr(self.prefix, libdir), "pkgconfig")
            if os.path.isdir(pkgdir):
                pkg_paths.append(pkgdir)
        if pkg_paths:
            pkg_config.add_default_env("PKG_CONFIG_PATH", os.pathsep.join(pkg_paths))
        pkg_config("--modversion", "libwfa2")
