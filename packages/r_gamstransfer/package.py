# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamstransfer(RPackage):
    """A Data Interface Between 'GAMS' and R

        Read, analyze, modify, and write 'GAMS' (General Algebraic
    Modeling System) data. The main focus of 'gamstransfer' is the
    highly efficient transfer of data with 'GAMS' <https://www.gams.com/>,
    while keeping these operations as simple as possible for the user. The
    transfer of data usually takes place via an intermediate GDX (GAMS Data
    Exchange) file. Additionally, 'gamstransfer' provides utility
    functions to get an overview of 'GAMS' data and to check its validity.
    """

    homepage = "https://github.com/GAMS-dev/transfer-r/tree/main/gamstransfer"
    cran = "gamstransfer"

    version("3.0.1", md5="1f0396b9b32cd1e8a1e75f2861aca470")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-r6@2.5.1:", type=("build", "run"))
    depends_on("r-r-utils@2.11:", type=("build", "run"))
    depends_on("r-collections@0.3.6:", type=("build", "run"))
    depends_on("zlib-api", type=("build", "run", "link"))
