# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class KentGit(MakefilePackage):
    """Entire source tree for the UCSC Genome Browser Group's suite of biological analysis and web display programs as well as some of Jim Kent's own tools."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/ucscGenomeBrowser/kent"
    url = "https://hgdownload.cse.ucsc.edu/admin/jksrc.zip"
    
    version("0.0.1", sha256="5a137f3127ee8edc56ae75febc5b05be50698616e1fa229766ce44ce2cb5fb11")

    depends_on("openssl")
    depends_on("libpng")
    depends_on("libuuid")
    depends_on("mysql@5.7.27") # build only?

    patch("fpic.patch")

    def build(self, spec, prefix):
        cd(join_path("src", "lib"))
        make()
        cd("../../")

    def install(self, spec, prefix):
        share_dir = join_path(self.prefix, "share", "kent-tree")
        mkdirp(share_dir)
        install_tree("src", share_dir)

    def setup_environment(self, env):
        env.set("KENT_SRC", join_path(self.prefix, "share", "kent-tree"))
        env.set("MACHTYPE", "x86_64")

    def setup_build_environment(self, env):
        self.setup_environment(env)

    def setup_run_environment(self, env):
        self.setup_environment(env)

    def setup_dependent_build_environment(self, env, dependent_spec):
        self.setup_environment(env)

    def setup_dependent_run_environment(self, env, dependent_spec):
        self.setup_environment(env)
