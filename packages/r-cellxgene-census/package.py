# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellxgeneCensus(RPackage):
    """The Census provides efficient computational tooling to access, query, and analyze all single-cell RNA data from CZ CELLxGENE Discover."""

    homepage = "https://chanzuckerberg.github.io/cellxgene-census"
    url = "https://chanzuckerberg.r-universe.dev/bin/linux/jammy/4.3/src/contrib/cellxgene.census_1.6.0.tar.gz"

    version("1.6.0", sha256="aa3372f59feecbd6c40c580d663ca8988bed6443e76145bdf22a5808a311a3d4")

    # depends_on("r-foo", type=("build", "run"))
