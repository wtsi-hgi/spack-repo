# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWarp(RPackage):
    """Group Dates.

    Tooling to group dates by a variety of periods
    including: yearly, monthly, by second, by week of the month, and more.
    The groups are defined in such a way that they also represent the
    distance between dates in terms of the period. This extracts valuable
    information that can be used in further calculations that rely on a
    specific temporal spacing between observations."""

    cran = "warp"

    version("0.2.0", sha256="0e0de344f3d711d58e6be2ab47ade1db3b703bf3ca85080b1124c0c25a630a68")

    depends_on("r@3.2.0:", type=("build", "run"))
