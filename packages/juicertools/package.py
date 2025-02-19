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
#     spack install juicertools
#
# You can edit this file again by typing:
#
#     spack edit juicertools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Juicertools(Package):
    """Juicebox is visualization software for Hi-C data. This distribution includes
    the source code for Juicebox, Juicer Tools, and Assembly Tools."""

    homepage = "https://github.com/aidenlab/JuicerTools"
    url = "https://github.com/aidenlab/JuicerTools/archive/refs/tags/v3.0.0.tar.gz"

    license("MIT")

    version("3.0.0", sha256="4486689330b43fbf739e580194cc5841e2765b7b272ce2a2a087d259b129a7a6")

    depends_on("java@1.8:", type=("build", "run"))
    depends_on("ant", type="build")

    def patch(self):
        filter_file(
            "/Library/Java/JavaVirtualMachines/jdk-13.0.2.jdk/Contents/Home",
            self.spec["java"].home,
            "juicebox.properties",
            string=True,
        )
        filter_file(
            "manifests/juicebox_jar/META-INF/",
            "",
            "build.xml",
            string=True,
        )
        filter_file(
            '"/resources/MANIFEST.MF"',
            '"${basedir}/src/resources/MANIFEST.MF"',
            "build.xml",
            string=True,
        )

    def install(self, spec, prefix):
        ant = which("ant")
        ant()

        # Install jar files from out/ directory
        mkdirp(prefix.bin)
        install_tree("out", prefix.bin)

    def setup_run_environment(self, env):
        # Add the installed jar files to CLASSPATH
        env.prepend_path("CLASSPATH", join_path(self.prefix.bin.artifacts, "Juicebox_jar", "Juicebox.jar"))
        env.prepend_path("CLASSPATH", join_path(self.prefix.bin.artifacts, "juicer_tools_jar", "juicer_tools.jar"))
