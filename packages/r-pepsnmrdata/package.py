# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepsnmrdata(RPackage):
    """Datasets for the PepsNMR package

    This package contains all the datasets used in the PepsNMR package.
    """

    bioc = "PepsNMRData"

    version("1.26.0", commit="25fc7f25cf9342e4997a3dbd2bf90221e86b15a4")
    version("1.20.0", commit="9f8300f1fbcc53864b8aa32db4eb1b2f2c38a282")

    depends_on("r@3.5:", type=("build", "run"))
