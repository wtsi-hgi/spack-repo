# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcmap(RPackage):
    """Combination Connectivity Mapping

    Finds drugs and drug combinations that are predicted to reverse or mimic gene expression signatures. These drugs might reverse diseases or mimic healthy lifestyles.
    """

    bioc = "ccmap"

    version("1.34.0", commit="1719f496a05a8774c627eb80c712543a2b6d3227")
    version("1.28.0", commit="9af3dcba1ad41850087bf53ff213b5a39ed7b595")

    depends_on("r-annotationdbi@1.36.2:", type=("build", "run"))
    depends_on("r-biocmanager@1.30.4:", type=("build", "run"))
    depends_on("r-ccdata@1.1.2:", type=("build", "run"))
    depends_on("r-doparallel@1.0.10:", type=("build", "run"))
    depends_on("r-data-table@1.10.4:", type=("build", "run"))
    depends_on("r-foreach@1.4.3:", type=("build", "run"))
    depends_on("r-xgboost@0.6.4:", type=("build", "run"))
    depends_on("r-lsa@0.73.1:", type=("build", "run"))
