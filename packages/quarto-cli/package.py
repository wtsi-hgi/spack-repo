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
#     spack install quarto-cli
#
# You can edit this file again by typing:
#
#     spack edit quarto-cli
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class QuartoCli(Package):
    """Quarto is an open-source scientific and technical publishing system built on Pandoc. Quarto documents are authored using markdown, an easy to write plain text format."""

    homepage = "https://github.com/quarto-dev/quarto-cli"
    url = "https://github.com/quarto-dev/quarto-cli/archive/refs/tags/v1.1.251.tar.gz"

    version("1.4.418", sha256="e1b3dbbefccf455efac0839b0f59d621174df34643f9bbad74c522227c7f462b")
    version("1.1.251", sha256="c6761abe793912042c607b45b9676bae9cd118a4808e6aab8f2ce7dcaccc9cf9")

    depends_on("unzip", type="build")

    def install(self, spec, prefix):
        filter_file(
                "echo \"99.9.9\"",
                "echo \""+str(spec.version)+"\"",
                "package/scripts/common/quarto",
                string=True,
            )

        which("./configure.sh")()

        install_tree("./", prefix)

    def setup_dependent_environmen(self):
        prepend_path("PATH", self.prefix + "/package/dist/bin")

