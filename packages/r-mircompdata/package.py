# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMircompdata(RPackage):
    """Data used in the miRcomp package

    Raw amplification data from a large microRNA mixture / dilution study. These data are used by the miRcomp package to assess the performance of methods that estimate expression from the amplification curves.
    """

    bioc = "miRcompData"

    version("1.38.0", commit="c1dd5a49278f54ee466e13010a655c225dbeea9a")
    version("1.32.0", commit="ca4e514ed7bd9f0dcec21b2fc499f69b2d12de65")

    depends_on("r@3.2:", type=("build", "run"))
