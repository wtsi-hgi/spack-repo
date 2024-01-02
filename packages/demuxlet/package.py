# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *

class Demuxlet(AutotoolsPackage):
    """Genetic multiplexing of barcoded single cell RNA-seq"""

    git = "https://github.com/statgen/demuxlet"

    version("2021-02-11", commit="f5044eb9ed5c6678aa3a80a8f2be7db7748ee732")

    depends_on("htslib@1.10~libdeflate", type=("build", "link"))
    depends_on("pkg-config", type="build")
    depends_on("zlib", type=("build", "link"))
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    def patch(self):
        mkdir("m4")
        filter_file(
                "../htslib/libhts.a",
                self.spec["htslib"].prefix.lib + "/libhts.a",
                "Makefile.am"
        )

    def configure_args(self):
        args = []

        args.append("--with-htslib={0}".format(self.spec["htslib"].prefix))

        return args
