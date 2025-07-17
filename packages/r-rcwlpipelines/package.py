# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcwlpipelines(RPackage):
    """Bioinformatics pipelines based on Rcwl

    A collection of Bioinformatics tools and pipelines based on R and the Common Workflow Language.
    """

    bioc = "RcwlPipelines"

    version("1.24.0", commit="9368b160d98a35f7b2e114de8dc9f7dd4a13909a")
    version("1.18.1", commit="0d1c0a0fb1cdc99b777acbf633e4896792bb00ca")
    version("1.18.0", md5="5ff1c2848694b09cc639a56009392cf3")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-rcwl", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-rappdirs", type=("build", "run"))
    depends_on("r-git2r", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
