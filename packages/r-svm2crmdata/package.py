# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvm2crmdata(RPackage):
    """An example dataset for use with the SVM2CRM package

    An example dataset for use with the SVM2CRM package.
    """

    bioc = "SVM2CRMdata"

    version("1.40.0", commit="38a5ebd202ce4fa041677970b25d4484be6449a2")
    version("1.34.0", commit="ea82b46060159e673d93d98d7b365ea22aee86e3")

    depends_on("r@3.2:", type=("build", "run"))
