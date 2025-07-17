# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnphooddata(RPackage):
    """Additional and more complex example data for the SNPhood package

    This companion package for SNPhood provides some example datasets of a larger size than allowed for the SNPhood package. They include full and real-world examples for performing analyses with the SNPhood package.
    """

    bioc = "SNPhoodData"

    version("1.38.0", commit="14607c245a5128fce0d44d640a7611c81ef1784f")
    version("1.32.0", commit="cea39c56cb3d095fae48de1bec79acab8cbc507d")

    depends_on("r@3.2:", type=("build", "run"))
