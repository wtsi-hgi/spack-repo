# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCardinalworkflows(RPackage):
    """Datasets and workflows for the Cardinal mass spectrometry imaging package

    Datasets and workflows for Cardinal: DESI and MALDI examples including pig fetus, cardinal painting, and human RCC.
    """

    bioc = "CardinalWorkflows"

    version("1.40.0", commit="10794a4eeaefd195ec84616c67b44d00fb70e736")
    version("1.34.0", commit="0a85b419bdd32cda5bd195577159544f875c56e1")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-cardinal", type=("build", "run"))
