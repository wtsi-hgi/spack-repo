# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaircompviz(RPackage):
    """Multiple comparison test visualization

    This package provides visualization of the results from the multiple (i.e. pairwise) comparison tests such as pairwise.t.test, pairwise.prop.test or pairwise.wilcox.test. The groups being compared are visualized as nodes in Hasse diagram. Such approach enables very clear and vivid depiction of which group is significantly greater than which others, especially if comparing a large number of groups.
    """

    bioc = "paircompviz"

    version("1.46.0", commit="67812e13916146cdca796fee2eed1c999e7b8eba")
    version("1.40.0", commit="636a6b854b037f049829b0c58dbf3d2c36817703")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
