# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class KentTools(MakefilePackage):
    """Entire source tree for the UCSC Genome Browser Group's suite of biological analysis and web display programs as well as some of Jim Kent's own tools."""

    homepage = "https://github.com/ucscGenomeBrowser/kent"
    git = "https://github.com/ucscGenomeBrowser/kent/"

    version("462", tag="v462_base")

    depends_on("openssl")
    depends_on("libpng")
    depends_on("libuuid")
    depends_on("glibc@:2.35")
    depends_on("gmake")
    depends_on("mariadb")
    depends_on("zlib")

    def edit(self, spec, prefix):
        filter_file("CFLAGS += -std=c99", "CFLAGS += -std=c99 -fPIC", "src/inc/common.mk", string=True)

        with open("src/inc/localEnvironment.mk", "w") as f:
            f.write(
                "kentSrc = "
                + join_path(self.stage.source_path, "src")
                + "\nMACHTYPE = x86_64\n"
                + "\nBINDIR = "
                + prefix.bin
                + "\nL = -lssl"
            )

    def build(self, spec, prefix):
        mkdir(prefix.bin)
        cd("src")
        make("destBin")
        make("libs")
        make("blatSuite")
        make("utils")
        cd("../")

    def install(self, spec, prefix):
        share_dir = join_path(self.prefix, "share", "kent-tree")
        mkdirp(share_dir)
        install_tree("src", share_dir)

    def setup_build_environment(self, env):
        env.set("BINDIR", self.prefix.bin)
        env.set("SCRIPTS", self.prefix.bin.scripts)

    def setup_environment(self, env):
        env.set("KENT_SRC", join_path(self.prefix, "share", "kent-tree"))
        env.set("MACHTYPE", "x86_64")

    def setup_dependent_build_environment(self, env, dependent_spec):
        self.setup_environment(env)
