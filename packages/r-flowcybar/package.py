# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowcybar(RPackage):
    """Analyze flow cytometric data using gate information

    A package to analyze flow cytometric data using gate information to follow population/community dynamics
    """

    homepage = "http://www.ufz.de/index.php?de=16773"
    bioc = "flowCyBar"

    version("1.44.0", commit="9eb4f0a750d85f13cda96e7be4200cd0a94bca45")
    version("1.38.0", commit="012d51a3ef137b43f579555324a64f061d74bb1a")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-vegan", type=("build", "run"))
