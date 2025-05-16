# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RGenabelData(RPackage):
    """GenABEL.data is an R package containing the data files used by the GenABEL package."""

    homepage = "https://github.com/GenABEL-Project/GenABEL.data"
    cran = "GenABEL.data"

    version("1.0.0", sha256="2c28d5df63ae13545cf7aea6ce5f22ae1bbb58219fdaed6c1d5d5affc072c65c")
