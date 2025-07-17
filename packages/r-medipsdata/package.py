# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedipsdata(RPackage):
    """Example data for MEDIPS and QSEA packages

    Example data for MEDIPS and QSEA packages, consisting of chromosome 22 MeDIP and control/Input sample data. Additionally, the package contains MeDIP seq data from 3 NSCLC samples and adjacent normal tissue (chr 20-22). All data has been aligned to human genome hg19.
    """

    bioc = "MEDIPSData"

    version("1.44.0", commit="00ebad4acfd39f94226372f728a7ebb94247af1e")
    version("1.38.0", commit="055eb8912093646d6db913a94cdeb195ffd9876f")

    depends_on("r@3.5:", type=("build", "run"))
