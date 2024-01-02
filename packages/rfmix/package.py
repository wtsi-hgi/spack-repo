# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Rfmix(AutotoolsPackage):
    """Local Ancestry and Admixture analysis."""

    git = "https://github.com/slowkoni/rfmix"

    version("2", commit="09599c19c69f81571c7a7aab4cd2d847a9e0633a")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
