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
#     spack install htslib-plugin
#
# You can edit this file again by typing:
#
#     spack edit htslib-plugin
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class HtslibPlugin(Package):
    """Plugins for use with HTSlib, including EGA-style encrypted (.cip) files,
    iRODS and Memory-mapped local files.

    The repo contains built libaries from Robert Davies."""

    homepage = "https://github.com/samtools/htslib-plugins"
    git = "https://gitlab.internal.sanger.ac.uk/eh19/htslib-plugin-libs.git"

    license("MIT")

    version("4.2.7", branch="v4.2.7")

    def install(self, spec, prefix):
        install_tree("lib", prefix.lib)
