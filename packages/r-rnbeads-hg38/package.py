# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeadsHg38(RPackage):
    """RnBeads.hg38

    Automatically generated RnBeads annotation package for the assembly hg38.
    """

    bioc = "RnBeads.hg38"

    version("1.40.0", commit="47bab6c1948b64631880db2ab226567c1d527762")
    version("1.34.0", commit="53c8f644fcc2ff2168a515513705e3a6dca73567")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
