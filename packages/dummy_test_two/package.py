# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class DummyTestTwo(BundlePackage):
    """A second dummy bundle package for testing parallel GitHub Actions workflow. Also depends on zlib."""

    homepage = "https://example.com/dummy-test-two"

    license("MIT")

    version("1.0.0")

    # Simple dependency for testing parallel processing
    depends_on("zlib", type=("build", "run"))
