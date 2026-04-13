# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Libva(AutotoolsPackage):
    """Libva is an implementation for VA-API (Video Acceleration API).
    VA-API is an open-source library and API specification, which provides
    access to graphics hardware acceleration capabilities for video
    processing. It consists of a main library and driver-specific
    acceleration backends for each supported hardware vendor."""

    homepage = "https://github.com/intel/libva"
    url = "https://github.com/intel/libva/archive/refs/tags/2.22.0.tar.gz"

    version("2.22.0", sha256="467c418c2640a178c6baad5be2e00d569842123763b80507721ab87eb7af8735")

    # depends_on("c", type="build")
    # depends_on("cxx", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("libdrm")
    depends_on("libx11", when="^[virtuals=gl] glx")
    depends_on("libxext", when="^[virtuals=gl] glx")

    def autoreconf(self, spec, prefix):
        autogen = Executable("./autogen.sh")
        autogen()

    def configure_args(self):
        spec = self.spec
        args = ["--disable-x11", "--disable-wayland", "--disable-glx", "--enable-libdrm"]
        if spec.satisfies("^[virtuals=gl] glx"):
            args.append("--enable-x11")
        else:
            args.append("--disable-x11")
        return args

    @run_after("install")
    def install_test(self):
        pkgconfig_dirs = []
        for lib_attr in ("lib", "lib64"):
            candidate = join_path(getattr(self.prefix, lib_attr), "pkgconfig")
            if os.path.isdir(candidate):
                pkgconfig_dirs.append(candidate)

        if not pkgconfig_dirs:
            raise InstallError("libva pkg-config metadata not installed")

        env = os.environ.copy()
        env["PKG_CONFIG_PATH"] = os.pathsep.join(
            pkgconfig_dirs + [env.get("PKG_CONFIG_PATH", "")]
        ).rstrip(os.pathsep)
        pkgconfig = which("pkg-config")
        pkgconfig("--modversion", "libva", env=env)
