# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFantom3and4cage(RPackage):
    """CAGE data from FANTOM3 and FANTOM4 projects

    CAGE (Cap Analysis Gene Expression) data from FANTOM3 and FANTOM4 projects produced by RIKEN Omics Science Center.
    """

    bioc = "FANTOM3and4CAGE"

    version("1.44.0", commit="06600b6208aecad6a5b53d82a653f63cdb781efe")
    version("1.38.0", commit="f282f93ce7576950026434347b0772a165e9f9a7")

    depends_on("r@2.15:", type=("build", "run"))
