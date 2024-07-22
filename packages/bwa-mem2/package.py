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
#     spack install bwa-mem2
#
# You can edit this file again by typing:
#
#     spack edit bwa-mem2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
from pathlib import Path


class BwaMem2(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/bwa-mem2/bwa-mem2/archive/refs/tags/v2.2.1.tar.gz"
    git = "https://github.com/bwa-mem2/bwa-mem2.git"
    submodules = True

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("2.2.1", tag="v2.2.1")

    depends_on("zlib-api")

    def patch(self):
        filter_file(
            "#if defined(__GNUC__) && !defined(__clang__)",
            "#if defined(__GNUC__) && __GNUC__ < 11 && !defined(__clang__)",
            "src/utils.h",
            string=True,
        )

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        for exe in Path(self.stage.source_path).glob("bwa-mem2*"):
            install(str(exe), join_path(prefix.bin, exe.name))
        chmod = which("chmod")
        chmod("+x", join_path(prefix.bin, "bwa-mem2"))
