# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreastcancermainz(RPackage):
    """Gene expression dataset published by Schmidt et al. [2008] (MAINZ).

    Gene expression data from the breast cancer study published by Schmidt et al. in 2008, provided as an eSet.
    """

    homepage = "http://compbio.dfci.harvard.edu/"
    bioc = "breastCancerMAINZ"

    version("1.46.0", commit="93f3f3eca2e51d40ee61a992b5255877bf20de26")
    version("1.40.0", commit="3be3a6da244ccac9aa04d16bfb5d427e451a95e4")

    depends_on("r@2.5:", type=("build", "run"))
