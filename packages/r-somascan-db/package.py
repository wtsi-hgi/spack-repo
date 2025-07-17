# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomascanDb(RPackage):
    """Somalogic SomaScan Annotation Data

    An R package providing extended biological annotations for the SomaScan Assay, a proteomics platform developed by SomaLogic Operating Co., Inc. The annotations in this package were assembled using data from public repositories. For more information about the SomaScan assay and its data, please reference the 'SomaLogic/SomaLogic-Data' GitHub repository.
    """

    homepage = "https://somalogic.com"
    bioc = "SomaScan.db"

    version("0.99.10", commit="7eac7312a74f75e3a28b4a10f79c24d16ffa6739")
    version("0.99.7", commit="4e8e055328c0e1280e11263ec81529f6186b833e")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-annotationdbi@1.56.2:", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db@3.14:", type=("build", "run"))
