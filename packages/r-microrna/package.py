# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrorna(RPackage):
    """Data and functions for dealing with microRNAs

    Different data resources for microRNAs and some functions for manipulating them.
    """

    bioc = "microRNA"

    version("1.66.0", commit="c486774aca9020ac0c5dd008b3ed55bbf78083cb")
    version("1.60.0", commit="37b8a8fd7d842f789c5f35d77fcfd7be57b3cfe9")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biostrings@2.11.32:", type=("build", "run"))
