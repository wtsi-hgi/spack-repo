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
#     spack install dejavu-fonts
#
# You can edit this file again by typing:
#
#     spack edit dejavu-fonts
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class DejavuFonts(MakefilePackage):
    """The DejaVu fonts are a font family based upon Bitstream Vera v1.10. Its purpose is to provide a wider range of characters while maintaining the original look-and-feel."""

    homepage = "https://github.com/dejavu-fonts/dejavu-fonts"
    url = "https://github.com/dejavu-fonts/dejavu-fonts/archive/refs/tags/version_2_37.tar.gz"

    version(
        "2.37",
        sha256="c4d10a1b665db893adc0c0aaee7ecd81b2b47c877d5cea0b40216707cbf327e4",
        url="https://github.com/dejavu-fonts/dejavu-fonts/archive/refs/tags/version_2_37.tar.gz",
    )

    depends_on("fontforge")
    depends_on("perl")
    depends_on("perl-font-ttf")
    depends_on("perl-io-string")

    @run_before("build")
    def fetch_additional_sources(self):
        git = which("git")
        curl = which("curl")
        with working_dir(join_path(self.stage.source_path, "resources")):
            git("clone", "git://anongit.freedesktop.org/git/fontconfig")
            move("fontconfig/fc-lang", "fc-lang")
            curl("-L", "-o", "UnicodeData.txt", "http://www.unicode.org/Public/UNIDATA/UnicodeData.txt")
            curl("-L", "-o", "Blocks.txt", "http://www.unicode.org/Public/UNIDATA/Blocks.txt")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("build/*.ttf", prefix.bin)
