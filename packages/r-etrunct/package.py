# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtrunct(RPackage):
    """Computes Moments of Univariate Truncated t Distribution"""

    cran = "etrunct"

    version("0.1", md5="3cbbc3b93874a20f653c2216cbc95030")

