# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandpack(RPackage):
    """Randomization routines for Clinical Trials

    A suite of classes and functions for randomizing patients in clinical trials.
    """

    bioc = "randPack"

    version("1.54.0", commit="a37f28326b3e21355783b9bfb73d41d4c14edee9")
    version("1.48.0", commit="d88939bb143e4d37fc9fdeb24431269221583dce")

    depends_on("r-biobase", type=("build", "run"))
