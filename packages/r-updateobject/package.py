# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpdateobject(RPackage):
    """Find/fix old serialized S4 instances

    A set of tools built around updateObject() to work with old serialized S4 instances. The package is primarily useful to package maintainers who want to update the serialized S4 instances included in their package. This is still work-in-progress.
    """

    homepage = "https://bioconductor.org/packages/updateObject"
    bioc = "updateObject"

    version("1.12.0", commit="2b8328aa5b87b158392410368355d08be54030f8")
    version("1.6.0", commit="e7909b8cd54838087d368f5cc55433c1139cf416")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-biocgenerics@0.47.1:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("git", type=("build", "link", "run"))
