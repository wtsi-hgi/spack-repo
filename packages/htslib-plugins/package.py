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
#     spack install htslib-plugins
#
# You can edit this file again by typing:
#
#     spack edit htslib-plugins
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class HtslibPlugins(MakefilePackage):
    """Plugins for use with HTSlib.."""

    homepage = "https://github.com/samtools/htslib-plugins"
    url = "https://github.com/samtools/htslib-plugins/archive/refs/tags/201712.tar.gz"
    git = "https://github.com/samtools/htslib-plugins.git"

    license("MIT")

    version("20210319", commit="5f12dfb90d44f46d2e975ce9a823f7f042b92d69")

    depends_on("irods-client@4.2.7", type=("build", "link", "run"))
    depends_on("htslib@1.20")
    depends_on("openssl")

    def edit(self, spec, prefix):
        makefile = FileFilter("Makefile")
        makefile.filter("/usr/local", self.prefix, string=True)

    def setup_build_environment(self, env):
        env.set("IRODS_HOME", self.spec["irods-client"].prefix.usr)

    def setup_run_environment(self, env):
        env.prepend_path("HTS_PATH", self.prefix.libexec.htslib)
