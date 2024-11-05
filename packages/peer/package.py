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
#     spack install peer
#
# You can edit this file again by typing:
#
#     spack edit peer
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Peer(CMakePackage):
    """PEER is a collection of Bayesian approaches to infer hidden determinants and their effects from gene expression profiles using factor analysis methods."""

    homepage = "https://github.com/PMBio/peer"
    git = "https://github.com/PMBio/peer.git"

    license("GPL-2")

    version("20120508", commit="40bc4b2cd92459ce42f44dfe279717436395f3f6")

    depends_on("r", type=("build", "run"))
    depends_on("swig")

    def cmake_args(self):
        return [
            "-DBUILD_PYTHON_PACKAGE=OFF",
            "-DBUILD_PEERTOOL=ON",
        ]
