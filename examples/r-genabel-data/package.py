# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""
Example rationale: Typical R package fetched from CRAN with standard R deps.

What this teaches:
- Set cran to the CRAN package name; version() may use md5 from CRAN.
- Prefer sha256 over md5 for modern sources.
"""
from spack.package import *

class RGenabelData(RPackage):
    """GenABEL.data is an R package containing the data files used by the GenABEL package."""

    homepage = "https://github.com/GenABEL-Project/GenABEL.data"
    cran = "GenABEL.data"

    version("1.0.0", sha256="2c28d5df63ae13545cf7aea6ce5f22ae1bbb58219fdaed6c1d5d5affc072c65c")
