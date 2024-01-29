# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import glob

class Tktable(AutotoolsPackage):
    """The tile project is a modified Tk styling engine demo. Currently it supports a standard Tk theme, an alternative Tk theme and an XP native theme."""

    homepage = "https://tktable.sourceforge.net/"
    url = "https://sourceforge.net/projects/tktable/files/tktable/2.10/Tktable2.10.tar.gz/download"

    version("2.10", sha256="c335117fa1be45fe4d3032e96fd4b4641fff6a4f8467878608dabed11198a4cb")

    depends_on("tcl")
    depends_on("tk")
    depends_on("pkg-config")

    def configure_args(self):
        return [
                "--with-tclconfig="+self.spec["tcl"].prefix.lib,
                "--with-tkconfig="+self.spec["tk"].prefix.lib
         ]

    def install(self, spec, prefix):
        mkdir(prefix.lib)
        for obj in glob.glob("*.so"):
            install(obj, prefix.lib)
