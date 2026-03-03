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
#     spack install sspace-basic
#
# You can edit this file again by typing:
#
#     spack edit sspace-basic
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class SspaceBasic(Package):
    """Scaffolding Pre-Assemblies After Contig Extension (SSPACE)."""

    homepage = "https://github.com/nsoranzo/sspace_basic"
    url = "https://github.com/nsoranzo/sspace_basic/archive/refs/tags/v2.1.1.tar.gz"

    license("GPL-2.0")

    version("2.1.1", sha256="a23327a79a18e520544f0ea923b6c92ff2cc869617ade1c75e118b179caa0919")

    depends_on("bowtie")
    depends_on("perl", type=("build", "run"))

    def setup_run_environment(self, env):
        env.prepend_path("PERL5LIB", self.prefix.dotlib)

    def build(self, spec, prefix):
        pass

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install_tree("dotlib", prefix.dotlib)
        install("SSPACE_Basic.pl", prefix.bin)
