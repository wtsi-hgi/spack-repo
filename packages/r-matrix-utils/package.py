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
#     spack install r-matrix-utils
#
# You can edit this file again by typing:
#
#     spack edit r-matrix-utils
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RMatrixUtils(RPackage):
    """Implements data manipulation methods such as cast, aggregate, and merge/join for Matrix and matrix-like objects."""

    cran = "Matrix.utils"

    version("0.9.8", sha256="ebc59d3ef751775515586ff1f2396e429a1e9d91a10099d804134fcf74c0ae28")
    version("0.9.7", sha256="6a9fbc9f7117e1a3978948739cbdd57860996498d96b2fe56fc1bf2115c9c4f4")
    version("0.9.6", sha256="2f0d02b5085b44b5fa38bec2af55d273e0c50761d9ddeb246ea0e26d7c114229")
    version("0.9.5", sha256="481c1f650871872feaa4d208b5e12f0e184957490fa2471fe323dcd685aef414")
    version("0.9.4", sha256="adeb2b693460a97dfa6e269f262823822345a7bc88f3c8d54ca719443bb974ad")
    version("0.9.3", sha256="3c19d99e07039e9b7f406cac687e5e02af4bb55c801c1db966d019021f8d0530")
    version("0.9.2", sha256="55eab5184b6eb36b1b53a5c42adb8b192596fea15bcfae9b7bc177f20448314c")
    version("0.9.1", sha256="7fa2f680922796df13fe08c6d2acae6eaf8b9351e94c8f974d34ae8a054aad17")
    version("0.9.0", sha256="2be687e627f7fd6205b183f4e4877476f33ea8e8fe9090571320ae6cf56cc904")
    version("0.5", sha256="f46778c26d2ee866c186994cf89e4b0629579cbfd7fe394b53a7b2bb784a5a13")

