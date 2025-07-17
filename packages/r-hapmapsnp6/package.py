# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmapsnp6(RPackage):
    """Sample data - Hapmap SNP 6.0 Affymetrix

    Sample dataset obtained from http://www.hapmap.org
    """

    bioc = "hapmapsnp6"

    version("1.50.0", commit="5aee0aac5cca1d621ec50b117e8a9ef21fba156d")
    version("1.44.0", commit="661c2b454e997160a07cb0b995f434f48ed004db")

    depends_on("r@2.15:", type=("build", "run"))
