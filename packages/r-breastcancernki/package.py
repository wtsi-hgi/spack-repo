# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreastcancernki(RPackage):
    """Genexpression dataset published by van't Veer et al. [2002] and van de Vijver et al. [2002] (NKI).

    Genexpression data from a breast cancer study published by van't Veer et al. in 2002 and van de Vijver et al. in 2002, provided as an eSet.
    """

    homepage = "http://compbio.dfci.harvard.edu/"
    bioc = "breastCancerNKI"

    version("1.46.0", commit="c0f9995551400cd46aa460eef817483acb32884a")
    version("1.40.0", commit="5a021bad2b02bee765248391be1d3a7fee3baca9")

    depends_on("r@2.5:", type=("build", "run"))
