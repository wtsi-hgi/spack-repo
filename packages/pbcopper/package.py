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
#     spack install pbcopper
#
# You can edit this file again by typing:
#
#     spack edit pbcopper
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Pbcopper(MesonPackage):
    """
    Provides a suite of data structures, algorithms,
    and utilities for PacBio C++ applications.
    """

    homepage = "https://github.com/pacificbiosciences/pbcopper"
    url = "https://github.com/PacificBiosciences/pbcopper/archive/v2.3.0.tar.gz"

    maintainers("pb-dseifert", "mhsieh", "armintoepfer")

    license("PacBio open source license")

    version(
        "2.3.0",
        sha256="5a183e4a4c860b7e4616b7dda6a3e04fc447d91aa8d75cfbe9b66bebc909c631",
    )

    depends_on("boost@1.75:", type=("build", "run"))

    def meson_args(self):
        return ["-Dtests=false"]
