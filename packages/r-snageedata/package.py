# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnageedata(RPackage):
    """SNAGEE data

    SNAGEE data - gene list and correlation matrix
    """

    homepage = "http://fleming.ulb.ac.be/SNAGEE"
    bioc = "SNAGEEdata"

    version("1.44.0", commit="27e11a7a31da530c4c505382aa5cc8e7b1d4e5fe")
    version("1.38.0", commit="79ebb8d74a6c45ec8839a5c36ac4b31203c10275")

    depends_on("r@2.6:", type=("build", "run"))
