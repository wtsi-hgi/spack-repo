# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtdata(RPackage):
    """Data companion to CTexploreR

    Data from publicly available databases (GTEx, CCLE, TCGA and ENCODE) that go with CTexploreR in order to re-define a comprehensive and thoroughly curated list of CT genes and their main characteristics.
    """

    bioc = "CTdata"

    version("1.8.0", commit="382602eb23f9a54e5bf6313fcbd58f636a90c12f")
    version("1.2.0", commit="b5173ccf36aae9f36ac5dc6f584b5152231dcd0b")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
