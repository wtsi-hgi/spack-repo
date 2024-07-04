# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Gtkmm(MesonPackage, AutotoolsPackage):
    """Gtkmm is the official C++ interface for the popular GUI library GTK+."""

    homepage = "https://www.gtkmm.org/en/"
    url = "https://mirror.accum.se/pub/GNOME/sources/gtkmm/2.24/gtkmm-2.24.4.tar.xz"

    license("LGPL-2.1-or-later")

    version("3.24.9", sha256="30d5bfe404571ce566a8e938c8bac17576420eb508f1e257837da63f14ad44ce")
    version("3.24.8", sha256="d2940c64922e5b958554b23d4c41d1839ea9e43e0d2e5b3819cfb46824a098c4")
    version("3.24.7", sha256="1d7a35af9c5ceccacb244ee3c2deb9b245720d8510ac5c7e6f4b6f9947e6789c")
    version("3.24.6", sha256="4b3e142e944e1633bba008900605c341a93cfd755a7fa2a00b05d041341f11d6")
    version("3.24.5", sha256="856333de86689f6a81c123f2db15d85db9addc438bc3574c36f15736aeae22e6")
    version("3.24.4", sha256="9beb71c3e90cfcfb790396b51e3f5e7169966751efd4f3ef9697114be3be6743")
    version("3.24.3", sha256="60497c4f7f354c3bd2557485f0254f8b7b4cf4bebc9fee0be26a77744eacd435")
    version("3.24.2", sha256="6d71091bcd1863133460d4188d04102810e9123de19706fb656b7bb915b4adc3")
    version("3.24.1", sha256="ddfe42ed2458a20a34de252854bcf4b52d3f0c671c045f56b42aa27c7542d2fd")
    version("3.24.0", sha256="cf5fc92805e581c8303e08d54519457ba07f15b766e9b1edde4862993ac1aa43")
    version("2.24.5", sha256="0680a53b7bf90b4e4bf444d1d89e6df41c777e0bacc96e9c09fc4dd2f5fe6b72")
    # version("2.19.6", sha256="d495d4012d49841a4f0a09584e002bc25ef55d7b2782660ecf7a58ed67357ad7")
    # version("2.19.4", sha256="ade220b0d395cb44215a69623af40a420281bc090ddaefc55350ad48e888fed2")
    # version("2.19.2", sha256="9c152f2d652344d9000756491c6b00bd394162f57f4302524db8535144b397a0")
    # version("2.17.11", sha256="0ec15d7aa14a0528352adf91aa612079590ba377aa15f47f7c8d37611ffbfbcd")
    # version("2.17.1", sha256="bd1369caeb28ffdc9e81b1c4dc846c265dd9533bed7958756b3ee4d14ffa1694")
    # version("2.16.0", sha256="7b2cccda794531ecfa65c01e57614ecba526153ad2a29d580c6e8df028d56ec4")
    # version("2.4.11", sha256="0754187a5bcf3795cd7c959de303e6a19a130b0c5927bff1504baa3524bee8c1")

    depends_on("automake", type="build", when="@:2")
    depends_on("autoconf", type="build", when="@:2")
    depends_on("libtool", type="build", when="@:2")

    depends_on("glibmm@:2.66", when="@:3")
    depends_on("atkmm")
    depends_on("gtkplus@3:", when="@3:")
    depends_on("gtkplus@:2", when="@:2")
    depends_on("pangomm@:2.46", when="@:3")
    depends_on("cairomm@:1.14", when="@:3")
    depends_on("cmake", type="build")

    build_system(
        conditional("autotools", when="@b:2"),
        conditional("meson", when="@3:,:b"),
        default="meson",
    )

    def url_for_version(self, version):
        """Handle glib's version-based custom URLs."""
        url = "https://ftp.acc.umu.se/pub/GNOME/sources/gtkmm"
        ext = ".tar.gz" if version < Version("3.1.0") else ".tar.xz"
        return url + "/%s/gtkmm-%s%s" % (version.up_to(2), version, ext)

    def meson_args(self):
        return ["-Dbuild-demos=false", "-Dbuild-tests=false"]

    def patch(self):
        if self.spec.satisfies("@3:"):
            filter_file("subdir('demos/gtk-demo')", "", "meson.build", string=True)

    #     for i in ["configure.ac", "Makefile.am", "meson.build"]:
    #         filter_file("cairomm-1.0", "cairomm-1.16", i, string=True)
    #         filter_file("pangomm-1.4", "pangomm-2.48", i, string=True)
