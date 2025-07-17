# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNdexr(RPackage):
    """NDEx R client library

    This package offers an interface to NDEx servers, e.g. the public server at http://ndexbio.org/. It can retrieve and save networks via the API. Networks are offered as RCX object and as igraph representation.
    """

    homepage = "https://github.com/frankkramer-lab/ndexr"
    bioc = "ndexr"

    version("1.30.0", commit="26b94e3da93edcf19c5bb098105a72884cfcd08f")
    version("1.24.0", commit="dd2784377093893a5bc4d9794701c3a43efd047a")

    depends_on("r-rcx", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
